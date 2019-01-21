from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse

# from blok.forms import ArtForm
from blok.models import Article
from web.models import BokeUser


def login(request):
    if request.method == 'GET':
        return render(request, 'backstage/login.html',)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = BokeUser.objects.filter(username=username).first()
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('blok:index'))
        else:
            msg = '账号或密码错误!'
            return render(request, 'login.html', {'msg': msg})


def register(request):
    if request.method == 'GET':
        return render(request, 'backstage/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if BokeUser.objects.filter(username=username).exists():
            msg = '用户名已存在'
            render(request, 'backstage/register.html', {'msg': msg})
        if password != password2:
            msg = '密码不一致'
            render(request, 'backstage/register.html', {'msg': msg})

        password = make_password(password)
        BokeUser.objects.create(username=username, password=password)
        return HttpResponseRedirect(reverse('blok:login'))


def index(request):
    if request.method == 'GET':
        return render(request, 'backstage/index.html')


def article(request):
    if request.method == "GET":
        page = int(request.GET.get('page', 1))
        article = Article.objects.all()

        pg = Paginator(article, 5)
        article = pg.page(page)
        return render(request, 'backstage/article.html', {'article': article})
    if request.method == 'POST':
        pass


def add_article(request):
    if request.method == 'GET':
        return render(request, 'backstage/add_article.html')
    if request.method == 'POST':
        imgs = request.FILES.get('imgs')
        title = request.POST.get('title')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')
        content = request.POST.get('content')
        tags = request.POST.get('tags')
        Article.objects.create(title=title, keyword=keywords, describe=describe,
                               img=imgs, content=content, label=tags)
        return HttpResponseRedirect(reverse('blok:article'))
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            imgs = form.cleaned_data['imgs']
            keywords = form.cleaned_data['keywords']
            content = form.cleaned_data['content']
            describe = form.cleaned_data['describe']
            label = form.cleaned_data['label']
            Article.objects.create(title=title, img=imgs, keyword=keywords,
                                   content=content, describe=describe, label=label)
            return HttpResponseRedirect(reverse('blok:article'))
        else:
            errors = form.errors
            return render(request, 'backstage/add_article.html', {'errors': errors})


def show_all(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        article = Article.objects.all()

        pg = Paginator(article, 1)
        article = pg.page(page)
        return render(request, 'backstage/article.html', {'article': article})


def edit_article(request):
    """
    文章编辑方法
    """
    if request.method == 'GET':
        return render(request, 'edit.html')
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 使用all()方法进行判断，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        if not all([title, content]):
            msg = '请填写完整的参数'
            return render(request, 'edit.html', {'msg': msg})
        # 创建文章
        Article.objects.create(title=title,
                               content=content)
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('users:article'))


def del_art(request, id):
    if request.method == 'GET':
        Article.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('blok:article'))


def category(request):
    if request.method == 'GET':
        return render(request, 'backstage/category.html')
    if request.method == 'POST':
        pass

