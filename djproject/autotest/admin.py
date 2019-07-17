from django.contrib import admin

# Register your models here.
# from autotest.models import UIboardFirstMenu
# from autotest.models import UIboardSecondMenu
# 
# @admin.register(UIboardFirstMenu)
# class UIFirstMenuAdmin(admin.ModelAdmin):
#     # 配置显示字段,
#     list_display = ['name','envronment']
#     # 配置查询字段
#     search_fields = ['name']
#     # 配置排序字段
#     ordering = ['name','envronment']
#     # 配置右边是否有过滤条件字段
#     list_filter = ['envronment']
#     # 配置列表页可编辑字段
#     #list_editable = ['account','password']
# 
# @admin.register(UIboardSecondMenu)
# class UISecondMenuAdmin(admin.ModelAdmin):
#     # 配置显示字段,
#     list_display = ['name','envronment','first_menu','repo_name','proj_name','package_name']
#     # 配置查询字段
#     search_fields = ['name']
#     # 配置排序字段
#     ordering = ['name','envronment','first_menu']
#     # 配置右边是否有过滤条件字段
#     list_filter = ['envronment','first_menu']
#     # 配置列表页可编辑字段
#     #list_editable = ['account','password']    