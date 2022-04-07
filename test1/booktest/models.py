from django.db import models


# Create your models here.

# 图书类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=24)
    bpub_date = models.DateField()

    def __str__(self):
        return self.btitle


# 人物类
class PersonInfo(models.Model):
    hname = models.CharField(max_length=12)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=120)
    # 关系属性对应表的字段名格式： 关系属性_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)  # 关系属性 与图书之间的关系是一对多  多类中定义关系属性

    def __str__(self):
        return self.btitle
