# Generated by Django 3.2.3 on 2021-06-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_alter_producto_nombreproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='numdoc',
            field=models.CharField(default=12, max_length=20),
            preserve_default=False,
        ),
    ]
