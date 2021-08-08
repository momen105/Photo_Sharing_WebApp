from django.db import models
from Login_App.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date', ]


class Album(models.Model):
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Album_list'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    album_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.album_name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='album_pic', blank=True)
    a_caption = models.TextField(max_length=264, blank=True)

    def __str__(self):
        return self.a_caption


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)