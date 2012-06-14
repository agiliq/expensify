# Create your views here.
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from forms import ExpenseCreationForm, CategoryCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
def aclogout(request):

    logout(request)
    return redirect('/')

def aclogin(request):
    redirect_to = request.REQUEST.get('next', '/')
    form = AuthenticationForm(data=request.POST or None)
    if request.POST and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(redirect_to)
            else:
                return HttpResponse('disabled account')
        else:
            return HttpResponse('invalid login')
    else:
        return render(request, 'index.html', {'form': form, 'login':'login'})

'''
def claims(request):
    
    u = UserProfile.objects.all()
    return render(request, 'index.html', {'claims':u})
'''

def index(request):
    
    return render(request, 'index.html', {})

def profile(request):

    u = UserProfile.objects.filter(usr__user=request.user)
    return render(request, 'index.html', {'details':u, 'profile':'profile'})

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
