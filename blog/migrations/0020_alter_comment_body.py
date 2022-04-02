# Generated by Django 3.2.6 on 2022-03-25 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(error_messages={'unique': 'This email has already been registered.'}, max_length=3500),
        ),
    ]
