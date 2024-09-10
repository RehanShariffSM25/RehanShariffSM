from django.db import models

class ModelA(models.Model):
    name = models.CharField(max_length=100)

class ModelB(models.Model):
    related_model = models.ForeignKey(ModelA, on_delete=models.CASCADE)
