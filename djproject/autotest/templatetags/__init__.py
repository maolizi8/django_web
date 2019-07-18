from django.apps import AppConfig
import os

default_app_config='qatools.QatoolsConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class QatoolsConfig(AppConfig):
    name = 'qatools'
    verbose_name =  '质量部工具管理'