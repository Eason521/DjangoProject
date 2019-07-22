from django.shortcuts import render, HttpResponseRedirect,redirect
from LoginApp import models
from django.http import JsonResponse
import hashlib


# Create your views here.
def direct(fun):#装饰器
    def inner(request,*args,**kwargs):
        username = request.COOKIES.get("username")
        if username:
            return fun(request,*args,**kwargs)
        else:
            return redirect("/login/")
    return inner


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = models.User.objects.filter(username=username).first()
        if user and password:
            pass_hax = hus(password)
            if user.password== pass_hax :
                request.COOKIES["username"] = username
                return render(request,'loginapp/index.html',locals())
    return render(request,"loginapp/login.html",locals())


def quits(request):
    res = HttpResponseRedirect('/login/')
    res.delete_cookie("username")
    return res


def register(request):
    dic = {"status":"error","content":""}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        q_password = request.POST.get("q_password")
        email = request.POST.get("email")
        if username:
            if password:
                user = models.User.objects.filter(username=username).first()
                if user:
                    dic["content"] = "用户已存在"
                    return render(request, 'loginapp/register.html', locals())
                else:
                    if q_password == password:
                        models.User.objects.create(
                            username = username,
                            password = hus(password),
                            email= email
                        )
                        return HttpResponseRedirect("/login/")
                    else:
                        dic["content"] = "两次密码不一致"
            else:
                dic["content"] = "密码不能为空"
        else:
            dic["content"] = "用户名不能为空"
    return render(request, 'loginapp/register.html',locals())

def nameValid(request):
    result = {"status":"error","data":""}
    if request.method == "GET" and request.GET:
        username = request.GET.get("username")
        if username:
            name = models.User.objects.filter(username=username).first()
            if name:
                result["data"] = "用户已存在"
            else:
                result["status"] = "success"
                result["data"] = "可以使用的用户名"
        else:
            result["data"] = "用户名不能为空"
        return JsonResponse(result)
def passwordValid(request):
    result = {"status":"error","data":""}
    if request.method == "GET" and request.GET:
        q_password = request.GET.get("q_password")
        if q_password:
            password = request.GET.get("password")
            if q_password == password:
                result["status"] = "success"
                result["data"] = "密码匹配成功"
            else:
                result["data"] = "两次密码不相同"
        else:
            result["data"] = "请输入确认密码"
        return JsonResponse(result)





@direct
def index(request):
    return render(request,"loginapp/login.html",locals())


def hus(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

