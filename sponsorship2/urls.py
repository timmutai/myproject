
from django.contrib import admin
from django.urls import include,path

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as auth_view
 

urlpatterns = [
    path('', include('users.urls')),
    path('', include('applications.urls')), 
    path('', include('gallery.urls')),   
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('login/', auth_view.obtain_auth_token),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)