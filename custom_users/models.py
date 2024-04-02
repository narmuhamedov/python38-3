from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    phone_number = models.CharField(max_length=20, default='+996')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=(('M', 'Male'),
                                                       ('F', 'Female'))
                              )
