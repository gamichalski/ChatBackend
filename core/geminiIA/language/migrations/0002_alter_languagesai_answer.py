# Generated by Django 5.1.3 on 2024-11-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagesai',
            name='answer',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]
