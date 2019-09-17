from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userschedule(models.Model):
	item =  models.CharField(max_length=100)
	time =  models.TimeField()
	duration = models.CharField(max_length=100)
	userref = models.ForeignKey(User,on_delete = models.CASCADE)