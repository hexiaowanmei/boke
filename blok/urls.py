from django.contrib import admin
from django.urls import path, include

from blok import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('article/', views.article, name='article'),
    path('add_article/', views.add_article, name='add_article'),
    path('show_all/', views.show_all, name='show_all'),
    # 编辑文章
    path('edit_article/', views.edit_article, name='edit_article'),
    # 文章列表
    path('article/', views.article, name='article'),
    path('del_art/<int:id>', views.del_art, name='del_art'),
    path('category/', views.category, name='category'),
]