from django.forms import ModelForm
from models import UserProfile, ExpenseCategory


class CategoryCreationForm(ModelForm):

    class Meta:
        model = ExpenseCategory


class ExpenseCreationForm(ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('usr', 'total_amount_claimed_till_date', 'status')

    def save(self, request, commit=True):
        model = super(ExpenseCreationForm, self).save(commit=False)

        model.usr = request.user.userprofile

        if commit:
            model.save()

        return model
