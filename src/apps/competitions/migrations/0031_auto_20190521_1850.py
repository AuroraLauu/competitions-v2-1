# Generated by Django 2.1.2 on 2019-05-21 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0030_submissiondetails_is_scoring'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phase',
            options={'ordering': ('index',)},
        ),
        migrations.RemoveField(
            model_name='phase',
            name='ingestion_program',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='input_data',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='is_task_and_solution',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='public_data',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='reference_data',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='scoring_program',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='solutions',
        ),
        migrations.RemoveField(
            model_name='phase',
            name='starting_kit',
        ),
    ]