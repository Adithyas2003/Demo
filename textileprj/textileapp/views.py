from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

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
    if 'shop' in req.session:
        return render(req,'shop/home.html')
    else:
        return redirect(e_shop_login)
