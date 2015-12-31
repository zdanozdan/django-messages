from django.utils.translation import ugettext_lazy as _
from endu.filters import SmartCharFilter
from django_messages.models import Message
from endu.factory import EnduFilterSet

class MessagesFilter(EnduFilterSet):
    sender = SmartCharFilter(name="sender__username",label=_("Sender"))

    class Meta:
        model = Message

