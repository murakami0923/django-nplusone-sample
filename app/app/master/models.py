from django.db import models


class District(models.Model):
    name = models.CharField(max_length=255)
    sequence = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
 
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'master_district'
        verbose_name = '地方マスタ'
        verbose_name_plural = verbose_name


class Prefecture(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    name = models.CharField('都道府県名', max_length=255)
    sequence = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'master_prefecture'
        verbose_name = '都道府県マスタ'
        verbose_name_plural = verbose_name


class Sex(models.Model):
    name = models.CharField('性別名', max_length=16)
    sequence = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'master_sex'
        verbose_name = '性別マスタ'
        verbose_name_plural = verbose_name
