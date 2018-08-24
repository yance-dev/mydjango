from django.shortcuts import render, HttpResponse
from app01.models import *

# Create your views here.
def add(request):
    # 方式1:
    # publish_obj = Publish.objects.get(nid=1)
    # book_obj = Book.objects.create(title="金瓶眉", publishDate="2012-12-12", price=100, publish=publish_obj)


    # 方式2:

    book_obj = Book.objects.create(title="金瓶眉", publishDate="2012-12-12", price=100, publish_id=1)
    # 当前生成的书籍对象
    # book_obj = Book.objects.create(title="追风筝的人", price=200, publishDate="2012-11-12", publish_id=1)
    # 为书籍绑定的做作者对象
    # tom = Author.objects.filter(name="tom").first()  # 在Author表中主键为2的纪录
    # mark = Author.objects.filter(name="mark").first()  # 在Author表中主键为1的纪录
    #
    # # 绑定多对多关系,即向关系表book_authors中添加纪录
    # book_obj.authors.add(mark ,tom)  # 将某些特定的 model 对象添加到被关联对象集合中。   =======    book_obj.authors.add(*[])

    return HttpResponse("OK")
