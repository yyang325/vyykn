from django.db import models
from desktop.models import DeskTop
# Create your models here.
class AlertDevice(models.Model):
    name=models.CharField(max_length=120)
    ip_address=models.CharField(max_length=30)
    status=models.IntegerField()
    desktop=models.ForeignKey(DeskTop)
