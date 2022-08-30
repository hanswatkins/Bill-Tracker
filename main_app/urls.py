from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bills/', views.Bills.as_view(), name='bills_list'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('create/', views.bill_form, name='create'),
    path('bills/add_bill', views.add_bill, name='add_bill'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]

