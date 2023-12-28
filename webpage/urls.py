"""
URL configuration for webpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from django.conf import settings  
from django.conf.urls.static import static  




urlpatterns = [
    
    path('signup/', views.singup),
    path('login/', views.login),
    path('', views.home),
  
     path('admin/', admin.site.urls), 
        path('res/<name>',views.my_view1),
        path('/res_tab_check/<name>',views.tab_check),#reservation
         path('home/',views.home),
          path('/menu/<name>',views.menu,name="menu"),# path('menu/',views.newmenu,name="menu"),
          
         path('adminmenu/',views.admin),
           path('order_check/<name>',views.order_check),


]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
