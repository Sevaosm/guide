from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_main, name="index_main"),
    path('<int:pk>/', views.index, name="index"),
]