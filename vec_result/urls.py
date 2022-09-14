from django.urls import path
from . import views

urlpatterns = [
    path('apiOverView/', views.ApiOverView.as_view()),
    path('results/IT/', views.PinkItTable.as_view()),
    path('results/IT/<int:pk>/', views.UpdateView.as_view()),


]
