from django.db import models
from django.contrib.auth import get_user_model

class Favorite(models.Model):
    workout_id = models.ForeignKey('Workout', on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.workout_id
