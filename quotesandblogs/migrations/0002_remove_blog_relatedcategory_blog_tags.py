# Generated by Django 4.0.1 on 2022-01-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesandblogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='relatedCategory',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='quotesandblogs.BlogsCategory'),
        ),
    ]
