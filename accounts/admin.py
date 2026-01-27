from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (
    User,
    Candidate,
    CandidateSkill,
    Education,
    Experience,
    Recruiter,
    Resume,
    Skill,
    Location,
)


class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email", "name", "role", "is_staff", "is_active")
    search_fields = ("email", "name")
    list_filter = ("role", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "role", "password1", "password2"),
            },
        ),
    )

    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, UserAdmin)
admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Skill)
admin.site.register(Location)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Resume)     