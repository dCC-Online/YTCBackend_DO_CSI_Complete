from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments_for_video(request, video_id):
    comments = Comment.objects.select_related('user').filter(video_id=video_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def replies(request, comment_id):
    if request.method == 'POST':
        temp_data = request.data
        temp_data['comment'] = comment_id
        serializer = ReplySerializer(data=temp_data)
        if serializer.is_valid():
            serializer.save(comment_id=comment_id, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        replies = Reply.objects.select_related('user').filter(comment_id=comment_id)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data)