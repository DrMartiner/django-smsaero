# -*- coding: utf-8 -*-

import urllib2
from hashlib import md5
from urllib import quote_plus, urlencode
import conf as settings
from models import Signature
from models import SMSMessage


class SmsSender():
    PROTOCOL = 'http'
    URL = 'gate.smsaero.ru'

    def send_request(self, link, params):
        params['user'] = settings.SMSAERO_USER
        params['password'] = self._get_password()
        url = '%s://%s%s%s' % (
            self.PROTOCOL,
            self.URL,
            quote_plus(link),
            urlencode(params),
        )
        try:
            response = urllib2.urlopen(url)
            return response.read()
        except Exception, e:
            # TODO: use the logger
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
        'text': text,
        'from': signature.name,
        'date': date or '',
    }
    response = sender.send_request(link, params)
    status, sms_id = sender.parse_response(response)

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