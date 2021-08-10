from django.conf.urls import url
from django.urls import path
from .views.signup_view import Sign_up
from .views.login_view import Login_user, edit_profile, logout_user, userprofile

app_name = "Login_App"

urlpatterns = [
    path('signup/', Sign_up.as_view(), name='signup'),
    path('login/', Login_user.as_view(), name='login'),
    path('edit/', edit_profile, name='edit'),
    path('logout/', logout_user, name='logout'),
    path('profile/', userprofile, name='userprofile'),

]
