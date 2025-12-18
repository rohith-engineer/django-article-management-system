from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Article, UserProfile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "word_count", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("word_count", "created_at", "updated_at")


@admin.register(UserProfile)
class CustomUserAdmin(UserAdmin):
    model = UserProfile

    # REMOVE username completely
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )

    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    # CRITICAL: tell Django there is NO username
    filter_horizontal = ("groups", "user_permissions")
