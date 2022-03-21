from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post
# Create your tests here.

class TestPost(TestCase):

    @classmethod
    def setUp(cls):
        user1 = User.objects.create_user(
                    username='john', password='abc12345'
                )
        user1.save()

        test_post = Post.objects.create(
                author = user1,
                title = 'Hello World',
                body = 'This is my first post'
            )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEquals(author, 'john')
        self.assertEquals(title, 'Hello World')
        self.assertEquals(body, 'This is my first post')
        

