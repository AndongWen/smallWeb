from django.db import models


# Create your models here.

# 图书类
class BookInfo(models.Model):
    '''选项 unique 这个字段在表中必须有唯一值
            db_index 表中会为此字段创建索引
            db_column 字段的名称，如果没有指定，则使用属性的名称
            null 允许为空（数据库管理的范畴）
            blank 允许为空白（与后台管理有关）'''
    btitle = models.CharField(max_length=24, db_column='title')
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)  # 软删除的标记 mysql不做真正的删除

    def __str__(self):
        return self.btitle


# 人物类
class PersonInfo(models.Model):
    hname = models.CharField(max_length=12)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=120, null=True, blank=True)
    # 关系属性对应表的字段名格式： 关系属性_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)  # 关系属性 与图书之间的关系是一对多  多类中定义关系属性
    isDelete = models.BooleanField(default=False)  # 软删除的标记 mysql不做真正的删除

    def __str__(self):
        return self.hname
