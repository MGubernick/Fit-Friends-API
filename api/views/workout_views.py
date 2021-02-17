from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.workout import Workout
from ..serializers import WorkoutSerializer, WorkoutReadSerializer, UserSerializer

# Create your views here.
class Workouts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = WorkoutSerializer

    def get(self, request):
        """Index ALL Of My Workouts Request"""
        workouts = Workout.objects.all()
        # Run the data through the serializer
        data = WorkoutReadSerializer(workouts, many=True).data
        return Response({ 'workouts': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['workout']['author'] = request.user.id
        # Serialize/create workout
        workout = WorkoutSerializer(data=request.data['workout'])
        # If the workout data is valid according to our serializer...
        if workout.is_valid():
            # Save the created workout
            workout.save()
            return Response({ 'workout': workout.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(workout.errors, status=status.HTTP_400_BAD_REQUEST)

class MyWorkouts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = WorkoutSerializer

    def get(self, request):
        """Index ALL Workouts Request"""
        # Filter the mangos by owner, so you can only see your owned mangos
        workouts = Workout.objects.filter(author=request.user.id)
        # Run the data through the serializer
        data = WorkoutSerializer(workouts, many=True).data
        return Response({ 'workouts': data })

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show A Workout request"""
        # Locate the mango to show
        workout = get_object_or_404(Workout, pk=pk)
        # Only want to show owned workouts?
        # if not request.user.id == workout.author.id:
        #     raise PermissionDenied('Unauthorized, sorry, you do not own this workout...')

        # Run the data through the serializer so it's formatted
        data = WorkoutReadSerializer(workout).data
        return Response({ 'workout': data })

    def delete(self, request, pk):
        """Delete Workout Request"""
        # Locate workout
        workout = get_object_or_404(Workout, pk=pk)
        # Check the owner against the user making the request
        if not request.user.id == workout.author.id:
            raise PermissionDenied('Oops, You\'re Unauthorized, it looks like you do not own this workout...')
        # Only delete if the user owns the  mango
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if request.data['workout'].get('author', False):
            del request.data['workout']['author']

        # Locate the Workout
        # get_object_or_404 returns a object representation of the workout
        workout = get_object_or_404(Workout, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == workout.author.id:
            raise PermissionDenied('Oops, You\'re Unauthorized, looks like you do not own this workout...')

        # Add author to data object now that we know this user owns the resource
        request.data['workout']['author'] = request.user.id
        # Validate updates with serializer
        data = WorkoutSerializer(workout, data=request.data['workout'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
