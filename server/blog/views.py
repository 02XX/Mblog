
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin
from .models import Blog,Tag,Category,Comment
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from server.markdown2HTML import markdownToHTML 
from rest_framework.response import Response
# Create your views here.
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields="__all__"

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields="__all__"

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields="__all__"


class BlogSerializer(ModelSerializer):
    tag = TagSerializer(many=True)
    category = CategorySerializer(many=True)
    comment = SerializerMethodField()
    class Meta:
        model = Blog
        fields="__all__"
    def get_comment(self,obj):
        comments = Comment.objects.filter(blog=obj)
        return CommentSerializer(comments, many=True).data
    # def to_representation(self, instance): #将model的数据展示
    #     representation = super().to_representation(instance=instance)
    #     content = instance.content
    #     representation['content'] = markdownToHTML(content)
    #     return representation
    # def to_internal_value(self, data): #将data转为model的数据
    #     return super().to_internal_value(data)


class blog(GenericViewSet ,DestroyModelMixin, CreateModelMixin, UpdateModelMixin,RetrieveModelMixin):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        print(page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

