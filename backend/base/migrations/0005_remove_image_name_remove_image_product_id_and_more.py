# Generated by Django 4.1.5 on 2023-12-01 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_alter_product_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="name",
        ),
        migrations.RemoveField(
            model_name="image",
            name="product_id",
        ),
        migrations.RemoveField(
            model_name="product",
            name="image_id",
        ),
        migrations.AddField(
            model_name="image",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="base.product",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]