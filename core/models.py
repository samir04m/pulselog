from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models

class BloodPressureMeasurement(models.Model):
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField()
    annotation = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{} [{}]'.format(self.date, self.user)

class FoodLog(models.Model):
    description = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=timezone.now)
    user =  models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{} - {} [{}]'.format(self.description, self.date, self.user)