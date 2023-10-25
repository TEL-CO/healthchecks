# Generated by Django 3.0.8 on 2020-07-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_subscription_invoice_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='next_billing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='renew_notice_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]