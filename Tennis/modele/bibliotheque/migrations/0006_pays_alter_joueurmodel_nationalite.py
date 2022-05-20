# Generated by Django 4.0.4 on 2022-05-19 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0005_alter_joueurmodel_nationalite_delete_pays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationalite', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='joueurmodel',
            name='Nationalite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.pays'),
        ),
    ]
