"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from quickstart import views
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# router url을 자동으로 맵핑
router = routers.DefaultRouter()
router.register(r'quizs', views.QuizViewset)
router.register(r'comments', views.CommentViewset)

# 2.0 이후로는 url 보다는 path 거는게 많다 알도록
# app 내 url 연동하는 곳
urlpatterns = [
    path('admin/', admin.site.urls),
    path('quizs/', include('quickstart.urls')), # ~ quizs/ app내 urls 따라감 -> views 함수 호출
    url(r'^', include(router.urls)), # localhost:8000 일때 router.urls
    url(r"^api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# MEDIA_URL 에 대한 요청이 왔을 때 MEDIA_ROOT 에서 일을 처리하게된다.


