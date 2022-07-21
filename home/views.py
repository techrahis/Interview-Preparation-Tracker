from multiprocessing import context
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from requests import post
from home.models import*
from category.models import*
from topic.models import*
from question.models import*
from user.models import*


@login_required(login_url='HandleLogin')
def homepage(request):
    category = Category.objects.all()
    topic = Topic.objects.all()
    context = {
        'category': category,
        'topic': topic,
    }
    current_user = "Welcome home "+str(request.user.first_name) + " 🚀"
    messages.success(request, current_user)
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='HandleLogin')
def question(request, slug):
    if request.method == "GET":
        question = Question.objects.filter(question_tIdentifier=slug).values()
        attempted = Question_Attempted.objects.filter(
            user=request.user.username).values()
        context = {
            'question': question,
            'attempted': attempted
        }
        template = loader.get_template('question.html')
        return HttpResponse(template.render(context, request))

    if request.method == "POST":
        # print(request.user.username)
        # print(request.POST['val'])
        try:
            attempted = Question_Attempted.objects.create(
                user=request.user.username, attempted_question_qIdentifier=request.POST['val'])
        except:
            messages.success(request, "Data present")
        question = Question.objects.filter(question_tIdentifier=slug).values()
        attempted = Question_Attempted.objects.filter(
            user=request.user.username).values()
        return redirect(slug)
