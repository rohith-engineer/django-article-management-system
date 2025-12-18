from pathlib import Path
import os

# ==================================================
# BASE
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# ENVIRONMENT
# ==================================================
ENV_STATE = os.getenv("ENV_STATE", "DEVELOPMENT").upper()
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# ==================================================
# SECURITY
# ==================================================
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-only")


if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is not set")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# Production-only security
if ENV_STATE == "PRODUCTION":
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# ==================================================
# SITE
# ==================================================
SITE_ID = 1
ADMIN_URL = os.getenv("ADMIN_URL", "admin/")

# ==================================================
# INSTALLED APPS
# ==================================================
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",

    # Third-party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "widget_tweaks",

    # Local
    "app.apps.AppConfig",
    "django_browser_reload",
        
    ]

# ==================================================
# MIDDLEWARE
# ==================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",

    # REQUIRED by django-allauth
    "allauth.account.middleware.AccountMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# ==================================================
# URLS / WSGI
# ==================================================
ROOT_URLCONF = "djangocourse.urls"
WSGI_APPLICATION = "djangocourse.wsgi.application"

# ==================================================
# TEMPLATES
# ==================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # REQUIRED for allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==================================================
# DATABASE
# ==================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==================================================
# AUTH
# ==================================================
# =========================
# AUTH USER MODEL
# =========================
AUTH_USER_MODEL = "app.UserProfile"

# =========================
# DJANGO AUTH
# =========================
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# =========================
# DJANGO-ALLAUTH (EMAIL ONLY — NO USERNAME)
# =========================
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_LOGIN_METHODS = {"email"}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_SIGNUP_FIELDS = ["email", "password1", "password2"]

ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# ==================================================
# SOCIAL AUTH (GitHub – optional)
# ==================================================
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

SOCIALACCOUNT_PROVIDERS = {}

if GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET:
    SOCIALACCOUNT_PROVIDERS["github"] = {
        "APP": {
            "client_id": GITHUB_CLIENT_ID,
            "secret": GITHUB_CLIENT_SECRET,
            "key": "",
        }
    }

# ==================================================
# PASSWORD VALIDATION
# ==================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==================================================
# I18N / TIME
# ==================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "djangocourse" / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# ==================================================
# DEFAULT PK
# ==================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==================================================
# DEBUG TOOLS
# ==================================================
if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]
