
from django.contrib import admin

from myapp.models import Student

#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name')
#     pass
#
# admin.site.register(Student, StudentAdmin)
admin.site.register(Student)