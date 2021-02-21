from django.urls import path
from .views.workout_views import Workouts, WorkoutDetail, MyWorkouts
from .views.user_views import Users, UserDetail, SignUp, SignIn, SignOut, ChangePassword
from .views.favorite_views import Favorites, FavoriteDetail

urlpatterns = [
  	# Restful routing
    # Workout Views
    path('workouts', Workouts.as_view(), name='workouts'),
    path('workouts/<int:pk>', WorkoutDetail.as_view(), name='workout_detail'),
    path('myworkouts', MyWorkouts.as_view(), name='myworkouts'),
    # User Path
    path('secret-user-path/', Users.as_view(), name='user_path'),
    path('one-user/<int:pk>', UserDetail.as_view(), name='one_user'),
    # Favorite Paths
    path('favorites', Favorites.as_view(), name='favorites'),
    path('favorite/<int:pk>', FavoriteDetail.as_view(), name='favorite_detail'),
    # Auth Paths
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
