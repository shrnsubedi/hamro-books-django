# Generated by Django 3.0.1 on 2020-06-24 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_condition',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Fine', 'Fine'), ('Torn', 'Torn')], default='Used', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('None', 'None'), ('Fiction', 'Fiction'), ('Non-fiction', 'Non-fiction'), ('Biography', 'Biography'), ('Other', 'Other')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(),
        ),
    ]
