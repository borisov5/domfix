# Generated by Django 4.1.4 on 2022-12-16 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('DRY_CONSTRUCTION_PRODUCT', 'Сухо строителство'), ('THERMAL_INSULATION_PRODUCT', 'Топлоизолация'), ('WATER_SUPPLY_AND_SANITATION_PRODUCT', 'Водопровод и канализация'), ('CONSTRUCTION_CHEMISTRY_PRODUCT', 'Строителна химия'), ('TOOLS_PRODUCT', 'Инструменти'), ('PAINTING_PRODUCTS', 'Бояджииство')], max_length=35)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('availability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('item_code', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('photo', models.URLField(blank=True, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]