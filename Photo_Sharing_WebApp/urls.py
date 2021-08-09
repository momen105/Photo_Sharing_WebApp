from django.contrib import admin
from django.urls import path , include

# To show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from Posts_App import views
from Posts_App.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login_App.urls')),
    path('post/', include('Posts_App.urls')),
    path('', Home.as_view(), name = 'home'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)