# Generated by Django 4.2.3 on 2023-08-11 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studypals', '0008_aee_che_csc_cve_eee_fst_mee_msc_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='aeeCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='cheCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='cscCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='cveCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='eeeCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='fstCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='meeCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.CreateModel(
            name='mscCourse',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('studypals.course',),
        ),
        migrations.DeleteModel(
            name='AEE',
        ),
        migrations.DeleteModel(
            name='CHE',
        ),
        migrations.DeleteModel(
            name='CSC',
        ),
        migrations.DeleteModel(
            name='CVE',
        ),
        migrations.DeleteModel(
            name='EEE',
        ),
        migrations.DeleteModel(
            name='FST',
        ),
        migrations.DeleteModel(
            name='MEE',
        ),
        migrations.DeleteModel(
            name='MSC',
        ),
    ]
