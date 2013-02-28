from django.forms import ModelForm
from django import forms
from models import Expense, ExpenseCategory, UserProfile



class CategoryCreationForm(ModelForm):

    class Meta:
        model = ExpenseCategory


class ExpenseCreationForm(ModelForm):

    class Meta:
        model = Expense
        exclude = ('usr', 'status', 'rejected')

    def __init__(self, user, *args, **kwargs):
        super(ExpenseCreationForm, self).__init__(*args, **kwargs)
        self._user = user

    def save(self, request, commit=True):
        model = super(ExpenseCreationForm, self).save(commit=False)
        model.usr = request.user
        model.save()
        return model

    def clean_amount(self):
        try:
            self.cleaned_data['category']
        except KeyError:
            raise forms.ValidationError("Select Category")
        amount = self.cleaned_data['amount']
        max_limit = self.cleaned_data['category'].max_limit
        if amount > max_limit:
            raise forms.ValidationError("Max limit for this category is %s" %
                                        (max_limit))
        elif amount <= 0:
            raise forms.ValidationError("Amount should be greater than 0.")

        
        up = UserProfile.objects.get_or_create(user=self._user)[0]
        prev_total_requested = up.total_requested_amount
        max_reimbursment = up.max_reimbursment
        total_requested_amount = prev_total_requested + amount
        if total_requested_amount > max_reimbursment:
            raise forms.ValidationError("Please enter amount less than %s. " \
                                        "Current amount crosses max reimbursment of %s"
                                        % (max_reimbursment-prev_total_requested+1,
                                           max_reimbursment))
        return amount
