from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_organiser', 'details_set']
    fieldsets = (
        (('User'), {'fields': ('username', 'email', 'is_organiser', 'details_set')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
