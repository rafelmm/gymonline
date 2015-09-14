# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.timezone import utc
from . import models

# Create your tests here.
class TestProfileModel(TestCase):
    
    def test_profile_creation(self):
        User = get_user_model()
        # New user created
        user = User.objects.create(
                username="testuser", password="testuser")
        
        p = models.Profile(
                    user = user,
                    birthday = datetime(1984, 2, 21,tzinfo = utc),
                    gender = 'M',
                    postal_code = '08440')
        p.save()
        # Check that a Profile instance has been created
        self.assertIsInstance(user.profile, models.Profiles