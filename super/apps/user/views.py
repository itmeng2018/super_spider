import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.user.models import User
from utils.VerifyCode import get_captcha


# /news/user/register/
class RegisterView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pwd = request.POST.get('confirm_pwd')
        phone = request.POST.get('phone')

        if not all([username, email, password, confirm_pwd, phone]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'login.html', {'errmsg': '邮箱格式不正确'})

        if password != confirm_pwd:
            return render(request, 'login.html', {'errmsg': '两次密码不一致'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'login.html', {'errmsg': '用户名已存在'})

        # 创建用户
        User.objects.create_user(username, email, password, phone=phone, is_active=0)
        return redirect(reverse('user:login'))


# /user/ver/
class VerRefreshView(View):
    def get(self, request):
        captcha = get_captcha()
        request.session['ver_code'] = captcha
        return JsonResponse({'ver_code': captcha})


# /news/user/login/
class LoginView(View):
    def get(self, request):
        captcha = get_captcha()
        request.session['ver_code'] = captcha
        # print(captcha)
        return render(request, 'login.html')

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        ver_code = request.POST.get('ver_code')



        # 参数
        if not all([username, password, ver_code]):
            print('参数不完整')
            return render(request, 'login.html', {'errmsg': '参数不完整'})

        # 验证码
        if not re.match(request.session.get('ver_code'), ver_code, re.I):
            return render(request, 'login.html', {'errmsg': '验证码错误'})

        # TODO Django auth不能验证, 未知原因, 手动查询数据库检测
        # user = authenticate(request, username=username, password=password)
        # print('views.login: ', user)

        try:
            # 查询数据库
            user = User.objects.get(username=username)
            if not check_password(password, user.password):
                return render(request, 'login.html', {'errmsg': '用户名或密码错误'})
        except User.DoesNotExist:
            user = None

        if user is None:
            return render(request, 'login.html', {'errmsg': '用户不存在'})

        # 激活状态 TODO 测试状态不检测
        # if not user.is_active:
        #     return render(request, 'login.html', {'errmsg': '账户未激活'})

        # 记录用户的登录状态
        login(request, user)      # TODO Django auth不能验证, 未知原因, 手动保存到session
        # request.session['user_id'] = user.id
        # request.session['is_login'] = True
        # 获取用户登录后要跳转到的地址
        next_url = request.GET.get('next', reverse('console:visualization'))
        # 返回response
        return redirect(next_url)

