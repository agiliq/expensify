from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.core.mail import send_mail


class ExpenseCategory(models.Model):
    title = models.CharField(max_length=200)
    max_limit = models.DecimalField(max_digits=10,
                                    decimal_places=0, default=0)
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Expense(models.Model):

    usr = models.ForeignKey(User)
    category = models.ForeignKey(ExpenseCategory)
    amount = models.DecimalField(max_digits=10,
                                 decimal_places=0)
    date = models.DateField(auto_now_add=False)
    #A expense claim starts as unpaid.
    status = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    description = models.TextField()
    invoice = models.FileField(upload_to='invoices', null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.usr.first_name, self.usr.last_name)

    class Meta:
        ordering = ['-date']


def notify_via_mail(sender, **kwargs):
    instance = kwargs['instance']
    subject = ""
    email_body = ""
    recipients = \
        list(User.objects.filter(is_superuser=True).values_list('email',
             flat=True))
    recipients.append(instance.usr.email)

    if kwargs['created']:
        subject = 'Reimbursement Claim Created by %s' % instance.usr.username
        email_body = "A new reimbursement claim under category %s, amount %s" \
                     " has been created on date %s.\nDescription : %s" \
                     % (instance.category, instance.amount,
                     instance.date, instance.description)

    if instance.status:
        subject = 'Reimursement Claim Approved'
        email_body = "Your Reimursement Claim dated %s has been approved. " \
                     "An amount of %s has been credited to your account." \
                     "\nDescription : %s"\
            % (instance.date, instance.amount, instance.description)

    send_mail(subject, email_body, 'expensify@agiliq.com', recipients,
              fail_silently=False)

post_save.connect(notify_via_mail, sender=Expense)


def change_username(sender, **kwargs):
    instance = kwargs['instance']
    if instance.username[0:6] == 'openid':
        instance.username = instance.email[0:-11]

pre_save.connect(change_username, sender=User)
