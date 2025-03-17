from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import Position, Candidate, Voter, Vote
from .serializers import PositionSerializer, CandidateSerializer, VoterSerializer, VoteSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

# 🟢 API to Fetch Voting Statistics
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vote_statistics(request):
    candidates = Candidate.objects.all()
    positions = Position.objects.all()
    
    data = {
        "total_votes": Vote.objects.count(),
        "total_candidates": Candidate.objects.count(),
        "total_voters": Voter.objects.count(),
        "votes_per_candidate": {candidate.name: candidate.votes for candidate in candidates},
        "votes_per_position": {position.title: position.candidates.count() for position in positions}
    }
    
    return JsonResponse(data)

# 🟢 API to Cast Vote
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
@login_required
def cast_vote(request):
    voter = get_object_or_404(Voter, user=request.user)  # ✅ This will now work
    if voter.has_voted:
        return Response({"error": "You have already voted."}, status=400)

    candidate_id = request.data.get("candidate_id")
    candidate = get_object_or_404(Candidate, id=candidate_id)

    Vote.objects.create(voter=voter, candidate=candidate)
    voter.has_voted = True
    voter.save()

    return Response({"message": "Vote cast successfully!"}, status=200)
# 🟢 Render Dashboard Page
@login_required(login_url='/login/')
def dashboard_view(request):
    positions = Position.objects.all()
    candidates = Candidate.objects.all()
    
    return render(request, 'dashboard.html', {
        "positions": positions,
        "candidates": candidates
    })
def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/login/') 
