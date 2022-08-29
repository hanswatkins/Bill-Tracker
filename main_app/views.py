from pipes import Template
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from main_app.models import Bill

# Create your views here.
class Home(TemplateView):
    template_name = "main_app/home.html"

# class Bills(TemplateView):
#     template_name = "main_app/bills.html"

class BillsList(TemplateView):
    template_name = "main_app/bills_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bills = Bill.objects.all()
        context["bills"] = bills
        return context
        

#     def bills_index(request):
#         bills = Bill.objects.all()
#         return render(request, './templates/main_app/bills.html', { 'bills', bills})

class SignUp(TemplateView):
    template_name = "main_app/signup.html"

class LogIn(TemplateView):
    template_name = "main_app/login.html"

class Create(TemplateView):
    template_name = "main_app/create.html"




