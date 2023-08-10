<<<<<<< HEAD
from django.contrib import admin
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'accounts'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = [AccountInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
=======
from django.contrib import admin

# Register your models here.
>>>>>>> 8370b914406d0e7e6cc81cdd76708d4004b83da8
