from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from booktest.models import BookInfo, PersonInfo
import datetime

"""1.<a href="/create">新增</a> 
   2.<a href="create">新增</a> 两者得区别
   1.相当于前面省略了http:127.0.0.1
   2.相当于在当前的页面加上现有的路由"""


# Create your views here.
def index(request):
    """本质就是django.shortcuts中的render"""
    # 使用模板文件
    # 1.加载模板文件，返回一个模板对象
    temp = loader.get_template("booktest/index.html")
    # 2.定义模板上下文，向模板文件传递数据
    # 3.渲染模板，产生标准的html文件
    res_html = temp.render({"content": "I want money", "list": [1, 4, 5, 78, 8, 3, 9]})  # 参数为字典
    # 4.返回给浏览器
    return HttpResponse(res_html)


def show_books(request):
    # 通过Models查找图书中的数据
    books = BookInfo.objects.all()
    # 使用模板
    return render(request, "booktest/show_books.html", {'books': books})


def books_detail(request, bid):
    book = BookInfo.objects.get(id=bid)
    heroes = book.personinfo_set.all()
    return render(request, "booktest/books_detail.html", {'book': book, 'heroes': heroes})


def create(request):
    b = BookInfo()
    b.btitle = "流星蝴蝶剑"
    b.bpub_date = datetime.date(1995, 11, 3)
    b.save()
    # 返回应答，让浏览器再次访问books页面，又称重定向 服务器不返回页面，而是让浏览器再去请求其他得url地址
    return HttpResponseRedirect("/books")


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    # 返回应答，让浏览器再次访问books页面，又称重定向 服务器不返回页面，而是让浏览器再去请求其他得url地址
    return redirect("/books")
