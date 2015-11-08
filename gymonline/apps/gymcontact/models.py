# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class GymContact(models.Model):
    # Relations
    
    # Attributes - Mandatory
    company = models.CharField(max_length=150,
                               verbose_name=_("Your company"))
    name = models.CharField(max_length=150,
                            verbose_name=_("Your name"))
    phone = models.CharField(max_length=20,
                             verbose_name=_("Your phone"))
    email = models.EmailField(verbose_name=_("Your email"))
    
    date = models.DateTimeField(auto_now = True,
                                verbose_name = _("Created at"))
    
    message = models.TextField(max_length=1000,
                               verbose_name=_("Your message"),
                               blank=True,
                               null=True)
    # Functions
    def __unicode__(self):
        return "%s, %s, %s" %(self.name, self.phone, self.email)