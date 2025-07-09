from django.contrib import admin
from .models import BloodPressureMeasurement, FoodLog

@admin.register(BloodPressureMeasurement)
class BloodPressureMeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'systolic', 'diastolic', 'pulse', 'annotation', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user__username', 'annotation')
    ordering = ('-date',)

@admin.register(FoodLog)
class FoodLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user__username', 'description')
    ordering = ('-date',)
