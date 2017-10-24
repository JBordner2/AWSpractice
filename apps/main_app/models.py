# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User
import re

class PetManager(models.Manager):
        def validate(self, postData):
                results = {
                        'errors' : [] 
                }
                if len(postData['name']) < 3:
                        results['errors'].append("Please enter a valid pet name")
                if len(postData['kind']) < 3:
                        results['errors'].append("please enter a valid type of pet")
                for key in postData:
                        if re.search(' ',postData[key]):
                                results['errors'].append('No space please')
                return results

class Pet(models.Model):
        name = models.CharField(max_length = 255)
        kind = models.CharField(max_length = 255)
        owner = models.ForeignKey(User, related_name= 'pets')
        objects = PetManager()
