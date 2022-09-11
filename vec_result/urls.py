from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('apiOverView/', views.ApiOverView.as_view()),
    path('results/IT/', views.PinkItTable.as_view()),
    path('result/IT/<int:pk>/', views.UpdateView.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
