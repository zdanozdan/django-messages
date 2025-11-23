import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from ...models import Message


class Command(BaseCommand):
    help = (
        'Deletes all system notif messages'
    )

    def handle(self, *args, **options):
        Message.objects.filter(
            notif_type=Message.RESULTS_NOTIF,
        ).delete()
