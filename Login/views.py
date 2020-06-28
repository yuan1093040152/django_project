from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
import time


def login(request):
    rep =  render(request,'Login/login.html')
    # is_login = request.COOKIES.get('is_login')
    # print(is_login)
    # is_register = request.COOKIES.get('is_register')
    # print(is_register)
    # if not (is_login == None):
    #     rep.delete_cookie("is_login")
    #
    # else:
    #     if not (is_register == None):
    #         rep.delete_cookie("is_register")
    #         return rep
    #
    #     return rep
    return rep



def successful(request):
    return render(request, 'Login/successful.html')



def login_successful(request):
    # return render(request, 'Login/login_successful.html')

    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if status == None:
        return render(request, 'Login/login.html')

    return  render(request, 'Login/login_successful.html')




#注册
def register(request):
    create_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    # print (create_time)
    # if request.method == 'POST':
    username = request.POST.get('username','USERNAME')
    password = request.POST.get('password','PASSWORD')
    problem = request.POST.get('problem','PROBLEM')
    answer = request.POST.get('answer','ANSWER')
    # info = models.emp_login.objects.raw("INSERT INTO emp_login(username,password,problem,answer,creat_time) VALUES ('%s','%s','%s','%s','%s');" % (username,password,problem,answer,create_time))
    info = models.emp_login.objects.create(username=username, password=password, problem=problem, answer=answer,creat_time=create_time)
    print(info)
    # return render(request, 'Login/successful.html')
    #获取cookie
    status = request.COOKIES.get('is_register')

    if status == None:

        # 注册成功记录cookie
        rep = render(request, 'Login/successful.html')
        rep.set_cookie('is_register', '234')
        return rep

    else:
        return render(request, 'Login/login.html')










def login_info(request):
     #if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.emp_login.objects.filter(username=username, password=password).first()
        print (user_obj)

        #若登录失败
        if user_obj == None :

            # 获取cookie
             status = request.COOKIES.get('is_login')

            #没有cookie信息返回登录页面
             if status == None:
                 return render(request,'Login/login.html')

             # 有cookie信息返回登录成功页面
             else:
                return render(request, 'Login/login_successful.html')

        # 若登录成功
        else:
            #登录成功记录cookie
            rep = render(request,'Login/login_successful.html')
            rep.set_cookie('is_login', '123')
            return rep




    # def index(request):
    #     print(request.COOKIES.get('is_login'))
    #     status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    #     if not status:
    #         return redirect('/login/')
    #     return render(request, "index.html")


#注销
def logout(request):
    rep =  render(request,'Login/login.html')
    keys = request.COOKIES.keys()
    for is_login in keys:

        rep.delete_cookie(is_login)

    bb = request.COOKIES.get('is_login')
    print(bb)
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面


#去登录
def go_login(request):
    rep =  render(request,'Login/login.html')
    rep.delete_cookie('is_register')
    return rep # 点击去登陆后执行,删除cookie,不再保存用户状态，并弹到登录页面
