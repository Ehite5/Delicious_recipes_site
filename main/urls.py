"""myssite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.AboutPage, name='aboutpage'),
    path('recipe/new/', views.CreateOrEditRecipe, name='add_recipe'),
    path('recipe/<int:pk>/edit/', views.CreateOrEditRecipe, name ='edit_recipe'),
    path('recepies/', views.AllRecipes, name='all_recipes'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='detail_recipe'),
    path('recipe/search/results', views.SearchRecipe, name='search_recipe'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
