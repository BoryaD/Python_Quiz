# Generated by Django 3.0.2 on 2020-02-26 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quize_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quize',
            name='quize_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quize',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('quize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize_app.Quize')),
            ],
        ),
    ]
