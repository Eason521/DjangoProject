from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return self.name

