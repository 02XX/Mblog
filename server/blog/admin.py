from django.contrib import admin
from .models import User, Blog, Tag, Category, Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
