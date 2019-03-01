# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sohye_blog.users import models as user_models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 모델이 추가되었을 때 최초 한번 기록
    updated_at = models.DateTimeField(auto_now=True) # 모델이 업데이트될 때마다 기록

    class Meta:
        abstract = True


class Image(TimeStampedModel):
    """ Image Model """
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT, related_name='images') # 이미지를 올린 유저

    # toString.
    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']


class Comment(TimeStampedModel):
    """ Comment Model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT) # 댓글 작성 유저
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='comments') # 어떤 사진에 댓글이 달린건지.

    def __str__(self):
        return self.message


class Like(TimeStampedModel):
    """ Like Model """
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)

