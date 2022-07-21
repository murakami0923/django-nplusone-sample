from django.db import models

from app.master.models import Prefecture, Sex


class Person(models.Model):
    name = models.CharField('氏名', max_length=128)
    name_kana = models.CharField('氏名（カタカナ）', max_length=128)
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT)
    telephone = models.CharField('電話番号', max_length=128)
    telephone_mobile = models.CharField('携帯電話', max_length=128)
    mail_address = models.CharField('メールアドレス', max_length=255)
    zip_code = models.CharField('郵便番号', max_length=32)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.PROTECT)
    address1 = models.CharField('住所1', max_length=255)
    address2 = models.CharField('住所1', max_length=255)
    birthday = models.DateField('生年月日')
    
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
 
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'person'
        verbose_name = '個人'
        verbose_name_plural = verbose_name
