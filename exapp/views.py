from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from models import ExpenseCategory, Expense
from forms import ExpenseCreationForm, CategoryCreationForm

def oidlogout(request):

    logout(request)
    return redirect('/')

def index(request):
    
    return render(request, 'index.html', {})

@login_required
def profile(request):

    e = Expense.objects.filter(usr=request.user)
    total_amount = 0
    for exp in e:
        total_amount += exp.amount
    return render(request, 'index.html', {'details': e, 'profile':'profile', 'total_amount': total_amount})

@login_required
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
