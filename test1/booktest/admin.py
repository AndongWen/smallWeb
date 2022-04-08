from django.contrib import admin
from booktest.models import BookInfo, PersonInfo


# 后台管理相关文件
# Register your models here.
# 可以自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']


class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hcomment', 'hgender', 'hbook_id']


# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(PersonInfo, PersonInfoAdmin)
