# Generated by Django 3.2.6 on 2022-03-25 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_comment_body'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='comment',
            name='body and email',
        ),
    ]
