# from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from swampdragon_auth.mixin import TokenAuthMixin

from .models import Notification
from .serializers import NotificationSerializer


class NotificationRouter(TokenAuthMixin, ModelPubRouter):
    valid_verbs = ['subscribe']
    route_name = 'notification'
    model = Notification
    serializer_class = NotificationSerializer
    include_related = []

    # @login_required
    # def subscribe(self, **kwargs):
    #     super().subscribe(**kwargs)
    #
    # def get_subscription_contexts(self, **kwargs):
    #     return {'user_id': self.connection.user.pk}


route_handler.register(NotificationRouter)
