from django.contrib import admin
from .models import Bill, BillOwner

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillOwner)
