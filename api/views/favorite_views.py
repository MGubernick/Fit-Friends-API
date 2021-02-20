from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.favs import Favorite
from ..serializers import FavoriteSerializer, FavoriteReadSerializer

# views here

class Favorites(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)

    def get(self, request):
      """Index A Users Favorites Request"""
      favorites = Favorite.objects.filter(user_id=request.user.id)
      data = FavoriteReadSerializer(favorites, many=True).data
      return Response({ 'favorites': data })

    serializer_class = FavoriteSerializer
    def post(self, request):
        """Post Request for Favs"""
        favorite = FavoriteSerializer(data=request.data)
        if favorite.is_valid():
            f = favorite.save()
            return Response(favorite.data, status=status.HTTP_201_CREATED)
        else:
            return Response(favorite.errors, status=status.HTTP_400_BAD_REQUEST)

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        """Show Request"""
        favorite = get_object_or_404(Favorite, pk=pk)
        data = FavoriteReadSerializer(favorite).data
        return Response({ 'favorite': data })

    def patch(self, request, pk):
        """Update Favorite"""
        favorite = get_object_or_404(Favorite, pk=pk)
        ms =FavoriteSerializer(favorite, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response({ 'favorite': ms.data })
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Favorite"""
        favorite = get_object_or_404(Favorite, pk=pk)
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
