'''
Created on 2018年5月9日

@author: geqiuli
'''
from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello world ! ")