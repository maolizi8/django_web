from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse

from django.contrib.auth.models import User,Permission
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin


from public import mysql_opr

    
#登录功能
class Login(View):
    def get(self,request):
        #return render(request,'sign_in.html')
        return render(request,'yiqa_login.html',{'message':''})

    def post(self,request):
        userName = request.POST.get('userName')
        userPassword = request.POST.get('userPassword')
        print(userName,userPassword)
        #验证用户，它接受两个参数，用户名 username 和 密码 password,认证只有是否激活跟用户名密码。
        user = authenticate(username = userName,password = userPassword)
        #并在密码对给出的用户名合法的情况下返回一个 User 对象。 如果密码不合法，authenticate()返回None。
        if user is not None:
            if user.is_active:
                #登录，向session中添加SESSION_KEY, 便于对用户进行跟踪:
                login(request,user)
                # 如果调用login方法以后，
                # request对象就会激活user属性，这个属性不管登录或者未登录都是存在
                return redirect(reverse('qahome'))
            else:
                message = '该用户未激活'
        else:
            message = '用户名或密码错误'

        return render(request,'yiqa_login.html',locals())

#注销功能
class Logout(View):
    def get(self,request):
        #注销用户，这个方法就会把我们的session跟cookie清理掉
        logout(request)
        message = '注销成功'
        return render(request,'yiqa_home.html',locals())
        
#class QAHome(LoginRequiredMixin,View): #登录验证,主要用于比如说直接输入地址情况。
class QAHome(View):
    # 如果需要指定单独的跳转，则该类中指定login_url属性
    # 如果需要指定全局的，则在settings中指定LOGIN_URL属性
    #login_url = '/login/'#没有登录则指定跳转
    def get(self,request):
        #return render(request,'sign_in.html')
        return render(request,'yiqa_home.html',{'message':''})
        

    def post(self,request):
        userName = request.POST.get('userName')
        userPassword = request.POST.get('userPassword')
        print(userName,userPassword)
        #验证用户，它接受两个参数，用户名 username 和 密码 password,认证只有是否激活跟用户名密码。
        user = authenticate(username = userName,password = userPassword)
        #并在密码对给出的用户名合法的情况下返回一个 User 对象。 如果密码不合法，authenticate()返回None。
        if user is not None:
            if user.is_active:
                #登录，向session中添加SESSION_KEY, 便于对用户进行跟踪:
                login(request,user)
                # 如果调用login方法以后，
                # request对象就会激活user属性，这个属性不管登录或者未登录都是存在
                return redirect(reverse('webui'))
            else:
                message = '该用户未激活'
        else:
            message = '用户名或密码错误'

        return render(request,'yiqa_home.html',locals())
#     def get(self,request):
#         #print(request.COOKIES)
#         #print(locals())
#         query0 = 'select * from auto_ui_collection where run_env=0'
#         query1 = 'select * from auto_ui_collection where run_env=2'
#         conn=mysql_opr.get_connection_qadb('qatest')
#         test_menus=mysql_opr.select_from_mysql(conn,query0,total=0)['data']
#         prd_menus=mysql_opr.select_from_mysql(conn,query1,total=0)['data']
#         print(locals())
#         return render(request, 'yiqa_home.html', locals())
    
#class UIWeb(LoginRequiredMixin,View): #登录验证,主要用于比如说直接输入地址情况。
#class UIWeb(View):
class UIWeb(LoginRequiredMixin,View): #登录验证,主要用于比如说直接输入地址情况
    # 如果需要指定单独的跳转，则该类中指定login_url属性
    # 如果需要指定全局的，则在settings中指定LOGIN_URL属性
    #login_url = '/login/'#没有登录则指定跳转
    def get(self,request):
        #print(request.COOKIES)
        menu_active='webui'
        query0 = 'select * from auto_ui_collection where run_env=0 and ui_sys=0'
        query1 = 'select * from auto_ui_collection where run_env=2 and ui_sys=0'
        conn=mysql_opr.get_connection_qadb('qatest')
        test_menus=mysql_opr.select_from_mysql(conn,query0,total=0)['data']
        prd_menus=mysql_opr.select_from_mysql(conn,query1,total=0)['data']
        #print(locals())
        return render(request, 'yiqa_webui.html', locals())


class UIAndroid(LoginRequiredMixin,View): 
    def get(self,request):
        #print(request.COOKIES)
        menu_active='androidui'
        query0 = 'select * from auto_ui_collection where run_env=0 and ui_sys=1'
        query1 = 'select * from auto_ui_collection where run_env=2 and ui_sys=1'
        conn=mysql_opr.get_connection_qadb('qatest')
        test_menus=mysql_opr.select_from_mysql(conn,query0,total=0)['data']
        prd_menus=mysql_opr.select_from_mysql(conn,query1,total=0)['data']
        #print(locals())
        return render(request, 'yiqa_webui.html', locals())
           
@api_view(['post'])
def get_collection_info(request):
    ''''''
    collectionid=request.POST['collectionid']
    query0 = 'select name,run_env from auto_ui_collection where id='+str(collectionid)
    #query1 = 'select * from auto_ui_testcase where collection='+str(collectionid)
    query1 = """SELECT a.*,b.id AS module_id,b.name AS module_name FROM auto_ui_testcase a
                LEFT JOIN auto_ui_businessmodule b 
                ON a.business_module=b.id
                WHERE a.collection="""+str(collectionid)
    query2 = 'select id,name from auto_ui_businessmodule where collection='+str(collectionid)
    conn=mysql_opr.get_connection_qadb('qatest')
    rsp_data1=mysql_opr.select_from_mysql(conn,query0,total=1)
    rsp_data2=mysql_opr.select_from_mysql(conn,query1,total=0)
    rsp_data3=mysql_opr.select_from_mysql(conn,query2,total=0)
       
    return JsonResponse({"collection":rsp_data1['data'],
                         "testcases":rsp_data2['data'],
                         "testmodule":rsp_data3['data']}, safe=False) 

@api_view(['post'])
def query_testcase_list(request):
    ''''''
    collectionid=request.POST['collectionid']
    moduleid=request.POST['moduleid']
    tapdid=request.POST['tapdid']
    keyword=request.POST['keyword']
    print('moduleid:',moduleid)
    print('tapdid:',tapdid)
    print('keyword:',keyword)
    #query1 = 'select * from auto_ui_testcase where collection='+str(collectionid)
    query1 = """SELECT a.*,b.id AS module_id,b.name AS module_name FROM auto_ui_testcase a
                LEFT JOIN auto_ui_businessmodule b 
                ON a.business_module=b.id
                WHERE a.collection="""+str(collectionid)
    if tapdid:
        query1+=' and tapd_id='+tapdid
    if moduleid:
        query1+=' and business_module='+moduleid
    if keyword:
        query1+=' and py_desc like \'%'+keyword+'%\''
    print('query1:',query1)
    conn=mysql_opr.get_connection_qadb('qatest')
    rsp_data=mysql_opr.select_from_mysql(conn,query1,total=0)
    return JsonResponse(rsp_data, safe=False) 

@api_view(['post'])
def update_case_estimatetime(request):
    '''更新运行时间'''
    py_name=request.POST['py_name']
    
    query1 = "SELECT AVG(test_duration) as avg FROM uitest_run_records WHERE test_name='"+py_name+"'"
    conn=mysql_opr.get_connection_qadb('qatest')
    rsp_data=mysql_opr.select_from_mysql(conn,query1,total=1)
    if rsp_data['code']==0:
        if rsp_data['data']['avg']:
            query2="UPDATE auto_ui_testcase SET estimate_time={0} WHERE py_name='{1}'".format(rsp_data['data']['avg'],
                                                                                              py_name)
            mysql_opr.query_mysql2(conn,query2,close=True)
    return JsonResponse(rsp_data, safe=False) 

#展示主页
# class Home(PermissionRequiredMixin,View):
#     #单个权限
#     permission_required = 'auth_study.view_products'
#     #多个权限，要同时具有，且的关系,元祖或列表都可
#     # permission_required = ['auth_study.view_products','auth_study.update_products']
#     #上面个相当于全局的，只有满足了上面权限中的一个就可以进入下面的get了，否则就跳转到setting配置的LOGIN_URL去了
#     def get(self,request):
#         print('get...',request.user.user_permissions.all())
#         #has_perm(perm)： 判断用户是否有某个权限。
#         #has_perms(perm_list)： 判断用户是否有权限列表中的某个列表。
#         if request.user.has_perm('auth_study.view_products'):
#             products = Product.objects.all()
#             if request.user.has_perm('auth_study.add_products'):
#                 canAdd = True   #判断有没有添加权限，然后置为True,页面去判断是否显示相关
#         else:
#             message = '没有查看商品的权限'
#         return render(request,'home.html',locals())    
# #注册功能
# class Register(View):
# 
#     def get(self,request):
#         return render(request,'sign_up.html')
# 
#     def post(self,request):
#         form = RegisterForm(request.POST)
#         print(form.is_bound)
# 
#         if form.is_valid():
#             userName = form.cleaned_data['userName']
#             userPassword = form.cleaned_data['userPassword']
#             userConfirmPassword = form.cleaned_data['userConfirmPassword']
#             userEmail = form.cleaned_data['userEmail']
#             #create_user可以由Django自动将密码加密，而create还需要先将密码自己加密再给
#             user = User.objects.create_user(username=userName,email=userEmail,password=userPassword)
#             #给用户添加权限，多对多关系，用add添加
#             user.user_permissions.add(Permission.objects.get(codename='view_products'))
#             user.save() #需要save，因为他们都是一个数据库操作
# 
#             return HttpResponse(u'注册成功，请返回<a href="/auth/login">登录</a>')
#         else:
# 
#             return render(request,'sign_up.html',locals())
# 
# 
# 
 

 
#重置密码
# class ResetPassword(View):
#     def get(self,request):
#         return render(request,'resetpassword.html')
# 
#     def post(self,request):
#         form = ResetPasswordForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['userName']
#             userPassword = form.cleaned_data['userPassword']
#             user = User.objects.get(username=username)
#             print(user)
#             if user:
#                 user.set_password(userPassword)
#                 user.save()
#                 return render(request, 'sign_in.html', locals())
# 
#         return render(request, 'resetpassword.html', locals())
# 
