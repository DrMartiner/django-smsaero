# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Signature
from .models import SMSMessage


class SMSMessageAdmin(admin.ModelAdmin):
    list_display = ('phone', 'status', 'signature', 'sms_id', 'created')
    list_filter = ('signature', 'status', 'created')
    list_display_links = ('signature',)
    search_fields = ('text', 'signature__name')

    can_delete = False

    def has_add_permission(self, request):
        return False

    # TODO: send after saving if selected check


admin.site.register(Signature)
admin.site.register(SMSMessage, SMSMessageAdmin)