from django.db import models
from django.contrib.auth.models import User

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
