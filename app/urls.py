from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, article_list, get_csrf_token

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('articles-list/', article_list, name='article-list'),
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
]