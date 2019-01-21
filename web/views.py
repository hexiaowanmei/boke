import random

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.urls import reverse

from blok.models import Article
from web.models import BokeUser, BokeToken


def index(request):
    if request.method == 'GET':
        article = Article.objects.all()

        for art in article:
            print(art)
        return render(request, 'web/index.html', {'article': article})


def about(request):
    return render(request, 'web/about.html')


def gbook(request):
    return render(request, 'web/gbook.html')


def info(request):
    return render(request, 'web/info.html')


def life(request):
    return render(request, 'web/life.html')


def list(request):
    return render(request, 'web/list.html')


def share(request):
    return render(request, 'web/share.html')


def time(request):
    return render(request, 'web/time.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'web/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = BokeUser.objects.filter(username=username).first()
        if check_password(password, user.password):
            res = HttpResponseRedirect(reverse('web:indexee'))
            s = '34234j23432j4j234234232342erer'
            token = ''
            for i in range(20):
                token += random.choice(s)
            res.set_cookie('token', token, max_age=400)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            msg = '账户或密码错误'
            return render(request, 'web/login.html', {'msg': msg})


def register(request):
    if request.method == 'GET':
        return render(request, 'web/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if BokeUser.objects.filter(username=username).exists():
            msg = '用户名已存在'
            render(request, 'web/register.html', {'msg': msg})
        if password != password2:
            msg = '密码不一致'
            render(request, 'web/register.html', {'msg': msg})

        password = make_password(password)
        BokeUser.objects.create(username=username, password=password)
        return HttpResponseRedirect(reverse('web:login'))


def indexee(request):
    if request.method == 'GET':
        # 从cookies中获取登录校验的token值
        token = request.COOKIES.get('token')
        # 判断token是否存在。如果不存在说明没有登录或登录失败
        if not token:
            return HttpResponseRedirect(reverse('web:login'))
        User_token = BokeToken.objects.filter(token=token)
        if not User_token:
            # if token != '123456789':
            return HttpResponseRedirect(reverse('web:login'))
        return render(request, 'index.html')