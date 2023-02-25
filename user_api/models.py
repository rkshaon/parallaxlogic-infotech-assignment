from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from django.conf import settings
import os



def use_directory_path(instance, filename):
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name




class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, image=None, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            image=image
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=use_directory_path, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# class User(AbstractUser):
#     """User Model"""
#     name = models.CharField(max_length=255)
#     picture = models.ImageField(upload_to=use_directory_path, blank=True, null=True, verbose_name='Picture')
#     email = models.CharField(max_length=255, blank=True, null=True, default=None)
#     password = models.CharField(max_length=255)