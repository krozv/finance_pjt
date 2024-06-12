from django.db import models

# Create your models here.
class DepositProduct(models.Model):
    DENY_CHOICES = [
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한'),
    ]
    fin_prdt_cd = models.CharField(max_length=255, unique=True)
    kor_co_nm = models.CharField(max_length=255)
    fin_prdt_nm = models.CharField(max_length=255)
    etc_note = models.TextField()
    join_deny = models.IntegerField(choices=DENY_CHOICES, default=1)
    join_member = models.TextField(blank=True, null=True)
    join_way = models.TextField(blank=True, null=True)
    spcl_cnd = models.TextField(blank=True, null=True)

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    fin_prdt_cd = models.CharField(max_length=255)
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

class SavingsProduct(models.Model):
    dcls_month = models.CharField(max_length=255)
    fin_co_no = models.CharField(max_length=255)
    fin_prdt_cd = models.CharField(max_length=255, unique=True)
    kor_co_nm = models.CharField(max_length=255)
    fin_prdt_nm = models.CharField(max_length=255)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.CharField(max_length=255)
    join_member = models.CharField(max_length=255)
    etc_note = models.TextField(null=True, blank=True)
    max_limit = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    dcls_strt_day = models.CharField(max_length=8)
    dcls_end_day = models.CharField(max_length=8, null=True, blank=True)
    fin_co_subm_day = models.CharField(max_length=14)

class SavingsOptions(models.Model):
    product = models.ForeignKey(SavingsProduct, related_name='options', on_delete=models.CASCADE)
    dcls_month = models.CharField(max_length=255)
    fin_co_no = models.CharField(max_length=255)
    fin_prdt_cd = models.CharField(max_length=255)
    intr_rate_type = models.CharField(max_length=255)
    intr_rate_type_nm = models.CharField(max_length=255)
    rsrv_type = models.CharField(max_length=255)
    rsrv_type_nm = models.CharField(max_length=255)
    save_trm = models.CharField(max_length=255)
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2)
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2)