# Generated by Django 4.1.4 on 2023-01-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reg_Form', '0002_delete_aero_eng_delete_architecture_eng_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_data',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('College', models.CharField(max_length=20)),
                ('PhoneNo', models.CharField(max_length=10)),
                ('event', models.CharField(max_length=50)),
                ('Txn_id', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
