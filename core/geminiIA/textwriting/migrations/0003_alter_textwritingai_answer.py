# Generated by Django 5.1.3 on 2024-11-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textwriting', '0002_alter_textwritingai_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textwritingai',
            name='answer',
            field=models.CharField(max_length=100000),
        ),
    ]