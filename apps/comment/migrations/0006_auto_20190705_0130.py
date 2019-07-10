# Generated by Django 2.1 on 2019-07-05 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_auto_20190703_2352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='内容类型'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
    ]