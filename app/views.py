from rest_framework import viewsets
from .models import TweetModel
from .serializer import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = TweetModel.objects.all()  # 全てのデータを取得
    serializer_class = TweetSerializer
