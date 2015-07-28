from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Timer

# Create your views here.

def home(request):
    timers = {'counter': Timer.objects.get(queue='Counter'),
    		  'selfservice': Timer.objects.get(queue='Self-service')
    		}
    template = loader.get_template('home.html')
    context = RequestContext(request, timers)
    return HttpResponse(template.render(context))