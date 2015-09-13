# -*- coding: utf-8 -*-
from django import forms
from gymonline.apps.gymclient import models

class ClassForm(forms.ModelForm):
    class Meta:
        model = models.Class
        exclude = ['date_updated', 'date_deleted', 'date_created' ]