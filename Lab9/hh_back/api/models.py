from django.db import models

class Company(models.Model):
    name = models.CharField()
    description = models.TextField()
    city = models.CharField()
    address = models.TextField()

class Vacancy(models.Model):
    name = models.CharField()
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey()
