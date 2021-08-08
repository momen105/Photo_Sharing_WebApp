from django.contrib import admin
from Posts_App.models import Post, Like, Album, Photo

# Register your models here.

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Album)
admin.site.register(Photo)