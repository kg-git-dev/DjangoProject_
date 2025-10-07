from django.urls import path
from . import views

urlpatterns = [
    # return "Hello World"
    path('', views.hello_world, name='hello_world'),   
    # sign up
    path('signup/', views.sign_up, name='sign_up'),   
    # login
    path('login/', views.log_in, name='log_in'),   
]
