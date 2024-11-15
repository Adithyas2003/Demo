from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *

def e_shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['shop']=uname
            return redirect(shop_home)
        else:
            messages.warning(req, "invalid password")
            return redirect(e_shop_login)
    else:
        return render(req,'login.html')
	
def e_shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(e_shop_login)

def shop_home(req):
    data=Product.objects.all()
    if 'shop' in req.session:
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(e_shop_login)


def add_product(req):
    if 'shop' in req.session:
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            descrip=req.POST['descrip']
            price=req.POST['price']
            o_price=req.POST['off_price']
            stock=req.POST['stock']
            file=req.FILES['img']
            data=Product.objects.create(pid=pid,name=name,dis=descrip,price=price,offer_price=o_price,stock=stock,img=file)

            data.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/addproduct.html')
    else:
        return redirect(e_shop_login)