from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogsSerializer,CommentsSerializer
from blog.models import BlogsModel,CommentsModel
from blog.exceptions import IdNotAvailable

class BlogsView(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            qs=BlogsModel.objects.filter(blog_id=id)
            if qs:
                serializer=BlogsSerializer(qs,many=True)
                return Response(serializer.data)
            else:
                raise IdNotAvailable()

    def post(self, request,format=None):
        serializer=BlogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Blog created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        try:
            note=BlogsModel.objects.get(blog_id=pk)
            serializer=BlogsSerializer(note,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Blog updated"})
        except BlogsModel.DoesNotExist:
            raise IdNotAvailable()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        qs=BlogsModel.objects.filter(blog_id=pk).delete()
        if qs[0]==1:
            return Response({"msg":"Blog deleted"})
        raise IdNotAvailable()


class CommentsView(APIView):
    def post(self, request,format=None):
        id=self.request.GET.get('blog_id')
        qs=BlogsModel.objects.filter(blog_id=id)
        if qs:
            serializer=CommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Comment Posted on blog"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            raise IdNotAvailable()
