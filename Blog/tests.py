from django.test import TestCase
from Blog.models import Post

# Create your tests here.

class PostTests(TestCase):

    def test_str(self):
        title = Post(title="this is a title")
        self.assertEquals(
        str(title), "this is a title"
        )
