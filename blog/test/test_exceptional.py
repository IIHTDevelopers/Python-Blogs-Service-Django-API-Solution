from rest_framework.test import APITestCase
from blog.models import BlogsModel,CommentsModel
from blog.test.TestUtils import TestUtils
class BlogAppAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        BlogsModel.objects.create(blog_id=101,title="Python",content="Python is an easy programming language")
        CommentsModel.objects.create(comment_id=1,blog_id=101,comment="It is easy")

    def test_blog_id_not_available_error_at_get_request(self):
        url='http://127.0.0.1:8000/blog_pk/102111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtGetRequest", True, "exception")
            print("TestBlogIdNotAvailableErrorAtGetRequest = Passed")
        else:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtGetRequest", False, "exception")
            print("TestBlogIdNotAvailableErrorAtGetRequest = Failed")

    def test_blog_id_not_available_error_at_patch_request(self):
        url='http://127.0.0.1:8000/blog_pk/11234/'
        response=self.client.patch(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtPatchRequest", True, "exception")
            print("TestBlogIdNotAvailableErrorAtPatchRequest = Passed")
        else:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtPatchRequest", False, "exception")
            print("TestBlogIdNotAvailableErrorAtPatchRequest = Failed")

    def test_blog_id_not_available_error_at_delete_request(self):
        url='http://127.0.0.1:8000/blog_pk/11234/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtDeleteRequest", True, "exception")
            print("TestBlogIdNotAvailableErrorAtDeleteRequest = Passed")
        else:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtDeleteRequest", False, "exception")
            print("TestBlogIdNotAvailableErrorAtDeleteRequest = Failed")

    def test_post_request_for_blog_with_invaild_data(self):
        url='http://127.0.0.1:8000/blog/'
        data={
            #"blog_id": 1,
            #"title": "Blog2",
            "content": "This is blog2"
        }
        response=self.client.post(url,data,format='json')
        test_obj = TestUtils()
        if response.status_code==400:
            test_obj.yakshaAssert("TestPostRequestForBlogWithInvaildData", True, "exception")
            print("TestPostRequestForBlogWithInvaildData = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestForBlogWithInvaildData", False, "exception")
            print("TestPostRequestForBlogWithInvaildData = Failed")

    def test_blog_id_not_available_error_at_post_comment(self):
        url='http://127.0.0.1:8000/comment/?blog_id=1111'
        response=self.client.post(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestBlogIdNotAvailableErrorAtPostComment", True, "exception")
            print("TestBlogIdNotAvailableErrorAtPostComment = Passed")
        else:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtPostComment", False, "exception")
            print("TestBlogIdNotAvailableErrorAtPostComment = Failed")
