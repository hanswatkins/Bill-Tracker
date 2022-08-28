from pipes import Template
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "main_app/home.html"

class Bills(TemplateView):
    template_name = "main_app/bills.html"

class Bills:
    def __init__(self, name, amount, your_share):
        self.name = name
        self.amount = amount
        self.your_share = your_share

bills = [
    Bills("Electricity", "125", "50"),
    Bills("Rent", "1800", "900"),
    Bills("Insurance", "100", "40"),
]

class BillsList(TemplateView):
    template_name = "main_app/bills_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bills"] = bills
        return context

class SignUp(TemplateView):
    template_name = "main_app/signup.html"

class LogIn(TemplateView):
    template_name = "main_app/login.html"

class Create(TemplateView):
    template_name = "main_app/create.html"




