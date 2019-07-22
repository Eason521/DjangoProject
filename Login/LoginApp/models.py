from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.username

class Grade(models.Model):
    pass