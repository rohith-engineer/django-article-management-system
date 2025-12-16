from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import re
from app.manager import UserManager
from django.utils.translation import gettext_lazy as _

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)

class UserProfile(AbstractUser):
    username = None  # ❗ remove username completely

    email = models.EmailField(_("email address"), max_length=255, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def article_count(self):
        return self.articles.count()

    @property
    def written_word_count(self):
        return self.articles.aggregate(total=models.Sum('word_count'))['total'] or 0

# my users.articles_count()

class Article(models.Model):
    title = models.CharField(_("title"), max_length=100)
    content = models.TextField(_("content"), blank=True, default="")
    word_count = models.IntegerField(_("word count"), blank=True, default=0)
    twitter_post = models.TextField(_("twitter post"), blank=True, default="")
    status = models.CharField(_("status"), max_length=20, choices=ARTICLE_STATUS, default="draft")
    create_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("creator"),
                                on_delete=models.CASCADE, related_name="articles")

    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", "")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)
