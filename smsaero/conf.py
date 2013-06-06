# -*- coding: utf-8 -*-

from django.conf import settings

SMSAERO_USER = getattr(settings, 'SMSAERO_USER', '')
SMSAERO_PASSWORD = getattr(settings, 'SMSAERO_PASSWORD', '')
SMSAERO_PASSWORD_MD5 = getattr(settings, 'SMSAERO_PASSWORD_MD5', '')
