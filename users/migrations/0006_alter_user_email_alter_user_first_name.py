# Generated by Django 4.2 on 2023-04-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Użytkownik o podanym adresie e-mail już istnieje.'}, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
