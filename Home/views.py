from django.shortcuts import render, redirect
from django.db.models import Sum, Avg
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView

from Home.models import *
from .forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

# Create your views here.

# Pages
def index(request):
  sales(request)
  return render(request, 'pages/index.html', { 'segment': 'index' })

def accounts(request):
  return render(request, 'pages/accounts.html', { 'segment': 'accounts' })

def catalog(request):
  return render(request, 'pages/catalog.html', { 'segment': 'catalog' })

def reports(request):
  return render(request, 'pages/reports.html', { 'segment': 'reports' })

def settings(request):
  return render(request, 'pages/settings.html', { 'segment': 'settings' })

def profile(request):
  return render(request, 'pages/profile.html', { 'segment': 'profile' })



# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Register failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'accounts/register.html', context)

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def products(request):
  products = Product.objects.all()
  return render(request, 'pages/catalog.html', {'product': products})

def services(request):
  services = Service.objects.all()
  return render(request, 'pages/catalog.html', {'service': services})

def sales(request):
  sales = Sale.objects.aggregate(Avg('sale_amount'))
  return render(request, 'pages/reports.html', {'sales': sales})

def pos(request):
  product = Product.objects.all()
  return render(request, 'pages/pos.html', {'products': product})

#def add_to_cart(request):
  #product = Product.objects.filter