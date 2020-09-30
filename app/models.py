from django.db import models


class TweetModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tweet = models.CharField(max_length=200)


