from rest_framework.serializers import ModelSerializer
from blog.models import BlogsModel,CommentsModel
class BlogsSerializer(ModelSerializer):
    class Meta:
        model=BlogsModel
        fields='__all__'

class CommentsSerializer(ModelSerializer):
    class Meta:
        model=CommentsModel
        fields='__all__'
