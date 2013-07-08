from django.contrib import admin

from models import ExpenseCategory, Expense, UserProfile


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('usr', 'category', 'amount', 'status', 'rejected',
                    'description')
    list_filter = ('usr', 'category', 'status', 'rejected')


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'max_limit')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'max_reimbursment')

admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
