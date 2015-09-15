# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# Register your models here.

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False
    verbose_name_plural = _("Profiles")

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)

class CenterInline(admin.StackedInline):
    model = models.Center
    verbose_name_plural = _("Centers")
    extra = 1

class GymAdmin(admin.ModelAdmin):
    inlines = (CenterInline, )
    
admin.site.register(models.Gym, GymAdmin)
