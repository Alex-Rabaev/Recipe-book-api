from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.JSONField()
    instructions = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
