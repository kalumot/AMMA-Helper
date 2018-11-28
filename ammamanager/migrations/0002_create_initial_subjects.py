# Generated by Django 2.0.1 on 2018-01-18 18:07

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('ammamanager', 'Subject')
    Subject.objects.create(name='Safe MMA', color='#343a40')




class Migration(migrations.Migration):

    dependencies = [
        ('ammamanager', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
