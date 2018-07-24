from django.db import models
from django.utils import timezone


class Post(models.Model): 															# Name of class, Post. models.Model means that Post is a Django model and Django will save it to our database.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)				# Author of Post. ForeignKey is a link to another model.
    title = models.CharField(max_length=200)										# Title of Post.
    text = models.TextField()														# Text of Post.
    created_date = models.DateTimeField(											# Date of when post was created.
            default=timezone.now)
    published_date = models.DateTimeField(											# Date of when post was published.
            blank=True, null=True)

    def publish(self):																# Name of method, publish.
        self.published_date = timezone.now()										# Set published date to current date.
        self.save()																	# Save.

    def __str__(self):																# Getter for title.
        return self.title