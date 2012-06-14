from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    
    def __unicode__(self):
        return self.title
    

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    expense = models.ForeignKey(ExpenseCategory)
    total_amount_claimed = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)

    def __unicode__(self):
        return self.user

