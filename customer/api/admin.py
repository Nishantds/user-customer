from django.contrib import admin
from.models import Customer,User
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','profile_no','user')


class UserAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','mobile_no')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(User,UserAdmin)