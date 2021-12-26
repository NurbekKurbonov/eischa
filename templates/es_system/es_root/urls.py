
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('startingpage.urls')),
    path('firstadmin', include('startingpage.urls')),
    path('secondadmin/', include('secondadmin.urls')),
    path('enterprises', include('enterprises.urls')),
    path('ges/', include('ges.urls')),
    path('authentication/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
