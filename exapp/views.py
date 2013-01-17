from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from models import ExpenseCategory, Expense
from forms import ExpenseCreationForm, CategoryCreationForm

from datetime import datetime

def oidlogout(request):

    logout(request)
    return redirect('/')

def index(request):
    
    return render(request, 'index.html', {})

@login_required
def profile(request):
    current_year = datetime.now().year
    e = Expense.objects.filter(usr=request.user, date__year=current_year)

    total_amount = 0
    for exp in e:
        total_amount += exp.amount
    return render(request, 'index.html', {'details': e,
        'profile':'profile', 'current_year': current_year,
                        'total_amount': total_amount})

@login_required
def create(request):
    
    form = CategoryCreationForm(data=request.POST or None)

    if form.is_valid():
        form.save(request)
        return redirect(reverse('reimburse'))

    return render(request, 'index.html', {'form': form, 'category':'category'})

@login_required
def reimburse(request):
    
    form = ExpenseCreationForm(request.POST or None, request.FILES or None)


    if form.is_valid():
        form.save(request)
        return redirect(reverse('profile'))

    return render(request, 'index.html', {'form': form})

@staff_member_required
@csrf_exempt
def all_claims(request):
    if request.method == 'POST':
        selected = request.POST['selected'].split(";")
        mark_as = request.POST['mark_as']
        if not (mark_as == "False" or mark_as == "True"):
            raise Http404
        if mark_as == "False":
            mark_as = ""
        for item in selected:
            exp_obj = Expense.objects.get(id=item)
            exp_obj.status = bool(mark_as)
            exp_obj.save()
    expenses = Expense.objects.filter(status=False)
    data = {'expenses': expenses}
    return render_to_response('all_claims.html', data,
            context_instance=RequestContext(request))

