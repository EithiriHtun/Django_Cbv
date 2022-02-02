from django.contrib import admin
from CbvApp.models import School,Student

class StudentAdmin(admin.ModelAdmin):

    fields = ['school','name','age']

    search_fileds = ['name','school']

    list_filter = ['name','age','school']

    list_display = ['school','name','age']

    list_editable = ['age']

# Register your models here.
admin.site.register(School)
admin.site.register(Student,StudentAdmin)