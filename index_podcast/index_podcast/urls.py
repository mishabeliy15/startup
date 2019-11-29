from django.contrib import admin
from django.urls import path, include
from .views import IndexView, PoliticsView, IntroPage, SettingsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', IndexView.as_view(), name='index'),
    path('intro/', IntroPage.as_view(), name='intro'),
    path('privacy_policy/', PoliticsView.as_view(), name='privacy_policy'),
    path('mypodcasts/', include('mypodcasts.urls')),
    path('', include('publish_podcasts.urls')),
    path('settings/', include('category.urls')),
    path('settings/', include('languages.urls')),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('stats/', include('stats.urls')),
    path('reports/', include('reports.urls')),
]
