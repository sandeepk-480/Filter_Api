from django.db import models

class Data(models.Model):
  ticker = models.CharField(max_length=50)
  date = models.DateField()
  revenue = models.CharField(max_length=50)
  gp = models.CharField(max_length=50)
  fcf = models.CharField(max_length=50)
  capex = models.CharField(max_length=50)

  class Meta:
    indexes = [
        models.Index(fields=['ticker']),
        models.Index(fields=['date']),  
    ]

    