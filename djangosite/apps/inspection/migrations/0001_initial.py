# Generated by Django 3.0.5 on 2020-04-13 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specification', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspector', models.CharField(blank=True, max_length=20)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspection_task', to='project.Task')),
            ],
        ),
        migrations.CreateModel(
            name='InspectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='Name')),
                ('doc', models.FileField(blank=True, upload_to='', verbose_name='document')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='image')),
                ('check_result', models.CharField(choices=[('PASS', 'Pass'), ('FAIL', 'Fail'), ('EMPTY', 'Empty')], default='EMPTY', max_length=5)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='inspection.Inspection')),
                ('spec_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spec_item', to='specification.SepcItem')),
            ],
        ),
    ]
