from django.db import models

# Create your models here.
class Bill(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    your_split = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
