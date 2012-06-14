# Create your views here.
from django.shortcuts import render
from django.core.urlresolvers import reverse
from forms import ExpenseCreationForm, CategoryCreationForm


#TODO login and login_required

def claims(request):
    
    u = UserProfile.objects.all()
    return render(request, 'index.html', {'claims':u})

def index(request):
    
    return render(request, 'index.html', {})

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
        return redirect(reverse('claims'))

    return render(request, 'index.html', {'form': form})
