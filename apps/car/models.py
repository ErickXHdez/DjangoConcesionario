from django.db import models

class Brand(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=15)