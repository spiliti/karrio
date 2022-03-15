# Generated by Django 3.2.11 on 2022-02-27 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import functools
import karrio.server.core.models.base
import karrio.server.core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgs', '0005_auto_20211231_2353'),
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(karrio.server.core.models.base.uuid, *(), **{'prefix': 'app_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=50)),
                ('developer_name', models.CharField(max_length=50)),
                ('is_public', models.BooleanField(default=False)),
                ('is_builtin', models.BooleanField(default=False)),
                ('is_embedded', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=False)),
                ('launch_url', models.CharField(max_length=100)),
                ('features', models.JSONField(blank=True, default=functools.partial(karrio.server.core.utils.identity, *(), **{'value': []}), null=True)),
                ('metadata', models.JSONField(blank=True, default=functools.partial(karrio.server.core.utils.identity, *(), **{'value': {}}), null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'Apps',
                'db_table': 'app',
                'ordering': ['-created_at'],
            },
            bases=(karrio.server.core.models.base.ControlledAccessModel, models.Model),
        ),
        migrations.CreateModel(
            name='AppInstallation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=functools.partial(karrio.server.core.models.base.uuid, *(), **{'prefix': 'ins_'}), editable=False, max_length=50, primary_key=True, serialize=False)),
                ('access_scopes', models.JSONField(blank=True, default=functools.partial(karrio.server.core.utils.identity, *(), **{'value': []}), null=True)),
                ('metadata', models.JSONField(blank=True, default=functools.partial(karrio.server.core.utils.identity, *(), **{'value': {}}), null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='installations', to='apps.app')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'App Installation',
                'verbose_name_plural': 'App Installations',
                'db_table': 'app-installation',
                'ordering': ['-created_at'],
            },
            bases=(karrio.server.core.models.base.ControlledAccessModel, models.Model),
        ),
        migrations.CreateModel(
            name='AppLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='apps.app')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_links', to='orgs.organization')),
            ],
        ),
        migrations.CreateModel(
            name='AppInstallationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='apps.appinstallation')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_installation_links', to='orgs.organization')),
            ],
        ),
        migrations.AddField(
            model_name='appinstallation',
            name='org',
            field=models.ManyToManyField(related_name='installations', through='apps.AppInstallationLink', to='orgs.Organization'),
        ),
        migrations.AddField(
            model_name='app',
            name='org',
            field=models.ManyToManyField(related_name='apps', through='apps.AppLink', to='orgs.Organization'),
        ),
        migrations.AddField(
            model_name='app',
            name='registration',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='app', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
    ]
