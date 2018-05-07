# Generated by Django 2.0.5 on 2018-05-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_type', models.CharField(choices=[('0', 'OUTGO'), ('1', 'INCOME')], default='0', max_length=1, verbose_name='账目类型')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='账目金额')),
                ('record_date', models.DateField(auto_now=True, verbose_name='记录时间')),
                ('remarks', models.CharField(max_length=140, verbose_name='备注信息')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'bills',
            },
        ),
    ]