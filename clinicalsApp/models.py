from django.db import models


# Create your models here.
class Patient(models.Model):
    objects = None
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    age = models.IntegerField()


class ClinicalData(models.Model):
    objects = None
    COMPONENT_NAMES = [('hw', 'Height/weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES,max_length=30)
    componentValue = models.CharField(max_length=30)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
