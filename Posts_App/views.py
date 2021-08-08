from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Login_App.models import Profile, User

from Posts_App.models import Post, Like, Album, Photo

# Create your views here.

@login_required
def home(request):
    posts = Post.objects.all
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)
    print(liked_post_list)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Profile.objects.filter(username__icontains=search)
    return render(request, 'Posts_App/home.html', context={'title':'Home', 'search':search, 'result':result, 'posts':posts, 'liked_post_list':liked_post_list})

@login_required
def gallery(request):
    user = request.user
    album = request.GET.get('album')
    if album == None:
        photos = Photo.objects.filter(album__user=user)
    else:
        photos = Photo.objects.filter(
            album__album_name=album, album__user=user)

    album_list = Album.objects.filter(user=user)
    context = {'album_list': album_list, 'photos': photos}
    return render(request, 'Posts_App/gallery.html', context)

@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'Posts_App/view_photo.html', {'photo': photo})

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

        return redirect('Posts_App:gallery')

    context = {'album_list': album_list}
    return render(request, 'Posts_App/add_album.html', context)



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