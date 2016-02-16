# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    cook = 'cook'
    eater = 'eater'
    USER_TYPE = (
        (cook, 'Cook'),
        (eater, 'Eater'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default=eater)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=6)
    description = models.CharField(max_length=140, blank=True)
    avatar = models.ImageField(upload_to='static/images/avatar', default='static/images/space-th-sm.jpg')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the "
                                                                   "format: '+""999999999'."" Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=11, validators=[phone_regex], blank=True)  # validators should be a list
    receive_updates = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def is_cook(self):
        return self.user_type == cook

    def get_full_address(self):
        return ','.join((self.street, self.city, self.state, self.zip_code))