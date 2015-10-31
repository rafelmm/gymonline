# -*- coding: utf-8 -*-
from .models import GymContact
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = GymContact
        fields = '__all__'
        readonly_fields = ('date',)
        