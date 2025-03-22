from django.contrib import admin
from .models import Election, Candidate, Vote

@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ("title", "start_date", "end_date", "is_active", "total_votes")
    list_filter = ("is_active",)
    search_fields = ("title", "description")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "election", "votes", "vote_percentage")
    list_filter = ("election",)
    search_fields = ("name", "department")


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "candidate", "election", "voted_at")
    list_filter = ("election",)
    search_fields = ("user__username", "candidate__name")
