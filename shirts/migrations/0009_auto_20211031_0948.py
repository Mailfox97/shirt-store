# Generated by Django 3.1.3 on 2021-10-31 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shirts', '0008_auto_20211031_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shirts.category'),
        ),
    ]
