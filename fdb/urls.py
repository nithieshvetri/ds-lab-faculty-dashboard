"""fdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.conf.urls.static import static

from .views import MyTokenObtainPairView
from django.views.static import serve

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings


urlpatterns = [
    # path('', RedirectView.as_view(url='home/', permanent=False)),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')), # home url for user urls
    path('api/faculty/', include('faculty.urls')), # home url for faculty urls
    path('',TemplateView.as_view(template_name='index.html')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('login/',TemplateView.as_view(template_name='index.html'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

