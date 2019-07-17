from django.db import models

# Create your models here.
# yes_or_no=(
#         (0,'否'),
#         (1,'是')
#         )
# env_choices=(
#         (0,'测试环境'),
#         (1,'预发布环境'),
#         (2,'生产环境'),
#         (3,'其他工具类')
#         )

# class RepoInfo(models.Model):
#     repo_name = models.CharField('git库名',max_length=100,null=False,blank=False)
#     root_dir = models.CharField('git库所处根目录',max_length=100,null=False,blank=False)
#      
# 
# class UIboardFirstMenu(models.Model):
#     '''UI自动化平台一级菜单'''
#     name = models.CharField('菜单名称',max_length=30,null=False,blank=False)
#     envronment = models.IntegerField('UI脚本环境',choices=yes_or_no,null=False,blank=False,default=0) 
#     
#     def __str__(self):
#         return self.name
#      
#     class Meta:  
#         verbose_name = 'UI平台一级菜单'  
#         verbose_name_plural = 'UI平台一级菜单'  
# 
# class UIboardSecondMenu(models.Model):
#     '''UI自动化平台二级菜单'''
#     name = models.CharField('菜单名称',max_length=30,null=False,blank=False)
#     first_menu=models.ForeignKey('UIboardFirstMenu',on_delete='SET_NULL',null=False,blank=False) 
#     envronment=models.IntegerField('UI脚本环境',choices=yes_or_no,null=False,blank=False,default=0) 
#     repo_name = models.CharField('git库名称',max_length=30,null=False,blank=False)
#     proj_name = models.CharField('项目名称',max_length=30,null=False,blank=False)
#     package_name = models.CharField('包名称',max_length=30,null=False,blank=False,help_text='项目下包名，多级以英文句点.连接：testenv_case.b2b_pc')
#     
#     def __str__(self):
#         return self.name
#      
#     class Meta:  
#         verbose_name = 'UI平台二级菜单'  
#         verbose_name_plural = 'UI平台二级菜单'  