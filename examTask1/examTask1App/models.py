from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    pageLink = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    ownerName = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Automobile(models.Model):
    type = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    maxAllowedSpeed = models.IntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type} {self.maxAllowedSpeed}"


class WorkShop(models.Model):
    name = models.CharField(max_length=100)
    yearFounded = models.IntegerField()
    oldtimerFix = models.BooleanField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ManufacturerWorkShop(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workShop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manufacturer} {self.workShop}"


class AutomobileFix(models.Model):
    code = models.CharField(max_length=50)
    date = models.DateField()
    problemDescription = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    problemImage = models.ImageField()
    automobileInfo = models.ForeignKey(Automobile, on_delete=models.CASCADE, null=True, blank=True)
    workShopInfo = models.ForeignKey(WorkShop, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.code
