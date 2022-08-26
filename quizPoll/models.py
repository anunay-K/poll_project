from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Questions(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    questions = models.TextField()
    option_one=models.CharField(max_length=30)
    option_two=models.CharField(max_length=30)
    option_three=models.CharField(max_length=30)
    option_foure=models.CharField(max_length=30)
    option_one_count=models.IntegerField(default=0)
    option_two_count=models.IntegerField(default=0)
    option_three_count=models.IntegerField(default=0)
    option_foure_count=models.IntegerField(default=0)
    
    
