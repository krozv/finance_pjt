# Generated by Django 5.0.6 on 2024-06-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0002_savingsproduct_savingsoptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingsoptions',
            name='dcls_month',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='fin_co_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='fin_prdt_cd',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='intr_rate_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='intr_rate_type_nm',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='rsrv_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='rsrv_type_nm',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsoptions',
            name='save_trm',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='dcls_month',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='fin_co_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='fin_prdt_cd',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='fin_prdt_nm',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='join_deny',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='join_member',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='savingsproduct',
            name='kor_co_nm',
            field=models.CharField(max_length=255),
        ),
    ]
