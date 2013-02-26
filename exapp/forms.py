from django.forms import ModelForm
from django import forms
from models import Expense, ExpenseCategory


class CategoryCreationForm(ModelForm):

    class Meta:
        model = ExpenseCategory


class ExpenseCreationForm(ModelForm):

    class Meta:
        model = Expense
        exclude = ('usr', 'status', 'rejected')

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
            raise forms.ValidationError("Max limit for this category is %s" % (max_limit))
        elif amount <= 0:
            raise forms.ValidationError("Amount should be greater than 0.")
        else:
            return amount

            

