from django.urls import path
from . import views
from django.contrib.auth import logout
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
