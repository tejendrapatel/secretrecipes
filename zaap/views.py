from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zaap.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse, request
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, message
from secret_recipe.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
import json

def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['usr']
        p = d['pass']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('admin_index')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)

def LOGOUT(request):
    logout(request)
    return redirect('home')

def HOME(request):
    if request.method == "POST":
        c = request.POST
        cname = c['nam']
        cdate = c['dat']
        ctime = c['tim']
        cmobile = c['mob']
        cperson = c['per']
        Book_Table.objects.create(name=cname,date=cdate,mobile=cmobile,time=ctime,persons=cperson)
    cakes = Menu.objects.filter(menu_choice="cakes").order_by('-id')
    chines = Menu.objects.filter(menu_choice="chinese").order_by('-id')
    indians = Menu.objects.filter(menu_choice="indian").order_by('-id')
    italia = Menu.objects.filter(menu_choice="italian").order_by('-id')
    cake = cakes[:6]
    chinese = chines[:6]
    indian = indians[:6]
    italian = italia[:6]
    tes = testimony.objects.all()
    d = {"tes":tes,"cake":cake,"chinese":chinese,"indian":indian,"italian":italian}
    return render(request, 'index.html',d)

def MENU(request):
    if request.method == "POST":
        c = request.POST
        cname = c['nam']
        cdate = c['dat']
        ctime = c['tim']
        cmobile = c['mob']
        cperson = c['per']
        Book_Table.objects.create(name=cname,date=cdate,mobile=cmobile,time=ctime,persons=cperson)
    cake = Menu.objects.filter(menu_choice="cakes").order_by('-id')
    chinese = Menu.objects.filter(menu_choice="chinese").order_by('-id')
    indian = Menu.objects.filter(menu_choice="indian").order_by('-id')
    italian = Menu.objects.filter(menu_choice="italian").order_by('-id')
    tes = testimony.objects.all()
    d = {"tes":tes,"cake":cake,"chinese":chinese,"indian":indian,"italian":italian}
    return render(request, 'menu.html',d)

def ABOUT(request):
    if request.method == "POST":
        c = request.POST
        cname = c['nam']
        cdate = c['dat']
        ctime = c['tim']
        cmobile = c['mob']
        cperson = c['per']
        Book_Table.objects.create(name=cname,date=cdate,mobile=cmobile,time=ctime,persons=cperson)
    cake = Menu.objects.filter(menu_choice="cakes").order_by('-id')
    chinese = Menu.objects.filter(menu_choice="chinese").order_by('-id')
    indian = Menu.objects.filter(menu_choice="indian").order_by('-id')
    italian = Menu.objects.filter(menu_choice="italian").order_by('-id')
    tes = testimony.objects.all()
    d = {"tes":tes,"cake":cake,"chinese":chinese,"indian":indian,"italian":italian}
    return render(request, 'about.html',d)

def BOOK_TABLE(request):
    if request.method == "POST":
        c = request.POST
        cname = c['nam']
        cdate = c['dat']
        ctime = c['tim']
        cmobile = c['mob']
        cperson = c['per']
        Book_Table.objects.create(name=cname,date=cdate,mobile=cmobile,time=ctime,persons=cperson)
    cake = Menu.objects.filter(menu_choice="cakes").order_by('-id')
    chinese = Menu.objects.filter(menu_choice="chinese").order_by('-id')
    indian = Menu.objects.filter(menu_choice="indian").order_by('-id')
    italian = Menu.objects.filter(menu_choice="italian").order_by('-id')
    tes = testimony.objects.all()
    d = {"tes":tes,"cake":cake,"chinese":chinese,"indian":indian,"italian":italian}
    return render(request, 'book_table.html',d)


###########      admin pannel        ########

def ADMIN_YOUTUBE(request):
 
    return render(request, 'admin_youtube.html')


def ADMIN_INDEX(request):
    men = Menu.objects.all()
    if request.method == "POST":
        mmen = request.POST['men']
        iimg = request.FILES['img']
        nnam = request.POST['nam']
        ppri = request.POST['pri']
        dell = request.POST['det']
        Menu.objects.create(menu_choice=mmen,image=iimg,detail=dell,price=ppri,name=nnam)
    d = {"men":men}
    return render(request, 'admin_index.html',d)

def MENU_DELETE(request,del_id):
    Menu.objects.get(id=del_id).delete()
    return redirect('admin_index')