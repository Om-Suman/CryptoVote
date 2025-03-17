from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PositionViewSet, CandidateViewSet, VoterViewSet, VoteViewSet, 
    dashboard_view, vote_statistics, home, login_view, signup_view, logout_view,cast_vote
)

router = DefaultRouter()
router.register(r'positions', PositionViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'voters', VoterViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),  
    path('api/vote-stats/', vote_statistics, name='vote_statistics'),
    path('api/cast-vote/', cast_vote, name='cast_vote'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]
