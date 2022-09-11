from django.urls import path
from . import views

urlpatterns = [
    path('apiOverView/', views.apiOverView, name='apiOverView'),
    path('results/IT/', views.getResultsIT, name='results'),
    path('result/IT/<int:pk>/', views.getResultIT, name='result')
]
