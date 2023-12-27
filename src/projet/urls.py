"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('feature/', views.feature_view, name='feature'),
    path('feature/pie', views.feature_view, name='feature/pie'),
    path('feature/bar', views.feature_view, name='feature/bar'),
    path('feature/scatter', views.feature_view, name='feature/scatter'),
    path('feature/doughnut', views.feature_view, name='feature/doughnut'),
    path('feature/bubble', views.feature_view, name='feature/bubble'),
    path('feature/line', views.feature_view, name='feature/line'),
    path('feature/polarArea', views.feature_view, name='feature/polarArea'),
    path('feature/area', views.feature_view, name='feature/area'),
    path('feature/radar', views.feature_view, name='feature/radar'),
    path('feature/mixed', views.feature_view, name='feature/mixed'),
    path('compoenents/mixed', views.feature_view, name='mixed'),
    path('chart/', views.chart_view, name='chart'),
    path('graph/', views.graph_view, name='graph'),
    path('upload/', views.upload_view, name='upload'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
