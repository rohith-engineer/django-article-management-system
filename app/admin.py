from django.contrib import admin
from app.models import Article, UserProfile
from django.contrib.auth.admin import UserAdmin

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "word_count", "create_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    date_hierarchy = "create_at"
    ordering = ("create_at",)
    readonly_fields = ("word_count", "create_at", "updated_at")

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None,{"fields":("email","password")}),
        ("Personal Info",{"fields":("first_name","last_name")}),
        ("Permissions",{"fields":("is_active","is_staff","is_superuser","groups","user_permission")}),
        ("Important Dates",{"fields":("last_login","date_joined")}),
    )
    add_fieldsets = (
        (None,{
            "classes":("wide"),
            "fields":("email","password1","password2")
               }),
    )
    model = UserProfile
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

# Correct registration
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile,CustomUserAdmin)
