from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Login_App.models import Profile, User

from Posts_App.models import Post, Like, Album, Photo
from django.views import View

from django.views.generic import DetailView


# Create your views here.
class Home(View):
    def get(self, request):
        user = request.user
        posts = Post.objects.filter(public=True)
        album_list = Album.objects.all
        photos = Photo.objects.all
        return render(request, 'Posts_App/home.html',
                      context={'posts': posts, 'album_list': album_list, 'photos': photos})


@login_required
def addalbum(request):
    user = request.user
    album_list = user.album_set.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['album_new'] != '':
            album, created = Album.objects.get_or_create(
                user=user,
                album_name=data['album_new'])
        else:
            album = None

        for image in images:
            photo = Photo.objects.create(
                album=album,
                a_caption=data['a_caption'],
                image=image,
            )

        return redirect('Login_App:userprofile')

    context = {'album_list': album_list}
    return render(request, 'Posts_App/add_album.html', context)


def albumshow(request):
    user = request.user
    album = request.GET.get('album')
    if album == None:
        photos = Photo.objects.filter(album__user=user)
    else:
        photos = Photo.objects.filter(
            album__album_name=album, album__user=user)
    album_list = Album.objects.filter(user=user)

    context = {'album_list': album_list, 'photos': photos}
    return render(request, 'Posts_App/album_home.html', context)


@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))


@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
