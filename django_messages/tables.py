import django_tables2 as tables
from django.utils.translation import ugettext_lazy as _

class MessagesTable(tables.Table):
    subject = tables.TemplateColumn(template_name="django_messages/subject_column.html",verbose_name=_('Subject'))
    body = tables.TemplateColumn(template_name="django_messages/body_column.html",verbose_name=_('Body'))
    sent_at = tables.TemplateColumn(template_name="django_messages/received_column.html",verbose_name=_('Received'))
    action = tables.TemplateColumn(template_name="django_messages/action_column.html",verbose_name=_('Action'))

class MessagesTableInbox(MessagesTable):
    sender = tables.TemplateColumn('<a href="{{record.sender.get_absolute_url}}">{{record.sender}}</a>',accessor='sender.username',verbose_name=_('Sender'))

    class Meta:
        sequence = ("sender",)

class MessagesTableOutbox(MessagesTable):
    recipient = tables.TemplateColumn('<a href="{{record.recipient.get_absolute_url}}">{{record.recipient}}</a>',accessor='recipient.username',verbose_name=_('Recipient'))

    class Meta:
        sequence = ("recipient",)

class MessagesTableTrash(MessagesTable):
    action = tables.TemplateColumn(template_name="django_messages/undelete_column.html",verbose_name=_('Action'))

class MessagesTableView(MessagesTableInbox):
    body = tables.Column(verbose_name=_('Body'))

