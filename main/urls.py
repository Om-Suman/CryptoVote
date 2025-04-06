from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
     home, login_view, signup_view, logout_view,dashboard,profile, user_settings,vote
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('Settings/', user_settings, name='settings'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('vote/', vote, name='vote'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)