# Generated by Django 3.1 on 2020-09-06 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coverLetters', '0022_auto_20200906_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='choice_of_user',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='coverLetters.userdetail'),
        ),
    ]
