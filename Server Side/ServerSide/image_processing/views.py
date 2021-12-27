from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer
from .test import Comment

# Create your views here.

@api_view(['GET','POST'])
def comment_view(request):
    message_obj = Comment("abc","def")
    serializer_class = CommentSerializer(message_obj)
    return Response(serializer_class.data)


