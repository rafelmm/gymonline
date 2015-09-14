# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.query import QuerySet

class CustomQuerySet(QuerySet):
    def delete(self):
        self.update(active=False)
    
class ProfileManager(models.Manager):
    def active(self):
        return self.model.objects.filter(active=True)
    
    def get_query_set(self):
        return CustomQuerySet(self.model, using=self._db)
 
class GymManager(models.Manager):
    def active(self):
        return self.model.objects.filter(active=True)
    
    def get_query_set(self):
        return CustomQuerySet(self.model, using=self._db)

class ClassManager(models.Manager):
    def active(self):
        return self.model.objects.filter(active=True)
    
    def get_query_set(self):
        return CustomQuerySet(self.model, using=self._db)

