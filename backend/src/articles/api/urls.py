from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls



# from django.urls import path

# from .views import (
#     ArticleListView,
#     ArticleDetailView,
#     ArticleCreatView,
#     ArticleUpdateView,
#     ArticleDeleteView
# )


# urlpatterns = [
#     path('', ArticleListView.as_view()),

#     path('create/', ArticleCreatView.as_view()),

#     path('<pk>', ArticleDetailView.as_view()),

#     path('<pk>/update/', ArticleUpdateView.as_view()),

#     path('<pk>/delete/', ArticleDeleteView.as_view()),  

# ]