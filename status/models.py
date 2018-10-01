from django.db import models

class Status(models.Model):
    id_status = models.IntegerField(primary_key= True)
    status = models.CharField(max_length= 100)
