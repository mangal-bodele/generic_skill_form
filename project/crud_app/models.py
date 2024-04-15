from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField()
    skill = models.CharField(max_length=10)
    fees = models.IntegerField()
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.name
