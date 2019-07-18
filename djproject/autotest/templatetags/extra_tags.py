'''
Created on 2019年7月17日

@author: geqiuli
'''
from django import template

register = template.Library()

# use simple tag to show string
@register.simple_tag
def quotient(num1,num2):
    '''除法运算 - 商'''
    return int(float(num1)//float(num2))

@register.simple_tag
def remainder(num1,num2):
    '''除法运算 - 余数'''
    return int(float(num1)%float(num2))

