"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from blok import views

from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static

# from utils.upload_image import upload_image

 # kindeditor编辑器上传图片地址
from boke import settings
from utils.upload_image.upload_images import upload_image

re_path(r'^util/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),

# 配置media访问路径

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web/', include(('web.urls', 'web'), namespace='web')),
    path('blok/', include(('blok.urls', 'blok'), namespace='blok')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
