from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Shoutout(models.Model):
    recipient = models.ForeignKey(
        User, related_name="shoutouts_received", on_delete=models.PROTECT
    )
    content = models.TextField()
    datetime = models.DateTimeField()
    user = models.ForeignKey(
        User, related_name="shoutouts_given", on_delete=models.PROTECT
    )
    likes = models.IntegerField()

class ShoutoutLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.IntegerField()