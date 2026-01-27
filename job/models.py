from django.db import models
from accounts.models import Recruiter, Skill, Location, Candidate


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    website = models.URLField(blank=True)
    recruiter = models.ForeignKey(
        Recruiter, on_delete=models.CASCADE, related_name="companys"
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, related_name="companys"
    )

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE = (
        ("FT", "Full Time"),
        ("PT", "Part Time"),
        ("IN", "Internship"),
        ("CT", "Contract"),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE)
    experience_required = models.IntegerField(help_text="Years of experience")
    salary = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = (
        ("APPLIED", "Applied"),
        ("SHORTLISTED", "Shortlisted"),
        ("REJECTED", "Rejected"),
        ("HIRED", "Hired"),
    )
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name="applications"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="APPLIED")
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("candidate", "job")

    def __str__(self):
        return f"{self.candidate.user.username} → {self.job.title}"


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_skills")
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("job", "skill")

    def __str__(self):
        return f"{self.job.title} - {self.skill.name}"
