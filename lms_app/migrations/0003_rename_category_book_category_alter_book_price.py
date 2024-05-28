# Generated by Django 4.2.11 on 2024-05-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0002_alter_book_category_alter_book_relat_price_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]