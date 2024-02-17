from django.db import models

# Create your models here.
class SignIn(models.Model):
    email = models.TextField(max_length=120)
    password = models.TextField(max_length=50)
    token = models.TextField()
    signInTime = models.DateTimeField()

class SignUp(models.Model):
    UName = models.CharField(max_length=120)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.TextField(max_length=50)
    signUpTime = models.DateTimeField()