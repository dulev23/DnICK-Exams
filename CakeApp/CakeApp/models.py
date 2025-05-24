from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Baker(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='cakes/', null=True, blank=True)
    baker = models.ForeignKey('Baker', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.price}"
