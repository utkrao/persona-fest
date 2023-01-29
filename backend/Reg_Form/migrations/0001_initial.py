# Generated by Django 4.1.4 on 2023-01-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aero_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Architecture_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bio_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Civil_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cse_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ece_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FoodAndTechnology',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ISBJ',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mech_Eng',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School_of_Education_and_Research',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SFT',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SOFA',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('selection', models.BooleanField(default=False)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('College', models.CharField(max_length=20)),
                ('PhoneNo', models.CharField(max_length=10)),
                ('event', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vedic_Science',
            fields=[
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
                ('selection', models.BooleanField(default=False)),
                ('event_name', models.CharField(max_length=50)),
                ('Registration_name', models.CharField(max_length=50)),
            ],
        ),
    ]
