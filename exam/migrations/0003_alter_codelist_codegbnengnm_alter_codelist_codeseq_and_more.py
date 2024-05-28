# Generated by Django 4.0.3 on 2024-05-28 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_rename_profile_codelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codelist',
            name='codegbnengnm',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='codeseq',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='remark1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='remark2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='remark3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='remark4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='codelist',
            name='upcodecd',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]