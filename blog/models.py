from django.db import models

class BlogsModel(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=200)

class CommentsModel(models.Model):
    comment_id = models.AutoField(primary_key=True)
    blog_id = models.IntegerField()
    comment=models.CharField(max_length=200)
