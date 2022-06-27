from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.models import*

@login_required(login_url='HandleLogin')
def homepage(request):    
    current_user = "Welcome to our site "+str(request.user)
    messages.success(request, current_user) 
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='HandleLogin')
def question(request):
    template = loader.get_template('question.html')
    return HttpResponse(template.render({}, request))

