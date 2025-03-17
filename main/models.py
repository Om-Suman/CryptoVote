from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="candidates")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.position.title}"

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)  # Default for existing rows

    class Meta:
        unique_together = ("voter", "candidate")

    def clean(self):
        if Vote.objects.filter(voter=self.voter, candidate__position=self.candidate.position).exists():
            raise ValidationError("You can only vote once per position.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.voter.user.username} -> {self.candidate.name} ({self.candidate.position.title})"