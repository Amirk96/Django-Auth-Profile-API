from django.contrib import admin
from myprofile.models import MyProfileModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for MyProfile model
# which acts a bit like a singleton
class MyProfileInline(admin.StackedInline):
    model = MyProfileModel
    can_delete = False
    verbose_name_plural = 'Profiles'   

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (MyProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)