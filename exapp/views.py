# Create your views here.
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from forms import ExpenseCreationForm, CategoryCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from models import ExpenseCategory, Expense

def oidlogout(request):

    logout(request)
    return redirect('/')

'''
def claims(request):
    
    u = UserProfile.objects.all()
    return render(request, 'index.html', {'claims':u})
'''

def index(request):
    
    return render(request, 'index.html', {})

def profile(request):

    e = Expense.objects.filter(usr=request.user)
    total_amount = 0
    for exp in e:
        total_amount += exp.amount
    return render(request, 'index.html', {'details': e, 'profile':'profile', 'total_amount': total_amount})

def create(request):
    
    form = CategoryCreationForm(data=request.POST or None)

    if form.is_valid():
        form.save(request)
        return redirect(reverse('reimburse'))

    return render(request, 'index.html', {'form': form, 'category':'category'})

    
def reimburse(request):
    
    form = ExpenseCreationForm(data=request.POST or None)

    if form.is_valid():
        form.save(request)
        return redirect(reverse('profile'))

    return render(request, 'index.html', {'form': form})
