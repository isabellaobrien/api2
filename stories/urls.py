from django.urls import path
from stories import views

urlpatterns = [
    path('stories/', views.StoryList.as_view()),
    path('stories/<int:pk>/', views.StoryDetail.as_view()),
]