from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:character_id>/', views.character_page, name='character_page'),
    path('character_creation', views.character_creation, name='character_creation'),
]