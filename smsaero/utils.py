# -*- coding: utf-8 -*-

import logging
import urllib2
from hashlib import md5
from urllib import quote_plus
from django.utils.html import strip_tags
from smsaero import conf as settings
from models import Signature
from models import SMSMessage

logger = logging.getLogger('smsaero')


class SmsSender():
    PROTOCOL = 'http'
    HOST = 'gate.smsaero.ru'

    def send_request(self, link, params):
        params['user'] = settings.SMSAERO_USER
        params['password'] = self._get_password()

        url = '%s://%s%s?%s' % (
            self.PROTOCOL,
            self.HOST,
            link,
            '&'.join('%s=%s' % i for i in params.items()),
        )
        try:
            response = urllib2.urlopen(url)
            return strip_tags(response.read()).strip()
        except urllib2.URLError:
            logger.error('connection error', exc_info=True)
            return 'connection error'
        except urllib2.HTTPErrorProcessor:
            logger.error('connection error', exc_info=True)
            return 'connection error'

    def _get_password(self):
        if settings.SMSAERO_PASSWORD_MD5:
            return settings.SMSAERO_PASSWORD_MD5

        m = md5()
        m.update(settings.SMSAERO_PASSWORD)
        return m.hexdigest()

    def parse_response(self, response):
        if '=' in response:
            return response.split('=')
        return response, None

    def get_signature(self, signature_id=None):
        if signature_id:
            return Signature.objects.get(pk=signature_id)
        else:
            return Signature.objects.all()[0]


sender = SmsSender()


def send_sms(to, text, signature_id=None, date=None, link='/send/'):
    signature = sender.get_signature(signature_id)
    params = {
        'to': to,
        'text': quote_plus(text),
        'from': signature.name,
        'date': date or '',
    }
    response = sender.send_request(link, params)
    sms_id, status = sender.parse_response(response)

    if not sms_id or not status:
        msg = 'Can not send SMS to %s. Status: %s' % (to, sms_id)
        logger.error(msg)
        raise Exception(msg)

    sms = SMSMessage(
        phone=to,
        signature=signature,
        text=text,
        sms_id=sms_id,
        status=status,
    )
    sms.save()
    return sms


def get_sms_status(sms_id, link='/status/'):
    response = sender.send_request({'id': sms_id}, link)
    status, sms_id = sender.parse_response(response)
    return status


def get_balance(link='/balance/'):
    response = sender.send_request({}, link)
    stuff, balanse = sender.parse_response(response)
    return balanse


def get_signatures_name(link='/senders/'):
    response = sender.send_request({}, link)
    return [n for n in response.split('\n') if n]