
from django.contrib import admin
from django.urls import include,path

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views as auth_view

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Sponsorship API",
      default_version='v1',
      description="Test description",
     
   ),
   public=True,

)
 

urlpatterns = [
    path('', include('users.urls')),
    path('', include('applications.urls')), 
    path('', include('gallery.urls')),   
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)