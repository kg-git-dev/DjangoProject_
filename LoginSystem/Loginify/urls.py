from django.urls import path
from . import views

urlpatterns = [
    # return "Hello World"
    path('', views.hello_world, name='hello_world'),   
    # sign up
    path('signup/', views.SignUpView.as_view(), name='sign_up'),   
    # login
    path('login/', views.LogInView.as_view(), name='log_in'),
    # login success
    path('success/', views.LoginSuccessView.as_view(), name='login_success'),

]
