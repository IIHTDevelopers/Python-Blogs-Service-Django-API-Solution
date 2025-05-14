from rest_framework.test import APITestCase
from blog.models import BlogsModel,CommentsModel
from blog.test.TestUtils import TestUtils
class BlogAppAPIFunctionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        BlogsModel.objects.create(blog_id=101,title="Python",content="Python is an easy programming language")
        CommentsModel.objects.create(comment_id=1,blog_id=101,comment="It is easy")

    def test_get_request_for_blog(self):
        url='http://127.0.0.1:8000/blog_pk/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForBlog", True, "functional")
            print("TestGetRequestForBlog = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForBlog", False, "functional")
            print("TestGetRequestForBlog = Failed")

    def test_post_request_for_blog(self):
        url='http://127.0.0.1:8000/blog/'
        data={
            #"blog_id": 1,
            "title": "Blog2",
            "content": "This is blog2"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequestForBlog", True, "functional")
            print("TestPostRequestForBlog = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForBlog", False, "functional")
            print("TestPostRequestForBlog = Failed")


    def test_patch_request_for_blog(self):
        url='http://127.0.0.1:8000/blog_pk/101/'
        data={
                "blog_id": 102,
                "content": "This is the Blog2"
            }
        response=self.client.patch(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestPatchRequestForBlog", True, "functional")
            print("TestPatchRequestForBlog = Passed")
        else:
            test_obj.yakshaAssert("TestPatchRequestForBlog", False, "functional")
            print("TestPatchRequestForBlog = Failed")

    def test_delete_request(self):
        url='http://127.0.0.1:8000/blog_pk/101/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteRequestForBlog", True, "functional")
            print("TestDeleteRequestForBlog = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequestForBlog", False, "functional")
            print("TestDeleteRequestForBlog = Failed")

    def test_post_request_for_comment(self):
        url='http://127.0.0.1:8000/comment/?blog_id=101'
        data={
            "blog_id": 101,
            "comment": "It is good"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequestForComment", True, "functional")
            print("TestPostRequestForComment = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForComment", False, "functional")
            print("TestPostRequestForComment = Failed")
