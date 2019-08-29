# Generated by Django 2.1.7 on 2019-08-28 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_id', models.PositiveIntegerField()),
                ('sanitary_inspector_name', models.CharField(max_length=50)),
                ('sanitary_inspector_phone', models.PositiveIntegerField()),
                ('sanitary_inspector_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward_id', models.PositiveIntegerField()),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wards', to='location.Cluster')),
            ],
        ),
        migrations.AddField(
            model_name='locality',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localities', to='location.Ward'),
        ),
    ]
