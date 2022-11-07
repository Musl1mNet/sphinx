# Generated by Django 4.1.3 on 2022-11-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['birthday'], name='table_user_birthda_dff966_idx'),
        ),
    ]