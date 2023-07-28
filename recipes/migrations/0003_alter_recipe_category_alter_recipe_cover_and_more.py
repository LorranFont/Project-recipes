# Generated by Django 4.2.1 on 2023-07-28 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_recipeo_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
