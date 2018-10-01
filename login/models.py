from django.db import models

class Login(models.Model):
    login =  models.CharField(max_length= 12)
    senha = models.IntegerField()