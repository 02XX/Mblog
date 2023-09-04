from datetime import date
from django.db import models


class Tag(models.Model):
    blogTag = models.CharField(max_length=100)
class Category(models.Model):
    blogCategory = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.IntegerField(choices=((0,'男'),(1,'女'),(2,'其他')), verbose_name='性别')
    phone = models.CharField(max_length=11)
    join_date = models.DateField(auto_now_add=True)

    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    brief = models.TextField()
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    content = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    # rating = models.IntegerField(default=5)



class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL,null=True) #文章
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True) # 评论者
    # to = models.IntegerField()
    content = models.TextField()
    commentData = models.DateField()
