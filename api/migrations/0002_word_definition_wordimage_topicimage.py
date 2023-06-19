# Generated by Django 4.2.2 on 2023-06-18 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='definition',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.CreateModel(
            name='WordImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=128, unique=True)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.word')),
            ],
        ),
        migrations.CreateModel(
            name='TopicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=128, unique=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.topic')),
            ],
        ),
    ]
