from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create Workout models here.
class Workout(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  CATEGORY_CHOICES = [
    ('Upper Body', 'UB'),
    ('Lower Body', 'LB'),
    ('Core', 'C'),
    ('Cardio', 'GO'),
    ('Full Body', 'FB'),
    ('Recovery', 'Re')
  ]

  title = models.CharField(max_length=100)
  author = models.ForeignKey(
    get_user_model(),
    related_name='workouts',
    on_delete=models.CASCADE
  )
  difficulty = models.IntegerField(
    default=1,
    validators=[MaxValueValidator(5), MinValueValidator(1)]
  )
  category = models.CharField(
    max_length=20,
    choices=CATEGORY_CHOICES
    )
  description = models.CharField(max_length=8000)


  favorites = models.ManyToManyField(
    get_user_model(),
    through='Favorite',
    through_fields=('workout_id', 'user_id'),
    blank=True,
    related_name='favorites'
  )


  def __str__(self):
    # This must return a string
    """Returns a string variation of Workout Model"""
    return str(self.id)

  def as_dict(self):
    """Returns dictionary version of Workout Model"""
    return {
        'id': self.id,
        'title': self.title,
        'author': self.author,
        'difficulty': self.difficulty,
        'category': self.category,
        'description': self.description
    }
