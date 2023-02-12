import imp
from turtle import title
from urllib import response
from django.test import TestCase
from .models import Post
from http import HTTPStatus


class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_objects(self):
        post = Post.objects.create(title="Test Post", body="Test Body")

        self.assertEqual(str(post), post.title)


class HomepageTest(TestCase):
    def setUp(self) -> None:
        post1 = Post.objects.create(
            title="Sample post 1",
            body="There are many variations of passages of Lorem Ipsum available",
        )
        post2 = Post.objects.create(
            title="Sample post 2",
            body="There are many variations of passages of Lorem Ipsum available",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, "Sample post 1")
        self.assertContains(response, "Sample post 2")

class DetailPageTest(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(
        title = "Learn Javascript in this 23 hour course",
        body = "This is a beginner course on JS"
    )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')
    
    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertNotContains(response, self.post.create_at)
