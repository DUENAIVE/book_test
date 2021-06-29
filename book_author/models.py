
from django.db import models


class Author(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    class Meta:
        db_table = 'tb_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    Name = models.CharField(max_length=20, verbose_name='名称')
    Gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    Born_Date = models.DateField(verbose_name='出生日期')

class Book(models.Model):
    Author = models.ForeignKey('Author', on_delete=models.CASCADE,null=True,default='')
    BookName = models.CharField(max_length=20, verbose_name='名称1',default='')
    Publish_Date = models.DateField(verbose_name='出版时间')
    Country = models.IntegerField(default=0, verbose_name='国家')
    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称
