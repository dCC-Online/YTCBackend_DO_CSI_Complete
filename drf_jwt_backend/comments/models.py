from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    video_id = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, on_delete=models.DO_NOTHING, related_name='replies')
    text = models.CharField(max_length=200)