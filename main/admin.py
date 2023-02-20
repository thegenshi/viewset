from django.contrib import admin
from .models import Students
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    
admin.site.register(Students)