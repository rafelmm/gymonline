from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
from .resources import COUNTRY_CHOICES

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
                        related_name="profile",
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
    # Attributes - Mandatory
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    
    cif = models.CharField(max_length=10, verbose_name=_("CIF"))
    active = models.BooleanField(default=True, editable=False, verbose_name=_("Active"))
    profile = models.CharField(max_length=50, verbose_name=_("Profile"))
    date_created = models.DateTimeField(verbose_name=_("Created at"), 
                                            auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),
                                        auto_now=True)
    
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
        
   
class Center(models.Model):
    # Relations
    gym = models.ForeignKey(Gym, related_name="gym", verbose_name=_("Gym"))
    contact_person = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Contact person"))
    
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
    country = models.CharField(max_length=2, 
                               choices = COUNTRY_CHOICES, 
                               default = 'ES', 
                               verbose_name=_("Country"))
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
        
class Class(models.Model):
    INTENSITY_CHOICES = (
            ('H', _('High')),
            ('M', _('Medium')),
            ('L', _('Low')),
    )
    # Attributes - Mandatory
    active = models.BooleanField(default = True, verbose_name=_("Active"))
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    description = models.CharField(max_length=150,
                                   blank=True,
                                   help_text = _("Write a description for the class (optional)"))
    intensity = models.CharField(max_length=1, 
                                  choices=INTENSITY_CHOICES,
                                  default='M')
    date_created = models.DateTimeField(verbose_name=_("Created at"),auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_("Updated at"),auto_now=True)
    
    # Attributes - Optional
    date_deleted = models.DateTimeField(null=True,
                                  editable=False,
                                  verbose_name=_("Deleted at"))
    popularity = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name=_("Popularity"))
    
    #Manager
    objects = managers.ClassManager()
    
    # Functions
    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.utcnow().replace(tzinfo = utc)
        super(Class, self).save(args, kwargs)
    
    def delete(self):
        self.active = False
        self.date_deleted = datetime.datetime.utcnow().replace(tzinfo = utc)
        self.save()

    # Meta
    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")
        ordering = ["name"]
        