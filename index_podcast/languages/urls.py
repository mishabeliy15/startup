from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (LanguageCreateView, LanguageListView, LanguageDeleteView, LanguageUpdateView)
from .api_views import LanguageViewSet

app_name = 'languages'


router = DefaultRouter()
router.register('languages', LanguageViewSet)

urlpatterns = [
    path('languages', LanguageListView.as_view(), name='list'),
    path('languages/create', LanguageCreateView.as_view(), name='add'),
    path('languages/<int:pk>/update', LanguageUpdateView.as_view(), name='update'),
    path('languages/<int:pk>/delete', LanguageDeleteView.as_view(), name='delete'),
    path('api/', include(router.urls)),
]
