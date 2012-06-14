from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail


class ExpenseCategory(models.Model):
    
    title = models.CharField(max_length=200)
    max_limit = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    description = models.TextField()
        
    def __unicode__(self):
        return self.title
    

class UserProfile(models.Model):

    usr = models.OneToOneField(User)
    expense_category = models.ForeignKey(ExpenseCategory)
    amount = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    date = models.DateField(auto_now_add=False)
    total_amount_claimed_till_date = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    status = models.BooleanField()

    def __unicode__(self):
        return self.user

def notify_via_mail(sender, **kwargs):
    instance = kwargs['instance']
    subject = ""; email_body = ""
    recipients = \
        list(User.objects.filter(is_superuser=True).values_list('email'
             , flat=True))
    recipients.append(instance.usr.user.email)
    
    if kwargs['created']:
        subject = 'Reimbursement Claim Created by %s' % instance.usr.user
        email_body = "A new reimbursement claim under category %s, amount %s has been created on date %s." \
            %(instance.expense_category, instance.amount, instance.date)
    
    if instance.status == True:
        subject = 'Reimursement Claim Approved'
        email_body = "Your Reimursement Claim dated %s has been approved. An amount of %s has been credited to your account."\
            %(instance.date, instance.amount)
        
    send_mail(subject, email_body, 'expensify@agiliq.com', recipients,
              fail_silently=False)

post_save.connect(notify_via_mail, sender=UserProfile)