"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from autotest import views as auto_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auto_view.Login.as_view(),name='login'),
    path('logout/',auto_view.Logout.as_view(),name='logout'),
    path('qahome/',auto_view.QAHome.as_view(),name='qahome'),
    path('qahome/login/',auto_view.QAHome.as_view(),name='qahomelogin'),
    path('qahome/logout/',auto_view.QAHome.as_view(),name='qahomelogout'),
    path('qahome/webui/',auto_view.UIWeb.as_view(),name='webui'),
    path('qahome/androidui/',auto_view.UIAndroid.as_view(),name='androidui'),
    path('qahome/collectioninfo/',auto_view.get_collection_info),
    path('qahome/gettestcases/',auto_view.query_testcase_list),
    path('qahome/updateestimate/',auto_view.update_case_estimatetime),
]
