# Generated by Django 4.2.7 on 2023-11-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('E', 'Economic'), ('S', 'Science'), ('IT', 'IT')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
