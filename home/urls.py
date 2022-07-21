from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('question/<str:slug>', views.question, name='question')

]
