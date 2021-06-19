from django.db import models

# Create your models here.
from django.utils import timezone

# 这行是用来定义我们的模型 (这是一个 对象 ).
# models.Model 表明Post是一个Django模型，所以Django知道它应该被保存在数据库中。
'''
现在我们定义了我们曾经提及到的那些属性： title , text , created_date , published_date 和 author 。 
为了做到那样我们需要为我们每个字段定义一个类型(它是文本吗？ 是数字？ 是日期？ 到另一个对象的关联，比如用户吗?）。

models.CharField - 这是你如何用为数有限的字符来定义一个文本。
models.TextField - 这是没有长度限制的长文本。这听起来用在博客文章的内容上挺适合的，对吧？
models.DateTimeField - 这是日期和时间。
models.ForeignKey - 这是指向另一个模型的连接。
我们不会对这里的代码解释得面面俱到因为那会花太多时间了。 如果你想了解更多有关模型字段以及如何定义除上面描述以外的东西，
那你应该去看看Django的官方文档( https://docs.djangoproject.com/zh-hans/2.2/ref/models/fields/ )。
'''


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
