from . import views
from django.urls import path
from User.authentication.views import UserCreateView, UserLoginView
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register_user'),
    path('login/', UserLoginView.as_view(), name='login_user'),
    path('logout/', views.log_out, name='logout'),
]
