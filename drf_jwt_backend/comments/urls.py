from django.urls import path
from .views import get_comments_for_video, post_comment, replies, update_comment

urlpatterns = [
    path('<str:video_id>/', get_comments_for_video),
    path('', post_comment),
    path('<int:comment_id>/update/', update_comment),
    path('<int:comment_id>/replies/', replies),
]
