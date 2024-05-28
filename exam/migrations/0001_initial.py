# Generated by Django 4.0.3 on 2024-05-28 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codegbncd', models.CharField(max_length=20)),
                ('codegbnnm', models.CharField(max_length=20)),
                ('codegbnengnm', models.CharField(max_length=20)),
                ('codegrpcd', models.CharField(max_length=20)),
                ('upcodecd', models.CharField(max_length=20)),
                ('remark1', models.CharField(max_length=20)),
                ('remark2', models.CharField(max_length=20)),
                ('remark3', models.CharField(max_length=20)),
                ('remark4', models.CharField(max_length=20)),
                ('codeseq', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '공통코드',
                'verbose_name_plural': '공통코드',
                'ordering': ['-codegbncd'],
            },
        ),
    ]
