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