from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from Login_App.forms import EditProfile
from Login_App.models import Profile, User
from Posts_App.forms import PostForm

# Authetication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
# Messages
from django.views import View

# Create your views here.
class Login_user(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'Login_App/login.html',context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('Posts_App:home'))
        return render(request, 'Login_App/login.html', context={'title': 'Login . Social', 'form': form})


@login_required
def edit_profile(request):
    current_user = Profile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_App:userprofile'))
    return render(request, 'Login_App/profile.html', context={'form':form, 'title':'Edit Profile . Social'})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:login'))

@login_required
def userprofile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Login_App/user.html', context={'title': 'User', 'form': form})
