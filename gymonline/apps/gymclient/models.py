# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
from gymonline.settings import LANGUAGES
import datetime


from gymonline.apps.gymclient import managers

# Create your models here.
  
class Profile(models.Model):
    GENDER_CHICES = (
            ('M', _('Male')),
            ('F', _('Female')),
    )
    
    # Relations
    user = models.OneToOneField(
                        settings.AUTH_USER_MODEL,
                        related_name="custom_user_profile",
                        verbose_name=_("user")
    )
    
    # Attributes - Mandatory
    birthday = models.DateField(verbose_name=_("Birthday"))
    gender = models.CharField(max_length=1,
                              choices = GENDER_CHICES,
                              default = 'M',
                              verbose_name=_("Gender"))
    postal_code = models.CharField(max_length=5,
                                   verbose_name=_("Postal code"))
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),auto_now=True)
    # Attributes - Optional
    date_deleted = models.DateTimeField(null=True, editable=False, verbose_name=_("Deleted at"))
    phone = models.IntegerField(verbose_name=_("Phone number"), 
                                null=True, 
                                blank=True)
    nif = models.CharField(max_length=10,
                           verbose_name=_("NIF"),
                           null=True, 
                           blank=True)
    city = models.CharField(max_length=50,
                            verbose_name=_("City"),
                            null=True,
                            blank=True)
    address = models.CharField(max_length=150,
                               verbose_name=_("Address"),
                               null=True,
                               blank=True)
    
    # Object Manager
    objects = managers.ProfileManager()
    
    # Custom Properties
    @property
    def username(self):
        return self.user.username
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    # Methods
    def delete(self):
        self.user.is_active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.user.save()
        self.save()
          
    # Meta and String
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",)
 
    def __str__(self):
        return self.user.username
    
class Gym(models.Model):
    # Relations
    contact_person = models.ForeignKey(
                                       settings.AUTH_USER_MODEL, 
                                       related_name="gym_contact_person",
                                       verbose_name=_("Gym Contact person"))
    
    # Attributes - Mandatory
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    
    cif = models.CharField(max_length=10, verbose_name=_("CIF"))
    active = models.BooleanField(default=True, editable=False, verbose_name=_("Active"))
    profile = models.CharField(max_length=50, verbose_name=_("Profile"))
    date_created = models.DateTimeField(verbose_name=_("Created at"), 
                                            auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),
                                        auto_now=True)
    number_of_views = models.IntegerField(verbose_name=_("Number of views"),
                                          default = 0,
                                          editable = False)
    mark = models.DecimalField(max_digits=2, 
                               decimal_places=1,
                               default = 0,
                               editable = False,
                               verbose_name=_("Mark"))
    # Attributes - Optional
    date_deleted = models.DateTimeField(verbose_name=_("Deleted at"),
                                        null=True,
                                        editable=False)
    # Manager
    object = managers.GymManager()
    
    # Functions
    def delete(self):
        self.active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.save()
        
    def __unicode__(self):
        return self.name

    # Meta
    class Meta:
        verbose_name = _("Gym")
        verbose_name_plural = _("Gyms")
        ordering = ["name"]
        
class Country(models.Model):
    # Attributes - Mandatory
    language = models.CharField(max_length=2, 
                                choices = LANGUAGES,
                                default = 'es')
    name = models.CharField(max_length=50,
                            verbose_name = _("Name")) 
    
    # Functions
    def __unicode__(self):
        return self.name
    
    # Meta
    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ["language", "name"]
        
class Center(models.Model):
    # Relations
    gym = models.ForeignKey(Gym, related_name="belongs_to_gym", verbose_name=_("Gym"))
    contact_person = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                       related_name="center_contact_person",
                                       verbose_name=_("Center Contact person"))
    country = models.ForeignKey(Country, 
                                related_name="center_country", 
                                verbose_name=_("Country"))
    
    # Attributes - Mandatory
    active = models.BooleanField(default=True, editable=False)
    name = models.CharField(max_length=150, verbose_name=_("Center Name"))
    date_created = models.DateTimeField(auto_now_add=True, 
                                        editable=False, 
                                        verbose_name=_("Created at"))
    date_updated = models.DateTimeField(auto_now = True, 
                                        editable=False, 
                                        verbose_name=_("Updated at"))
    
    address = models.CharField(max_length=250, verbose_name=_("Address"))
    postal_code = models.CharField(max_length=5, verbose_name=_("Postal Code"))
    region = models.CharField(max_length=20, verbose_name=_("Region"))
    number_of_views = models.IntegerField(verbose_name=_("Number of views"),
                                          default = 0,
                                          editable = False)
    mark = models.DecimalField(max_digits=2, 
                               decimal_places=1,
                               default = 0,
                               editable = False,
                               verbose_name=_("Mark"))
    # Attributes - Optional
    date_deleted = models.DateTimeField(null=True, editable=False, verbose_name=_("Deleted at"))
           
    # Manager
    object = managers.CenterManager()
    
    # Functions
    def delete(self):
        self.active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.save()
        
    def __unicode__(self):
        return "%s - %s" %(self.gym.name, self.name)

    # Meta
    class Meta:
        verbose_name = _("Gym Center")
        verbose_name_plural = _("Gym Centers")
        ordering = ["name"]
     
class IntensityLevel(models.Model):
    # Attributes - Mandatory
    language = models.CharField(max_length=2, 
                                choices = LANGUAGES,
                                default = 'es')
    description = models.CharField(max_length=20,
                                   verbose_name = _("Description")) 
      
    # Functions
    def __unicode__(self):
        return self.description
    
    # Meta
    class Meta:
        verbose_name = _("Intensity Level")
        verbose_name_plural = _("Intensity Levels")
        ordering = ["language", "description"]
    
class Monitor(models.Model):
    # Relations
    user = models.OneToOneField(
                        settings.AUTH_USER_MODEL,
                        related_name="monitor_user_profile",
                        verbose_name=_("user"))
    gym = models.ForeignKey(Gym, 
                            related_name="monitor_gym",
                            verbose_name=_("Gym"))
              
    # Attributes - Mandatory
    active = models.BooleanField(default = True, 
                                 verbose_name=_("Active"))
    date_created = models.DateTimeField(verbose_name=_("Created at"),
                                        auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),
                                        auto_now=True)
    number_of_views = models.IntegerField(verbose_name=_("Number of views"),
                                          default = 0,
                                          editable = False)
    mark = models.DecimalField(max_digits=2, 
                               decimal_places=1,
                               default = 0,
                               editable = False,
                               verbose_name=_("Mark"))
    # Attributes - Optional
    date_deleted = models.DateTimeField(null=True,
                                  editable=False,
                                  verbose_name=_("Deleted at"))
    #Manager
    objects = managers.MonitorManager()
    
    # Functions
    def __unicode__(self):
        return ' '.join([self.user.first_name, self.user.last_name])
    
    def delete(self):
        self.active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.save()

    # Meta
    class Meta:
        verbose_name = _("Monitor")
        verbose_name_plural = _("Monitors")
            
class GymClass(models.Model):
    # Relations
    intensity  = models.ForeignKey(IntensityLevel, 
                                   related_name="class_intensity",
                                   verbose_name=_("Intensity Level"))
    monitor = models.ForeignKey(Monitor,
                                related_name="monitor_of_class",
                                verbose_name=_("Monitor"))
    # Attributes - Mandatory
    active = models.BooleanField(default = True, verbose_name=_("Active"))
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    description = models.CharField(max_length=500,
                                   blank=True,
                                   help_text = _("Write a description for the class (optional)"),
                                   verbose_name = _("Description"))
    date_created = models.DateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),auto_now=True)
    number_of_views = models.IntegerField(verbose_name=_("Number of views"),
                                          default = 0,
                                          editable = False)
    mark = models.DecimalField(max_digits=2, 
                               decimal_places=1,
                               default = 0,
                               editable = False,
                               verbose_name=_("Mark"))
    # Attributes - Optional
    date_deleted = models.DateTimeField(null=True,
                                  editable=False,
                                  verbose_name=_("Deleted at"))
    popularity = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name=_("Popularity"))
    #Manager
    objects = managers.GymClassManager()
    
    # Functions
    def __unicode__(self):
        return self.name
    
    def delete(self):
        self.active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.save()

    # Meta
    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")
        ordering = ["name"]
        
class GymClassSession(models.Model):
    # Relations
    gymClass = models.ForeignKey(GymClass,
                                 related_name="session_of_class",
                                 verbose_name=_("Class"))
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    description = models.CharField(max_length=500,
                                   blank=True,
                                   help_text = _("Write a description for the session (optional)"),
                                   verbose_name = _("Description"))
    
    date_created = models.DateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),auto_now=True)
    number_of_views = models.IntegerField(verbose_name=_("Number of views"),
                                          default = 0,
                                          editable = False)
    mark = models.DecimalField(max_digits=2, 
                               decimal_places=1,
                               default = 0,
                               editable = False,
                               verbose_name=_("Mark"))
    # Attributes - Optional
    date_deleted = models.DateTimeField(null=True,
                                  editable=False,
                                  verbose_name=_("Deleted at"))
    popularity = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name=_("Popularity"))
    #Manager
    objects = managers.GymClassSessionManager()
    
    # Functions
    def __unicode__(self):
        return self.name
    
    def delete(self):
        self.active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.save()

    # Meta
    class Meta:
        verbose_name = _("Class Session")
        verbose_name_plural = _("Class Sessions")
        ordering = ["name"]