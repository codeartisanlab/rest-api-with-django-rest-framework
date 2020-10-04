from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['full_name','email','contact','address']
admin.site.register(Employee,EmployeeAdmin)
