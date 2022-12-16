from django.core import validators
from django.core.validators import MinLengthValidator

from django.db import models
from django.contrib.auth import models as auth_models

from domfix.core.validators import validate_only_letters


class AppUser(auth_models.AbstractUser):
    MAX_USERNAME_LENGTH = 100

    MIN_AGE_LENGTH = 18

    MAX_PASSWORD_LENGTH = 100

    MIN_FIRST_NAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 30

    MIN_LAST_NAME_LENGTH = 2
    MAX_LAST_NAME_LENGTH = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE_LENGTH),
        ),
        null=True,
        blank=True,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_only_letters,
        ),
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_only_letters,
        ),
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
