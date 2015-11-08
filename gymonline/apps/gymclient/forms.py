# -*- coding: utf-8 -*-
from django import forms
from gymonline.apps.gymclient import models
from django.contrib.auth.models import Group

class ClassForm(forms.ModelForm):
    class Meta:
        model = models.GymClass
        exclude = ['date_updated', 'date_deleted', 'date_created' ]
  
class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
              
class MySignupForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = models.Profile
        fields = ['gender', 'birthday', 'postal_code']
        
    def signup(self, request, user):
        profile = models.Profile(user = user, 
                                 gender = self.cleaned_data['gender'],
                                 birthday = self.cleaned_data['birthday'],
                                 postal_code = self.cleaned_data['postal_code'])
        g = Group.objects.get(name='USR')
        user.groups.add(g)
        profile.save()
        
        