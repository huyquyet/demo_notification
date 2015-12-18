from django.contrib.auth.models import User
from django.db import models
from swampdragon.models import SelfPublishModel

from .serializers import NotificationSerializer


class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    name = models.TextField(default=None)
