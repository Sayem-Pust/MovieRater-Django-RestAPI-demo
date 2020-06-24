from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'auth/', obtain_auth_token),
]
