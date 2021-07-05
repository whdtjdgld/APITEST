from rest_framework import serializers
from .models import quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiz
        fields = ('title', 'body', 'answer')
