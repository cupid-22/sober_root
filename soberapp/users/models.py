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
        if social_id is None:
            raise ValueError("Social Id is required for application users")
        if social_type is None:
            raise ValueError("Social type is required for application users")

        user = self.model(social_id=social_id, social_type=social_type, **extra_fields)
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
    class SocialLoginOption(models.TextChoices):
        FACEBOOK = 'fb', _('Facebook Login')
        GOOGLE = 'google', _('Google Login')
        APPLE = 'apple', _('Apple Login')
        ADMIN = 'admin', _('Admin Login')

    username = None
    email = models.EmailField(unique=True, null=True, blank=False)

    profile = models.ImageField(null=True, blank=True, upload_to="admin/")
    social_id = models.CharField(null=False, blank=False, unique=True, max_length=SOCIAL_ID_LENGTH, db_index=True)
    social_type = models.CharField(null=False, blank=False, choices=SocialLoginOption.choices, max_length=6)
    sobriety_date = models.DateField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        unique_together = ('social_id', 'social_type',)
        db_table = 'users'

    objects = UserManager()

    def __str__(self):
        return f"<{self.social_id}:{self.social_type}>"
