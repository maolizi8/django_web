'''
Created on 2019年7月5日

@author: geqiuli
'''
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    userName = forms.CharField(label=u'用户名',min_length = 3,max_length = 20)
    userPassword = forms.CharField(label=u'登录密码',min_length= 6,max_length = 20,error_messages = {'min_length':u'密码至少6位','max_length':u'密码最长20位'})
    userConfirmPassword = forms.CharField(label=u'确认密码',min_length = 6,max_length = 20,error_messages = {'min_length':u'密码至少6位','max_length':u'密码最长20位'})
    userEmail = forms.EmailField(label=u'邮箱')

    def clean_userName(self):
        userName = self.cleaned_data['userName']
        user = User.objects.filter(username = userName)
        if user:
            raise forms.ValidationError(u'用户名已存在')
        return userName

    def clean_userConfirmPassword(self):
        userPassword = self.cleaned_data['userConfirmPassword']
        userConfirmPassword = self.cleaned_data['userConfirmPassword']
        if userPassword != userConfirmPassword:
            raise forms.ValidationError(u'两次密码不一致')
        return userPassword


class ResetPasswordForm(forms.Form):
    userName = forms.CharField(label=u'用户名',min_length = 3,max_length = 20)
    userPassword = forms.CharField(label=u'登录密码', min_length=6, max_length=20,error_messages={'min_length': u'密码至少6位', 'max_length': u'密码最长20位'})
    userConfirmPassword = forms.CharField(label=u'确认密码',min_length = 6,max_length = 20,error_messages = {'min_length':u'密码至少6位','max_length':u'密码最长20位'})

    def clean_userName(self):
        userName = self.cleaned_data['userName']
        user = User.objects.filter(username = userName)
        print(user)
        if not user:
            raise forms.ValidationError(u'用户名不存在')
        return userName


    def clean_userConfirmPassword(self):
        userPassword = self.cleaned_data['userPassword']
        userConfirmPassword = self.cleaned_data['userConfirmPassword']
        print(userPassword,userConfirmPassword)

        if userPassword != userConfirmPassword:
            raise forms.ValidationError(u'两次密码不一致')
        return userPassword