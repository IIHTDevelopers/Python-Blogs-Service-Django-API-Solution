from django.contrib import admin
from blog.models import BlogsModel,CommentsModel

class BlogsModelAdmin(admin.ModelAdmin):
    list_display=['blog_id','title','content']

class CommentsModelAdmin(admin.ModelAdmin):
    list_display=['comment_id','blog_id','comment']

admin.site.register(BlogsModel,BlogsModelAdmin)
admin.site.register(CommentsModel,CommentsModelAdmin)
