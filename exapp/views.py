from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from models import Expense
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
    e = Expense.objects.filter(usr=request.user, date__year=current_year).order_by('-rejected', 'status', '-date')
    rejected_count = e.filter(rejected=True, status=False).count()
    pending_count = e.filter(rejected=False, status=False).count()
    claimed_count = e.filter(rejected=False, status=True).count()

    total_amount = 0
    for exp in e:
        total_amount += exp.amount

    paginator = Paginator(e, 10)
    page = request.GET.get('page')
    try:
        e = paginator.page(page)
    except PageNotAnInteger:
        e = paginator.page(1)
    except EmptyPage:
        e = paginator.page(paginator.num_pages)



    return render(request, 'index.html', {'details': e,
        'profile':'profile', 'current_year': current_year,
        'total_amount': total_amount, 'rejected_count': rejected_count,
        'pending_count': pending_count, 'claimed_count': claimed_count})

@login_required
def create(request):
    
    form = CategoryCreationForm(data=request.POST or None)

    if form.is_valid():
        form.save()
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
        if (len(selected) == 0 or selected[0] == u''):
            messages.add_message(request, messages.ERROR, 'Please select atleast one before submitting.')
            expenses = Expense.objects.filter(status=False)
            data = {'expenses': expenses}
            return render_to_response('all_claims.html', data,
                    context_instance=RequestContext(request))

        mark_as = request.POST['mark_as']

        if not ( mark_as == "True" or mark_as == 'rejected'):
            raise Http404
        status = False
        reject = False
        if mark_as == "True":
            status = True
            reject = False
        elif mark_as == "rejected":
            status = ""
            reject = True

        for item in selected:
            exp_obj = Expense.objects.get(id=item)
            exp_obj.status = status
            exp_obj.rejected = reject
            exp_obj.save()
    expenses = Expense.objects.filter(status=False)
    rejected_count = expenses.filter(rejected=True).count()
    pending_count = expenses.filter(rejected=False).count()


    paginator = Paginator(expenses, 10)
    page = request.GET.get('page')
    try:
        expenses = paginator.page(page)
    except PageNotAnInteger:
        expenses = paginator.page(1)
    except EmptyPage:
        expenses = paginator.page(paginator.num_pages)

    data = {'expenses': expenses, 'rejected_count': rejected_count,
            'pending_count': pending_count}
    return render_to_response('all_claims.html', data,
            context_instance=RequestContext(request))


@staff_member_required
@csrf_exempt
def approved_claims(request):
    expenses = Expense.objects.filter(status=True, rejected=False)
    approved_count = expenses.count()
    paginator = Paginator(expenses, 10)
    page = request.GET.get('page')
    try:
        expenses = paginator.page(page)
    except PageNotAnInteger:
        expenses = paginator.page(1)
    except EmptyPage:
        expenses = paginator.page(paginator.num_pages)
    data = {'expenses': expenses, 'approved_count': approved_count}
    return render_to_response('approved_claims.html', data,
            context_instance=RequestContext(request))

