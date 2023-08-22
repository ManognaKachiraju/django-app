# Generated by Django 2.1.5 on 2023-07-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_furniture_complain'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture_complain',
            name='name',
            field=models.CharField(default=34, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='furniture_complain',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
