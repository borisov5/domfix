from django.db import models


class Partner(models.Model):

    MAX_NAME_LENGTH = 30

    MAX_DESCRIPTION_LENGTH = 300

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )

    photo = models.URLField(
        null=True,
        blank=True,
    )
