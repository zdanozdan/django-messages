from django.utils.translation import gettext_lazy as _

from django_messages.models import Message
from endu.factory import EnduFilterSet
from endu.filters import SmartCharFilter


class MessagesFilter(EnduFilterSet):
    sender = SmartCharFilter(field_name="sender__username",label=_("Sender"))

    class Meta:
        model = Message

