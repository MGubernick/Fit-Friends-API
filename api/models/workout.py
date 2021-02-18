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



  def __str__(self):
    # This must return a string
    """Returns a string variation of Workout Model"""
    return f"The workout titled '{self.name}' was written by {self.author} and falls into the category: {self.category}. The difficulty level is {self.difficulty} and here are the exercises and details: {self.description}."

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
