from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryCreateView, SubCategoryCreateView, CategoryListView, CategoryDeleteView, CategoryUpdateView,
                    SubCategoryUpdateView, SubCategoryDeleteView)
from .api_views import CategoryViewSet
app_name = 'category'

router = DefaultRouter()
router.register('category', CategoryViewSet)

urlpatterns = [
    path('category', CategoryListView.as_view(), name='list-category'),
    path('category/create', CategoryCreateView.as_view(), name='add-category'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='update-category'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='delete-category'),
    path('subcategory/create', SubCategoryCreateView.as_view(), name='add-subcategory'),
    path('subcategory/<int:pk>/update', SubCategoryUpdateView.as_view(), name='update-subcategory'),
    path('subcategory/<int:pk>/delete', SubCategoryDeleteView.as_view(), name='delete-subcategory'),
    path('api/', include(router.urls)),
]
