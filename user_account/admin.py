from django.contrib import admin
from user_account.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email','first_name','last_name',]
