from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo, PersonInfo


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
