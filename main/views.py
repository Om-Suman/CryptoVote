from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime
from .models import Election, Vote, Candidate,Profile
from django.utils import timezone
import json
import pycountry
import pytz
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
            #messages.success(request, f"Welcome, {user.username}!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")
@login_required
def dashboard(request):
    now = timezone.now()

    # Total elections count
    total_elections = Election.objects.count()

    # Ongoing elections (start_date <= now <= end_date)
    ongoing_elections = Election.objects.filter(start_date__lte=now, end_date__gte=now)

    # Completed elections (end_date < now)
    completed_elections = Election.objects.filter(end_date__lt=now)

    # Total voters count (from Profile)
    total_voters = Profile.objects.count()

    # Check if user is authenticated before getting username
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Guest"  # Default if no user is logged in

    context = {
        "total_elections": total_elections,
        "ongoing_elections": ongoing_elections,
        "completed_elections": completed_elections,
        "total_voters": total_voters,
        "username": username,  # Pass username to the template
        "active_page": "dashboard",  # Mark dashboard as active in sidebar
    }
    return render(request, "dashboard.html", context)
@login_required
def profile(request):
    user = request.user

    # Get list of countries and time zones
    countries = [{'code': c.alpha_2, 'name': c.name} for c in pycountry.countries]
    timezones = pytz.all_timezones

    if request.method == 'POST':
        full_name = request.POST.get('fullName', '')
        nick_name = request.POST.get('nickName', '')
        gender = request.POST.get('gender', '')
        country = request.POST.get('country', '')
        email = request.POST.get('email', '')
        timezone = request.POST.get('timezone', '')

        # Update user and profile details
        user.first_name = full_name
        user.last_name = nick_name
        user.profile.gender = gender
        user.profile.country = country
        user.email = email
        user.profile.timezone = timezone

        if 'profilePic' in request.FILES:
            user.profile.profile_pic = request.FILES['profilePic']

        user.save()
        user.profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(
        request,
        'profile.html',
        {
            'user': user,
            'countries': countries,
            'timezones': timezones,
        },
    )


@login_required
def vote(request):
    # Get all ongoing elections
    ongoing_elections = Election.objects.filter(
        start_date__lte=datetime.now(), end_date__gte=datetime.now()
    ).order_by("end_date")

    # Get the user's votes to prevent multiple voting
    user_votes = Vote.objects.filter(user=request.user)
    voted_election_ids = user_votes.values_list("election_id", flat=True)

    # Check if a vote is being submitted
    if request.method == "POST":
        election_id = request.POST.get("election_id")
        candidate_id = request.POST.get("candidate_id")

        # Ensure election and candidate exist
        election = get_object_or_404(Election, id=election_id)
        candidate = get_object_or_404(Candidate, id=candidate_id, election=election)

        # Check if the user has already voted in this election
        if election.id in voted_election_ids:
            messages.error(request, "You have already voted in this election.")
            return redirect("vote")

        # Save the vote and increase the candidate's vote count
        Vote.objects.create(
            user=request.user,
            election=election,
            candidate=candidate,
        )

        # Increment candidate votes
        candidate.votes += 1
        candidate.save()

        messages.success(request, f"You have successfully voted for {candidate.name}!")
        return redirect("vote")

    context = {
        "active_page": "vote",
        "ongoing_elections": ongoing_elections,
        "voted_election_ids": voted_election_ids,
    }
    return render(request, "vote.html", context)


@login_required
def user_settings(request):
    if request.method == "POST":
        # Get data from form
        new_password = request.POST.get("new_password")
        voting_updates = request.POST.get("voting_updates")
        newsletters = request.POST.get("newsletters")
        security_alerts = request.POST.get("security_alerts")
        two_factor = request.POST.get("two_factor")
        privacy_setting = request.POST.get("privacy_setting")

        # Change password if provided
        if new_password:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password changed successfully!")

        # Save other settings (Here, mock save. Customize for DB if needed)
        request.session["email_preferences"] = {
            "voting_updates": True if voting_updates else False,
            "newsletters": True if newsletters else False,
            "security_alerts": True if security_alerts else False,
        }
        request.session["two_factor"] = two_factor
        request.session["privacy_setting"] = privacy_setting

        messages.success(request, "Settings saved successfully!")
        return redirect("settings")

    # Initial data for display
    context = {
        "email_preferences": request.session.get("email_preferences", {}),
        "two_factor": request.session.get("two_factor", "off"),
        "privacy_setting": request.session.get("privacy_setting", "public"),
    }

    return render(request, "settings.html", context)

def logout_view(request):
    logout(request)
    return redirect('/login/') 
