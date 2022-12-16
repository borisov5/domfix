from enum import Enum

from django.core import validators
from django.db import models

from domfix.core.model_mixins import ChoicesEnumMixin


class Category(ChoicesEnumMixin, Enum):
    DRY_CONSTRUCTION_PRODUCT = 'Сухо строителство'
    THERMAL_INSULATION_PRODUCT = 'Топлоизолация'
    WATER_SUPPLY_AND_SANITATION_PRODUCT = 'Водопровод и канализация'
    CONSTRUCTION_CHEMISTRY_PRODUCT = 'Строителна химия'
    TOOLS_PRODUCT = 'Инструменти'
    PAINTING_PRODUCTS = 'Бояджииство'


class Product(models.Model):
    MAX_NAME_LENGTH = 50

    MAX_DESCRIPTION_LENGTH = 300

    MAX_ITEM_CODE_LENGTH = 30

    MAX_MANUFACTURER_LENGTH = 30

    MIN_AVAILABILITY_LENGTH = 0

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    category = models.CharField(
        choices=Category.choices(),
        max_length=Category.max_len(),
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
    )

    availability = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AVAILABILITY_LENGTH),
        )
    )

    item_code = models.CharField(
        max_length=MAX_ITEM_CODE_LENGTH,
        unique=True,
        null=True,
        blank=True,
    )

    price = models.FloatField(
        null=True,
        blank=True,
    )

    photo = models.URLField(
        null=True,
        blank=True,
    )

    manufacturer = models.CharField(
        max_length=MAX_MANUFACTURER_LENGTH,
        null=True,
        blank=True,
    )
