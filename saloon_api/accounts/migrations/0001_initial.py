# Generated by Django 2.1.1 on 2018-10-15 05:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, default='images/None/No-image.png', null=True, upload_to='images/')),
                ('contact_number', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', regex='^\\+?\\d{9,15}$')])),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user_type', models.CharField(blank=True, choices=[('o', 'Owner'), ('c', 'Customer'), ('e', 'Employee')], default='c', help_text='User Role', max_length=1)),
                ('saloon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Saloon')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
