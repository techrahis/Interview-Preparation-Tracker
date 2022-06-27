from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.HandleLogin, name='HandleLogin'),
    path('register/',views.register, name='register'),
    path('logout/',views.HandleLogout, name='HandleLogout')
]
