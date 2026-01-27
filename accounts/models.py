# from django.db import models
# from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from .managers import UserManager


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)
#     role = models.CharField(max_length=10)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()  # ✅ THIS FIXES YOUR ERROR

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["name", "role"]

#     def __str__(self):
#         return self.email


# class Candidate(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15)
#     location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
#     skill = models.ManyToManyField("Skill", through="CandidateSkill", blank=True)

#     def __str__(self):
#         return self.user.username


# class Skill(models.Model):
#     name = models.CharField(max_length=15, unique=True)

#     def __str__(self):
#         return self.name


# class Location(models.Model):
#     city = models.CharField(max_length=10)
#     state = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.city}, {self.state}"


# class Education(models.Model):
#     user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#     degree = models.CharField(max_length=100)
#     university = models.CharField(max_length=100)
#     start_year = models.IntegerField()
#     end_year = models.IntegerField()

#     def __str__(self):
#         return self.degree


# class Experience(models.Model):
#     user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#     company = models.CharField(max_length=100)
#     role = models.CharField(max_length=100)
#     start_year = models.DateField()
#     end_year = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.company


# class Resume(models.Model):
#     user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#     file = models.FileField(upload_to="resumes/")
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name


# class CandidateSkill(models.Model):
#     candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("candidate", "skill")

# class Recruiter(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=100)
#     location = models.ForeignKey(
#         Location, on_delete=models.SET_NULL, null=True, blank=True
#     )

#     def __str__(self):
#         return self.user.username



from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("CANDIDATE", "Candidate"),
        ("RECRUITER", "Recruiter"),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "role"]

    def __str__(self):
        return self.email


class Skill(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.state}"


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.email


class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.email


class Education(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.degree


class Experience(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company


class Resume(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("candidate", "skill")