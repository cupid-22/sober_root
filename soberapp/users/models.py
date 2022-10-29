from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.managers import InheritanceManager

from common.models import CoreModel
from soberapp.settings import SOCIAL_ID_LENGTH


class UserManager(InheritanceManager, BaseUserManager):
    use_in_migrations = True

    def create_user(self, social_id, social_type, **extra_fields):
        """Create and save a regular User with the given email and password."""
        if extra_fields.get('social_id') is None:
            raise ValueError("Social Id is required for application users")
        extra_fields.setdefault('social_id', social_id)

        if extra_fields.get('social_type') is None:
            raise ValueError("Social type is required for application users")
        extra_fields.setdefault('social_type', social_type)

        user = self.model(**extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save an Admin User with the given email and password."""
        if password is None:
            raise ValueError("Password is required for admin users")
        if email is None:
            raise ValueError("Email is required for admin users")
        normalised_email = self.normalize_email(email)

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(email=normalised_email, social_id=f"{datetime.utcnow().strftime('%Y%m%d%H')}_default_social",
                          social_type=User.SocialLoginOption.ADMIN, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(CoreModel, AbstractUser, PermissionsMixin):
    class SocialLoginOption(models.IntegerChoices):
        FACEBOOK = 1, _('Facebook Login')
        GOOGLE = 2, _('Google Login')
        APPLE = 3, _('Apple Login')
        ADMIN = 4, _('Admin Login')

    username = None
    email = models.EmailField(unique=True, null=True, blank=False)

    profile = models.ImageField(null=True, blank=True, upload_to="admin/")
    social_id = models.CharField(null=False, blank=False, unique=True, max_length=SOCIAL_ID_LENGTH, db_index=True)
    social_type = models.IntegerField(null=False, blank=False, choices=SocialLoginOption.choices)
    sobriety_date = models.DateField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        unique_together = ('social_id', 'social_type',)
        db_table = 'users'

    objects = UserManager()

    def __str__(self):
        return f"<{self.social_id}:{self.social_type}>"
