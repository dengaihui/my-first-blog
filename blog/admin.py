from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)

'''
如你所见，我们导入（包括）了前一章定义的Post模型。 为了让我们的模型在admin页面上可见，
我们需要使用 admin.site.register(Post) 来注册模型.
OK, 现在来看看我们的 Post 模型。 记得先在控制台输入 python manage.py runserver 
启动服务器。 然后打开浏览器，输入地址 http://127.0.0.1:8000/admin/ 你会看到登录界面像这样:
'''
