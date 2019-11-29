from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('-display')
    serializer_class = LanguageSerializer
