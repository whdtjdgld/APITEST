from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import comment, quiz
from .serializers import CommentSerializer, QuizSerializer
import random
from rest_framework import viewsets

# urls 에서 넘어와 api에 보여지는  views

@api_view(['GET']) # HELLO API 는 get 메소드로
def helloAPI(request):
    return Response("Hello World")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True) # many=T 다수 데이터도 직렬화
    return Response(serializer.data)

class QuizViewset(viewsets.ModelViewSet):
    queryset = quiz.objects.all()
    serializer_class = QuizSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer