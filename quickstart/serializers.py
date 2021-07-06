from rest_framework import serializers
from .models import comment, quiz

# 데이터를 json(가장 보편적), xml등 데이터로 변환
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiz
        fields = ('title', 'body', 'image', 'answer')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'