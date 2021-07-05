from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import quiz
from .serializers import QuizSerializer
import random

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