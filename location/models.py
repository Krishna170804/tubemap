from django.db import models

# Create your models here.
# Database is created here using the concept of inheritance.
# Uses inheritance to get attributes and methods from Model function to Location

class Location(models.Model):
    start_point = models.CharField("Start Point", max_length=100)
    check_point_1 = models.CharField("Check point 1", max_length=100, blank = True, null=True)
    check_point_2 = models.CharField("Check point 2", max_length=100, blank = True, null=True)
    check_point_3 = models.CharField("Check point 3", max_length=100, blank = True, null=True)
    end_point = models.CharField("End Point", max_length=100)

    def __str__(self):
        """String representation of model"""
        return str(self.start_point)