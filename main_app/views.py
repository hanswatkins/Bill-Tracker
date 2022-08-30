from pipes import Template
from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bill
from .forms import NewBillForm


# Create your views here.
class Home(TemplateView):
    template_name = "main_app/home.html"

class Bills(TemplateView):
    template_name = "main_app/bills_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bills = Bill.objects.all()
        context["bills"] = bills
        return context

        
    # def bills_index(request):
    #     bills = Bill.objects.all()
    #     return render(request, './templates/main_app/bills.html', { 'bills', bills})

# class BillsList(TemplateView):
#     template_name = "main_app/bills_list.html"

class SignUp(TemplateView):
    template_name = "main_app/signup.html"

class LogIn(TemplateView):
    template_name = "main_app/login.html"

# class Create(View):
#     template_name = "main_app/create.html"

def bill_form(request):
    new_bill_form = NewBillForm()
    return render(request, 'main_app/create.html', {
    'new_bill_form': new_bill_form
        })

def add_bill(request):
    form = NewBillForm(request.POST)
    if form.is_valid():
        new_bill = form.save(commit=False)
        new_bill.save()
        return redirect('bills')
        
class BillCreate(CreateView):
    model = Bill
    fields = '__all__'
    success_url = '/bills/'






