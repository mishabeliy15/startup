from rest_framework import permissions, viewsets
from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-display')
    serializer_class = CategorySerializer
