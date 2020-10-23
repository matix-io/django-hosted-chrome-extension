# Generated by Django 3.1.2 on 2020-10-23 22:54

from django.db import migrations, models
import hosted_chrome_extension.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChromeExtensionVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='chrome-extension/')),
                ('version', models.CharField(max_length=10, unique=True, validators=[hosted_chrome_extension.models.validate_version])),
            ],
        ),
    ]
