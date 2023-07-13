from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.IntegerField()

    def __str__(self):
        return self.content
