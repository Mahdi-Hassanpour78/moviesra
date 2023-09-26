from django.db import models


class UsersModel(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True
    )
    email = models.EmailField(unique=True)
    image = models.ImageField()
    registery_date = models.DateTimeField(auto_now_add=True)