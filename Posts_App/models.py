from django.db import models
from Login_App.models import User
from django.utils import timezone


# Create your models here.

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(
            PostManager,
            self).filter(draft=False).filter(publish__lte=timezone.now())

    def public_post(self, *args, **kwargs):
        return super(
            PostManager,
            self).filter(public=True)

    def private_post(self, *args, **kwargs):
        return super(
            PostManager,
            self).filter(public=False)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=True)

    objects = PostManager()

    @property
    def is_public(self):
        return self.public

    @property
    def is_private(self):
        return self.private

    class Meta:
        ordering = ['-upload_date', ]


class Album(models.Model):
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Album_list'
        ordering = ['-upload_date', ]

    album_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='album_aut')
    album_name = models.CharField(max_length=100, null=False, blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.album_name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
        ordering = ['-upload_date', ]

    photo_aut = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='photo_aut')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='album_pic', blank=True)
    a_caption = models.TextField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.a_caption


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)
