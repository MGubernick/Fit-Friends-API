# Generated by Django 3.0 on 2021-02-18 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210217_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='category',
            field=models.CharField(choices=[('Upper Body', 'UB'), ('Lower Body', 'LB'), ('Core', 'C'), ('Cardio', 'GO'), ('Full Body', 'FB'), ('Recovery', 'Re')], max_length=20),
        ),
    ]
