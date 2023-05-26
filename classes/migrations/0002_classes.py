# Generated by Django 4.2 on 2023-05-26 09:13

import classes.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('difficulty_level', models.CharField(max_length=50)),
                ('max_number_of_lessons', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('active', models.BooleanField(default=True)),
                ('price_for_lesson', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stationary', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, validators=[classes.validators.validate_teacher_role])),
                ('type_of_classes_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='classes.typeofclasses')),
            ],
        ),
    ]
