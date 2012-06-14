from django.db import models
from django.contrib.auth.models import User

class EventDetails(models.Model):
    
    title = models.CharField(max_length=500)
    description = models.TextField()
    venue = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __unicode__(self):
        return self.name
    

class ExpenseDetails(models.Model):
    

    travel_to_and_fro_amt = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    local_travel_amt = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    food_amt = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    event_ticket_amt = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)
    any_extra_amt = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)



class UserProfile(models.Model):

    user = models.OneToOneField(User)
    event = models.ForeignKey(EventDetails)
    expense = models.ForeignKey(ExpenseDetails)
    total_amount_claimed = models.DecimalField(max_digits=10,
            decimal_places=0, default=0)

    def __unicode__(self):
        return self.user

