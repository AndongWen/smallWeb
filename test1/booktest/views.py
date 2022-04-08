from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    """本质就是django.shortcuts中的render"""
    # 使用模板文件
    # 1.加载模板文件，返回一个模板对象
    temp = loader.get_template("booktest/index.html")
    # 2.定义模板上下文，向模板文件传递数据
    # 3.渲染模板，产生标准的html文件
    res_html = temp.render({"content": "I want money", "list": [1,4,5,78,8,3,9]})  # 参数为字典
    # 4.返回给浏览器
    return HttpResponse(res_html)