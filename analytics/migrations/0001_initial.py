# Generated by Django 2.2.12 on 2021-12-27 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=255, verbose_name='Site Name')),
                ('url', models.URLField(help_text='URL must be with or without scheme (http/https)', verbose_name='Site URL')),
                ('is_verified', models.BooleanField(default=False)),
                ('track_id', models.CharField(max_length=50, unique=True, verbose_name='Track ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'url')},
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(blank=True, max_length=64, null=True, verbose_name='IP Address')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='First Visited')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Visited')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('keyword', models.CharField(help_text='Must be unique in same domain', max_length=50)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Client')),
            ],
            options={
                'unique_together': {('host', 'keyword')},
            },
        ),
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('visit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='analytics.Visit')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Client')),
            ],
            options={
                'verbose_name': 'Website Visit Count',
                'verbose_name_plural': 'Website Visit Counts',
            },
            bases=('analytics.visit',),
        ),
        migrations.CreateModel(
            name='PageVisit',
            fields=[
                ('visit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='analytics.Visit')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.Page')),
            ],
            options={
                'verbose_name': 'Page Visit Count',
                'verbose_name_plural': 'Page Visit Counts',
            },
            bases=('analytics.visit',),
        ),
    ]
