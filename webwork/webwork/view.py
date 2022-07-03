# views.py

from quopri import encodestring
from django.shortcuts import render
import json
import os

BASE_URL = os.path.abspath('./webwork')


def index(request):
    #print("path",BASE_URL)
    f = open(BASE_URL+'/templates/index.json',encoding='utf-8')
    js = f.read()
    js = json.loads(js)
    return render(request, 'index.html', js)

def login(request):
    return render(request,'login.html')

def logup(request):
    return render(request,'logup.html')