from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
     home, login_view, signup_view, logout_view,dashboard,profile,settings,vote
)


urlpatterns = [
    path('', home, name='home'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('settings/',settings, name='settings'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('vote/', vote, name='vote'),
]
