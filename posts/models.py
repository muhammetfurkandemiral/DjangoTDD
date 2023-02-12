from operator import mod
from statistics import mode
from turtle import title
from urllib import response
from django.db import models
from django.test import TestCase

# Create your models here.
"""
    class Post
        id:int
        title:varchar
        body:text
        created_at:datetime
        modified_at:datetime
"""


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
