from django.shortcuts import render
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse 
# Create your views here.
def singup(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            try:
               a=Userlogin.objects.get(username=name)
               if(a.username==name):
                   form=Loginform()
                   error='error'
                   return render(request,'signup.html',{'error':error,'form':form})
            except ObjectDoesNotExist:
                form.save()
    else:
        form = Loginform()
    return render(request, 'signup.html', {'form': form})

from django.contrib.auth.hashers import make_password, check_password

# # Rename login view to avoid conflict with built-in login function
# def user_login(request):
#     if request.method == 'POST':
#         form = log_in(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             try:
#                 user = Login.objects.get(username=name)
#                 if check_password(password, user.password):
#                     return render(request, 'web.html', {'log': '1', 'name': user})
#                 else:
#                     form = log_in()
#                     error = 'Invalid password'
#                     return render(request, 'login.html', {'error': error, 'form': form})
#             except Login.DoesNotExist:
#                 form = log_in()
#                 error = 'User does not exist'
#                 return render(request, 'login.html', {'error': error, 'form': form})
#         else:
#             form = log_in()
#             # Handle form validation errors
#             return render(request, 'login.html', {'form': form})

#     else:
#         form = log_in()
#     return render(request, 'login.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
               a=Userlogin.objects.get(username=name)
               if(a.password==password):
                 return render(request,'web.html',{'log':'1','name':a})
               else:
                form = Loginform()
                error='error'
                return render(request,'login.html',{'error':error,'form':form})
            except ObjectDoesNotExist:
                form = Loginform()
                error='error'
                return render(request,'login.html',{'error':error,'form':form}) 
        else:
            form = Loginform()
            error='error'
            return render(request,'login.html',{'error1':error,'form':form}) 
                
    else:
        form = Loginform()
    return render(request, 'login.html', {'form': form})
import json  #reservation
from collections import Counter
def my_view1(request,name):
    tab=[]
    for i in range(1,100):
        tab.append(i)  
    if request.method == 'POST':
        array = request.POST.get('dataArray')
        date=request.POST.get('date')
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().time().strftime("%H:%M")
        current_datetime=current_date+"T"+current_time
        if(date<current_datetime):
            ub = booking.objects.filter(username=name)
            a= booking.objects.values_list('num', flat=True)
            return render(request,'res.html',{'forms':a,'tab':tab,'b':ub,'username':name,'error':'error'})
        data_list = json.loads(array)
        data=[]
        m= data_list
        value_counts = Counter(m)
        for value, count in value_counts.items():
           if count%2==1:
               data.append(value)
           else:
              continue
        for i in data:
           if booking.objects.filter(num=i).exists():
            #    errors='error'
            #    a1= booking.objects.values_list('num', flat=True)
            #    return render(request,'res.html',{'forms':a1,'tab':tab,'error':errors,'name':name})
            continue
           else:
                booking.objects.create(username=name,num=i,date=date)
        ub = booking.objects.filter(username=name)
        a= booking.objects.values_list('num', flat=True)
        return render(request,'res.html',{'forms':a,'tab':tab,'b':ub,'username':name})
    else:
        ub = booking.objects.filter(username=name)
        a= booking.objects.values_list('num', flat=True)
        return render(request,'res.html',{'forms':a,'tab':tab,'b':ub,'username':name})
def home(request):
    return render(request,'web.html',{'log':'0'})
import json
from django.http import JsonResponse
def menu(request,name):
    tab=[]
    tab1=[]
    menu_num=[]
    title=[]
    title2=[]
    
    title1=['appetizer','salads','main courses','sandwiches and wraps','vegetarian/vegan options','side Dishes','desserts','beverages','kids menu','specials']
    
    for i in title1:
       
        q=Menu.objects.filter(item_type=i)
        
        for l in q:
            tab1.append(int(l.num))
            tab.append(int(l.num))
            title2.append(l.item_type)
        if tab1 and title2:
            title.append(title2[0])
            menu_num.append(tab1[0])
            title2=[]
            tab1=[]
   
    title_num={}
    k=0
    for i in menu_num:
        title_num[i]=title[k] 
        k=k+1
   
    if request.method == 'POST':      
        array1=request.POST.get('Array')
        count1=request.POST.get('count')
        array = json.loads(array1)
        count = json.loads(count1)
        
        j=0
        for i in array:
            i=int(i)
            a=Menu.objects.get(num=str(i))
            if (count[j]==0):
                j=j+1
                continue
            else:
                Order.objects.create(username=name,items=a.items,price=a.price,count=int(count[j]))
                j=j+1
        price=Menu.objects.values_list('price', flat=True)
        items= Menu.objects.values_list('items', flat=True)
        num= Menu.objects.values_list('num', flat=True)
        image = [menu.image.url for menu in Menu.objects.all()]
        b={}
        a={}
        images={}
        u=0
        for i in num:
            b[int(i)]=price[u]
            a[int(i)]=items[u]
            images[int(i)]=image[u]
            u=u+1
        return render(request,'menu1.html',{'tab':tab,'forms':a,'price':b,'title':title,'menu':menu_num,'title_num':title_num,'images':images,'username':name})
    else:
        price=Menu.objects.values_list('price', flat=True)
        items= Menu.objects.values_list('items', flat=True)
        num= Menu.objects.values_list('num', flat=True)
        image = [menu.image.url for menu in Menu.objects.all()]
        b={}
        a={}
        images={}
        u=0
        for i in num:
            b[int(i)]=price[u]
            a[int(i)]=items[u]
            images[int(i)]=image[u]
            u=u+1
        return render(request,'menu1.html',{'tab':tab,'forms':a,'price':b,'title':title,'menu':menu_num,'title_num':title_num,'images':images,'username':name})
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def admin(request):
    if request.method=='POST':
        form=admin_menu(request.POST,request.FILES)
        if form.is_valid():
            names=['appetizer','salads','main courses','sandwiches and wraps','vegetarian/vegan options','side Dishes','desserts','beverages','kids menu','specials']
            items=form.cleaned_data['item_type']
            # num=form.cleaned_data['num']     #fields=["items","price","item_type","image"]
            # price=form.cleaned_data['price']
            # item_type=form.cleaned_data['item_type']
            # image=form.cleaned_data['image']
            # return HttpResponse(request,names)
            if(items in names):
                # Menu.objects.create()
                form.save()
                a=admin_menu()
                num= Menu.objects.values_list('num', flat=True)
                
                if num:
                    length = int(num.last())
                    return render(request,'admin_menu.html',{'form':a,'length':length+1})
                else:
                    length=0
                    return render(request,'admin_menu.html',{'form':a,'length':length+1})
            else:
               
                 error='error'
                 num= Menu.objects.values_list('num', flat=True)
                 
                 if num:
                    length = int(num.last())
                    return render(request,'admin_menu.html',{'form':a,'length':length+1})
                 else:
                    length=0
                    return render(request,'admin_menu.html',{'form':a,'length':length+1})    
           
        return HttpResponse("error")
    else:
        a=admin_menu()     
        num= Menu.objects.values_list('num', flat=True)
        if num:
            length = int(num.last())
            return render(request,'admin_menu.html',{'form':a,'length':length+1})
        else:
            length=0
            return render(request,'admin_menu.html',{'form':a,'length':length+1})
        #   names=Menu.objects.values_list('item_type',flat=True)
        #   return JsonResponse({'menu_num': names})
    
# def newmenu(request):
#     title1=['appetizer','salads','main courses','sandwiches and wraps','vegetarian/vegan options','side Dishes','desserts','beverages','kids menu','specials']
#     d={}
#     for i in title1:
#         d[i]=Menu.objects.filter(item_type=i)

#     items=Menu.objects.all()
#     return render(request,"mymenu.html",{"items":title1,"d":d})

# def trail(request):
#     tab=[1]
#     image = [menu.image.url for menu in Menu.objects.all()]
#     images={}
#     u=0
#     num= Menu.objects.values_list('num', flat=True)
    
#     for i in num:
       
#         images[int(i)]=image[u]
#         u=u+1
#     return render(request, 'trail.html', {'images': images,'i':0})
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def order_check(request,name):
    log=0
    if request.method=="POST":
        log=log+1
        
        ub = booking.objects.filter(username=name)
        b = Order.objects.filter(username=name)
        a=0
        for i in b:
            a=a+(int(i.price)*int(i.count))
        mount=a*100*83

        client = razorpay.Client(auth=("rzp_test_mkEAnH2fj4QnO2", "h9H07jUdtPrIorAd8SZc4leJ"))

        payment = client.order.create({'amount': mount, 'currency': 'INR','payment_capture': '1'})
        if payment['status'] == 'created':
            # Payment is not yet successful, handle this case as needed
            pass
        else:
            # Payment is successful, update the order status or mark it as paid
            for i in b:
                i.status='paid'
                i.save()
            pass           
        fil=['id','amount','amount_paid','amount_due','status','receipt']
        return render(request, 'check.html', {'fil':fil,'log': log, 'book': ub, 'b': b, 'name': name, 'mount': int(mount), 'a': a, 'payment1': payment})

        
    else:
        log=0
        ub = booking.objects.filter(username=name)
        b = Order.objects.filter(username=name)
        a=0
        for i in b:
            a=a+(int(i.price)*int(i.count))
        mount=a*100*83

        return render(request,'check.html',{'log':log,'book':ub,'mount':int(mount),'b':b,'name':name,'a':a})



from datetime import datetime
def tab_check(request, name):
    if request.method == "POST":
        pass
    else:
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().time().strftime("%H:%M")
        current_datetime=current_date+"T"+current_time
        b=booking.objects.filter(username=name, date__lt=current_datetime).delete()
        ub = booking.objects.filter(username=name)
        return render(request, 'check_tab.html', {'book': ub, 'name': name})

@csrf_exempt
def success(request):
    return render(request, "success.html")
