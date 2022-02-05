from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.details, name='details'),
]
