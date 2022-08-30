from django.forms import ModelForm
from .models import Bill

class NewBillForm(ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'amount', 'your_split', 'bill_owner']