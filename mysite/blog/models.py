from django.db import models
from django.contrib.auth.models import User
    
# This is a models for male human measurements

class MaleMeasurement(models.Model):
    height = models.IntegerField()
    age = models.IntegerField()
    weight = models.IntegerField()
    waist = models.IntegerField()

    def __str__(self):
        return str(self.height)

#end of models for male human measurements   


