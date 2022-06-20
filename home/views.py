from django.http import HttpResponse
from django.template import loader
from home.models import Topic, Question


def home(request):
    topic = Topic.objects.all()
    context = {
        'topic': topic,
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def question(request, slug):
    template = loader.get_template('question.html')
    return HttpResponse(template.render())