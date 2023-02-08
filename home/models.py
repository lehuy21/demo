from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel (models.Model):
    username = models.CharField(max_length=200)
    password = models.IntegerField()
    re_password = models.IntegerField()

    class meta:
        models = User
        fields = ["username", "password", "re_password"]
