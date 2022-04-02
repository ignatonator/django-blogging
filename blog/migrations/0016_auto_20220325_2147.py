# Generated by Django 3.2.6 on 2022-03-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment_name of constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='comment',
            name='name of constraint',
        ),
        migrations.AddConstraint(
            model_name='comment',
            constraint=models.UniqueConstraint(fields=('body', 'email'), name='body and email'),
        ),
    ]
