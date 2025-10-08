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
    # get all user details
    path('get-all-users/', views.all_user_details, name='all_user_details'),
    # get user by email
    path('get-user-by-email/<str:Email>', views.user_details_by_email, name='user_by_email'),   
    # update user details
    path('update-user-details/<str:Email>', views.update_user_details, name='update_user_details'),    
    # delete user
    path('delete-user/<str:Email>', views.delete_user, name='delete_user'),     
]
