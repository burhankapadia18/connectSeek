# Generated by Django 3.2.8 on 2021-12-01 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_assignment_details_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=1)),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=1000000)),
                ('payment_mode', models.CharField(choices=[('UPI', 'UPI'), ('DD', 'Demand Draft'), ('Cash', 'Cash')], max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student_table')),
            ],
        ),
    ]
