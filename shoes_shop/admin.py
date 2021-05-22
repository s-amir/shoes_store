from django.contrib import admin

# Register your models here.
from shoes_shop.models import Customer, Shoes, Employee, Company, OrderRecord


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'size', 'number', 'status', 'company')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(OrderRecord)
class OrderRecordAdmin(admin.ModelAdmin):

    list_display = ('customer_id', 'employee_id', 'shoe_id', 'number', 'date')
    search_fields = ('customer-id', 'employee-id')
    ordering = ['date', 'shoe_id']
