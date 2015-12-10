from django.db import models

# Create your models here.
class DeskTop(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=120)
    password=models.CharField(max_length=30, blank=False)




