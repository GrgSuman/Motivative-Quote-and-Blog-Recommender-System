# Generated by Django 3.2.9 on 2021-11-17 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='QuotesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default='')),
                ('img', models.ImageField(default='defaultCategory.png', upload_to='uploads/category')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriberEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('subscriptionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=400)),
                ('slug', models.SlugField(default='')),
                ('backgroundImage', models.ImageField(default='defaultBG.png', upload_to='static/images')),
                ('keywords', models.CharField(default='', max_length=400)),
                ('metaDesc', models.CharField(default='', max_length=400)),
                ('author', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('postStatus', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quotescategory', to='quotesandblogs.quotescategory')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(default='')),
                ('featuredImage', models.ImageField(default='defaultBG.png', upload_to='static/images')),
                ('keywords', models.CharField(default='', max_length=400)),
                ('metaDesc', models.CharField(default='', max_length=400)),
                ('body', tinymce.models.HTMLField(blank=True, null=True)),
                ('createdAt', models.DateField(null=True)),
                ('postStatus', models.BooleanField(default=False)),
                ('claps', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('mainCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='quotesandblogs.blogscategory')),
                ('relatedCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quotesandblogs.blogscategory')),
            ],
        ),
    ]