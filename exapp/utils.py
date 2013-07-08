from django.contrib.auth.models import User
from django.db.models import Sum

from exapp.models import UserProfile, Expense


def populate_userprofile():
    '''
    MUST READ:
    This populates the total_requested_amount field of model UserProfile
    with the sum of all his expenses.


    Should not use in the middle because, whenever certain approved expenses
    are removed from the database, this script wont have access to those
    deleted records and hence the amount from those deleted records wont
    be added to the total_requested_amount. But, that should not happen.

    '''
    users = User.objects.all()
    for u in users:
        t = Expense.objects.filter(usr=u).\
            aggregate(Sum('amount'))['amount__sum']
        if not t:
            t = 0
        up = UserProfile.objects.get_or_create(user=u)[0]
        up.total_requested_amount = t
        up.save()
