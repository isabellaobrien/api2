from django.urls import path
from reply_likes import views

urlpatterns = [
    path('reply_likes/', views.ReplyLikeList.as_view()),
    path('reply_likes/<int:pk>/', views.ReplyLikeDetail.as_view()),
]