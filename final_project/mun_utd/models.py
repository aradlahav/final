from django.db import models


class Player(models.Model):
    objects = None
    number = models.IntegerField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    hire_date = models.IntegerField()
    position = models.CharField(max_length=3)
    second_position = models.CharField(max_length=4)
    salary = models.IntegerField()
    max_bonus = models.IntegerField()
    picture = models.ImageField()
    slug = models.SlugField(default='player')

    def __str__(self):
        return self.last_name



