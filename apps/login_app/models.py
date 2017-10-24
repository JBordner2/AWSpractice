from __future__ import unicode_literals

from django.db import models
#We import re to use for validating emails
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]+$')
#Make sure to check for alphanumeric in python. This was left out of the demo
class UserManager(models.Manager):
        def loginVal(self, postData):
                results = {'errors': [], 'status' : False, 'user': None }
                email_matches = self.filter(email = postData['email'])
                if len(email_matches) == 0:
                        results['errors'].append('Please check your email and password and try again')
                        results['status'] = True
                else:
                        #Line below is grabbing the first email in the email_matches array
                        results['user'] = email_matches[0]
                        if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                                results['errors'].append('Please check your email and password and try again')
                                results['status'] = True
                return results


        def createUser(self, postData):
                password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                print password
                self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = password)
                
        def registerVal(self, postData):
                results = {'errors': [], 'status': False}
                if len(postData['first_name']) < 2: 
                        results['status'] = True
                        results['errors'].append('first name is too short')
                if len(postData['last_name']) < 2: 
                        results['status'] = True
                        results['errors'].append('last name is too short')
                if not EMAIL_REGEX.match(postData['email']): 
                        results['status'] = True
                        results['errors'].append('Email is not valid')
                if len(postData['password']) < 3: 
                        results['status'] = True
                        results['errors'].append('password is too short')
                if postData['password'] != postData['c_password']:
                        results['status'] = True
                        results['errors'].append('passwords do not match')
                
                #The line below is saying to grab all the emails that are the same as the postData['email'] and if there are any emails at all, then we know that the user already exists in the database
                user = self.filter(email = postData['email'])
                if len(user) > 0:
                        results['status'] = True
                        results['errors'].append('User already exist in database')

                return results

class User(models.Model):
        first_name = models.CharField(max_length = 100)
        last_name = models.CharField(max_length = 100)
        email = models.CharField(max_length = 100) 
        password = models.CharField(max_length = 100) 
        objects = UserManager()

