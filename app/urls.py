from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "app"

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path("create/", ArticleCreateView.as_view(), name="create_articles"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="update_articles"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="delete_articles"),
]
