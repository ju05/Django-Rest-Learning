from django.db import models

class Report(models.Model):
    TYPE_OPTIONS = (('SUN', 'Sunny'),
                    ('CLO', 'Cloudy'),
                    ('WIN', 'Windy'),
                    ('RAI', 'Rainy'),
                    ('STO', 'Stormy'))
    type = models.CharField(max_length=3, choices= TYPE_OPTIONS)
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
# Create your models here.
