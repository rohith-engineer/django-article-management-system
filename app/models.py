from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import re

from app.manager import UserManager

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)


class UserProfile(AbstractUser):
    """
    Custom User model:
    - Email-only authentication
    - No username field
    - Compatible with django-allauth (stable mode)
    """

    username = None  # remove username completely

    email = models.EmailField(
        _("email address"),
        unique=True,
        max_length=255,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def article_count(self):
        return self.articles.count()

    @property
    def written_word_count(self):
        return (
            self.articles.aggregate(
                total=models.Sum("word_count")
            )["total"] or 0
        )


class Article(models.Model):
    title = models.CharField(_("title"), max_length=100)
    content = models.TextField(_("content"), blank=True, default="")
    word_count = models.PositiveIntegerField(_("word count"), default=0)
    twitter_post = models.TextField(_("twitter post"), blank=True, default="")
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=ARTICLE_STATUS,
        default="draft",
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("creator"),
        on_delete=models.CASCADE,
        related_name="articles",
    )

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", "")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
