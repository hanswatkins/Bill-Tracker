from audioop import reverse
from django.db import models
from django.urls import reverse


# Create your models here.

# class Bill(models.Model):
#     name = models.CharField(max_length=100)
#     amount = models.IntegerField()
#     your_split = models.IntegerField()

#     def __str__(self):
#         return f'{self.name} ({self.id})'

#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'bill_id': self.id})

# class BillOwner(models.Model):
#     name = models.CharField(max_length=100)
#     bills = models.ForeignKey(Bill, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.get_name_display()} on {self.bills}"


class BillOwner(models.Model):
    name = models.CharField(max_length=100)
    income = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('add_bill', kwargs={'bill_owner_id' : self.id})

class Bill(models.Model):
    name = models.CharField(max_length=100, default='Untitled Bill')
    amount = models.IntegerField()
    your_split = models.IntegerField()
    bill_owner = models.ForeignKey(BillOwner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name