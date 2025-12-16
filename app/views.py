from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "app/home.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        queryset = Article.objects.filter(
            creator=self.request.user
        ).order_by("-create_at")

        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

    
class ArticleCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    template_name = "app/create_articles.html"
    model = Article
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("app:home")
    success_message = "Article created successfully!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Article
    template_name = "app/create_articles.html"
    fields = ["title", "status", "content", "twitter_post"]
    success_url = reverse_lazy("app:home")
    success_message = "Article updated successfully!"

    def test_func(self):
        return self.request.user == self.get_object().creator

class ArticleDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = Article
    template_name = "app/article_delete.html"
    success_url = reverse_lazy("app:home")

    def test_func(self):
        return self.request.user == self.get_object().creator

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Article deleted successfully!")
        return super().delete(request, *args, **kwargs)
