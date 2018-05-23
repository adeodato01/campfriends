from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^[a-zA-Z\d]{8,}$")
NAME_REGEX = re.compile(r"^[a-zA-Z\D]{2,}$")


class UserManager(models.Manager):
    def ValidateTheUser(self, postData):
        result = {
            'status': False,
            'errors': []
        }
        if len(postData['first_name']) < 1:
            result['errors'].append("Your name is required")
        elif not NAME_REGEX.match(postData['first_name']):
            result['errors'].append("Your name must be more than 2 letters")
        if len(postData['last_name']) < 1:
            result['errors'].append("Your name is required")
        elif not NAME_REGEX.match(postData['last_name']):
            result['errors'].append("Your name must be more than 2 letters")
        if len(postData['password1']) < 1:
            result['errors'].append("Password is required")
        elif not PASSWORD_REGEX.match(postData['password1']):
            result['errors'].append("Password must contain a number, a letter, and be at least 8 characters")
        if len(postData['password2']) < 1:
            result['errors'].append("Password confirmation is required")
        elif postData['password2'] != postData['password1']:
            result['errors'].append("Passwords must match")
        if len(result['errors']) == 0:
            result['status'] = True
            result['user_id'] = User.objects.create(
                first_name = postData['first_name'],
                last_name=postData['last_name'],
                email = postData['email'],
                password = bcrypt.hashpw(postData['password1'].encode(), bcrypt.gensalt())
            ).id

        return result

    def ValidateLogin(self, postData):
        result = {
            'status': False,
            'errors': []
        }
        existing_users = User.objects.filter(email__iexact=postData['email'])
        if len(existing_users) == 0:
            result['errors'].append("Invalid email & password combination")
        else:
            if bcrypt.checkpw(postData['password3'].encode(), existing_users[0].password.encode()):
                result['status'] = True
                result['user_id'] = existing_users[0].id
            else:
                result['errors'].append("Invalid email & password combination")
        return result


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __repr__(self):
        return "<User object: name:{} username:{} id:{}>".format(self.name, self.username, self.id)
