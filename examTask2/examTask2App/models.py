from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Agent(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=15)
    profile_link = models.URLField()
    total_sales = models.IntegerField()
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class RealEstate(models.Model):
    name = models.CharField(max_length=100)
    location_description = models.TextField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    date_published = models.DateField()
    image = models.ImageField(upload_to='real_estates/')
    characteristics = models.CharField(max_length=260, default="", blank=True, null=True)
    is_reserved = models.BooleanField()
    is_sold = models.BooleanField()

    def __str__(self):
        return f"{self.name}"


class AgentRealEstate(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agent.firstName} {self.agent.lastName} - {self.real_estate.name}"


class Characteristic(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class CharacteristicRealEstate(models.Model):
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.characteristic.name} {self.real_estate.name}"