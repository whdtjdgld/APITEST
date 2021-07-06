from django.db import models

# Create your models here.
class quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()
    image = models.ImageField(upload_to="%Y/%m/%d") # 저장경로가 년/ 월/ 일 디렉토리로

class comment(models.Model):
    text = models.CharField(max_length=200)
    post = models.ForeignKey('quiz', verbose_name="comments", on_delete=models.CASCADE, blank=True)
    