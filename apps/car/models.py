from django.db import models


class Brand(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=15)

    class Meta:
        ordering = ['name']


class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=25)
    manufacturing_date = models.DateField()
    brand = models.ForeignKey(
        'Brand',
        related_name='cars',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['updated']
        indexes = [models.Index(fields=['brand'])]