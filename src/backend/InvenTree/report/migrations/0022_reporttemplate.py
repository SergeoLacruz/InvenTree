# Generated by Django 4.2.11 on 2024-04-21 03:11

import InvenTree.models
import django.core.validators
from django.db import migrations, models
import report.helpers
import report.models
import report.validators


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0021_auto_20231009_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata', models.JSONField(blank=True, help_text='JSON metadata field, for use by external plugins', null=True, verbose_name='Plugin Metadata')),
                ('name', models.CharField(help_text='Template name', max_length=100, verbose_name='Name')),
                ('template', models.FileField(help_text='Template file', upload_to='report/report', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html', 'htm'])], verbose_name='Template')),
                ('description', models.CharField(help_text='Template description', max_length=250, verbose_name='Description')),
                ('revision', models.PositiveIntegerField(default=1, editable=False, help_text='Revision number (auto-increments)', verbose_name='Revision')),
                ('page_size', models.CharField(default=report.helpers.report_page_size_default, help_text='Page size for PDF reports', max_length=20, verbose_name='Page Size')),
                ('landscape', models.BooleanField(default=False, help_text='Render report in landscape orientation', verbose_name='Landscape')),
                ('filename_pattern', models.CharField(default='output.pdf', help_text='Pattern for generating filenames', max_length=100, verbose_name='Filename Pattern')),
                ('enabled', models.BooleanField(default=True, help_text='Template is enabled', verbose_name='Enabled')),
                ('model_type', models.CharField(max_length=100, help_text='Target model type for template', validators=[report.validators.validate_report_model_type])),
                ('filters', models.CharField(blank=True, help_text='Template query filters (comma-separated list of key=value pairs)', max_length=250, validators=[report.validators.validate_filters], verbose_name='Filters')),
            ],
            options={
                'abstract': False,
                'unique_together': [('name', 'model_type')]
            },
            bases=(InvenTree.models.PluginValidationMixin, models.Model),
        ),
    ]
