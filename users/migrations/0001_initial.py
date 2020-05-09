# Generated by Django 2.2.10 on 2020-05-09 10:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                (
                    'mobile',
                    models.CharField(
                        max_length=16, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Enter a valid mobile number', regex='^(\\+\\d{1,3}[- ]?)?\\d{10}$')]
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        max_length=300,
                        unique=True,
                        validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be alphanumeric or contain numbers', regex='^[a-zA-Z0-9.+-]*$')],
                    ),
                ),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('firstName', models.CharField(max_length=20, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=20, verbose_name='Last Name')),
                ('dateJoined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={'abstract': False,},
        ),
        migrations.CreateModel(
            name='SavedPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ManyToManyField(to='posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.TextField()),
                ('year', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')], default='1', max_length=1)),
                (
                    'branch',
                    models.CharField(
                        choices=[
                            ('COE', 'Computer Engineering'),
                            ('CSE', 'Computer Science Engineering'),
                            ('ECE', 'Electroincs and Communications Engineering'),
                            ('ENC', 'Electroincs and Computer Engineering'),
                            ('COBS', 'Computer Science and Business Studies'),
                            ('CE', 'Chemical Engineering'),
                            ('CiE', 'Civil Engineering'),
                            ('BiE', 'Biotechnology'),
                            ('BME', 'Biomedical Engineering'),
                            ('SE', 'Structural Engineering'),
                            ('IE', 'Infrastructure Engineering'),
                            ('ME', 'Mechanical Engineering'),
                            ('MEC', 'Mechatronics Engineering'),
                            ('EE', 'Electrical Engineering'),
                            ('ECE', 'Electroinc (Instrumentation and Control)'),
                            ('ME(P)', 'Mechanical (Production) Engineering'),
                            ('BE-MBA(ME)', 'Mechanical MBA Dual Degree'),
                            ('BE-MBA(ECE)', 'Electroincs MBA Dual Degree'),
                            ('Others', 'Other'),
                        ],
                        max_length=11,
                    ),
                ),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
