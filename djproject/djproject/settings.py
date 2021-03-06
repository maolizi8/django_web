"""
Django settings for djproject project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's3#_iax8uj$d0=%r%&a+xkgq1n3v$s$=_05t9b!^@dad8m1n0u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False #生产环境请使用 False

# 允许访问的ip
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',   #api
    'django_python3_ldap', # ldap3
    
    # project apps
    'autotest',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # 未登录请求接口异常
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
'''
# django默认的数据库连接方式
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
## 改成mysql数据库：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE_NAME',
        'USER': 'CONNECTION_USERNAME',
        'PASSWORD': 'CONNECTION_PASSWORD',
        #'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'HOST': 'XX.XX.XX.XX',   # Or an IP Address that your DB is hosted on
        'PORT': 3306,
        'CHARSET':'utf8'
    }
}




# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


'''--------添加ldap认证登录方法--------'''
AUTHENTICATION_BACKENDS = (
    "django_python3_ldap.auth.LDAPBackend",  #配置为先使用LDAP认证，如通过认证则不再使用后面的认证方式
    "django.contrib.auth.backends.ModelBackend",
)
LDAP_AUTH_URL = 'ldap://xx.xx.xx.xx:389'
LDAP_AUTH_USE_TLS = False
LDAP_AUTH_CONNECTION_USERNAME = "username for auth-connection, provided from IT"
LDAP_AUTH_CONNECTION_PASSWORD = "password for auth-connection, provided from IT"

LDAP_AUTH_SEARCH_BASE = 'dc=domain,dc=com' # 获取所有的用户

#LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"
LDAP_AUTH_OBJECT_CLASS = "user"
LDAP_AUTH_USER_FIELDS  = {
            "username": "sAMAccountName",
            
            # ./manage.py ldap_sync_users时，添加上以下参数，可将信息同步，
            "first_name": "givenName",
            "last_name": "sn",
            "email": "userPrincipalName",
        }
# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
LDAP_AUTH_SYNC_USER_RELATIONS = "django_python3_ldap.utils.sync_user_relations"
LDAP_AUTH_FORMAT_SEARCH_FILTERS = "django_python3_ldap.utils.format_search_filters"
#LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_openldap"
# #For user-principal-name formats (e.g. "user@domain.com"):
LDAP_AUTH_FORMAT_USERNAME="django_python3_ldap.utils.format_username_active_directory_principal"
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN="domain.com"



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# django默认的语音及时区
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_TZ = True
# 更改为中国时区
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

USE_I18N = True

USE_L10N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

'''以下均为新增，非默认设置'''
# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
 
# 其它 存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #'/path/to/others/static/',  # 用不到的时候可以不写这一行
)
 
# 这个是默认设置，Django 默认会在 STATICFILES_DIRS中的文件夹 和 各app下的static文件夹中找文件
# 注意有先后顺序，找到了就不再继续找了
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

# 文件和图片等
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# 全局登录页面
LOGIN_URL = '/login/'

# rest的接口
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    )
}
