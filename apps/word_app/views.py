# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import string
import random
from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    # print 'd@m'*50
    try:
        print request.session['attempt']
    except KeyError:
        request.session['attempt'] = 0
    return render(request, 'word_app/index.html')

def generate(request):
    if request.method == 'POST':
        request.session['attempt'] += 1
        request.session['randomword'] = (
            ''.join(random.choice(string.ascii_uppercase) for x in range(14))
        )
    return redirect('/')
