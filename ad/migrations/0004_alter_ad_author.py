# Generated by Django 4.1.3 on 2022-11-20 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options'),
        ('ad', '0003_alter_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ad', to='user.user', verbose_name='Автор'),
        ),
    ]
