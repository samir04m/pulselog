from django.contrib.auth import get_user_model
from django.db import models

class HealthMeasurement(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    annotation = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']

class FoodLog(models.Model):
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']