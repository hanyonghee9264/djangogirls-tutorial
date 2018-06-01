from django.http import HttpResponse
from django.shortcuts import render

def post_list(requests):
    return HttpResponse('Post List입니다')
