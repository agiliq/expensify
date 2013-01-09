from django.contrib import admin

from models import ExpenseCategory, Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('usr', 'category', 'amount', 'status', 'description')
    list_filter = ('usr', 'category', 'status')


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'max_limit')


admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(Expense, ExpenseAdmin)


