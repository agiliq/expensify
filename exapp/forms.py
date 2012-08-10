from django.forms import ModelForm
from models import Expense, ExpenseCategory


class CategoryCreationForm(ModelForm):

    class Meta:
        model = ExpenseCategory


class ExpenseCreationForm(ModelForm):

    class Meta:
        model = Expense
        exclude = ('usr', 'status')

    def save(self, request, commit=True):
        model = super(ExpenseCreationForm, self).save(commit=False)

        model.usr = request.user

        model.save()

        return model
