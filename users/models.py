from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True)
    phone_number = PhoneNumberField(default="", blank=False)
    volunteer_portal_ID = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(default="", blank=True) 