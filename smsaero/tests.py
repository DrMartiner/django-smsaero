# -*- coding: utf-8 -*-

from mock import patch
from hashlib import md5
from django.test import TestCase
from .utils import SmsSender
from django.test.utils import override_settings
from django.conf import settings
from .utils import send_sms
from .utils import get_sms_status
from .utils import get_balance
from .utils import get_signatures_name
from .models import Signature
from .models import SMSMessage
from .factoey import SignatureF


class SmsSenderTest(TestCase):
    def test_send_request(self):
        sender = SmsSender()
        sender.URL = 'foo.bar'
        status = sender.send_request('', {})
        self.assertEqual(status, SMSMessage.STATUS_CONNECTION)

    @patch('smsaero.conf.SMSAERO_PASSWORD', 'FAKE')
    @patch('smsaero.conf.SMSAERO_PASSWORD_MD5', '')
    def test_get_encrypted_password(self):
        sender = SmsSender()
        hashed = sender._get_password()

        m = md5()
        m.update('FAKE')
        passord = m.hexdigest()

        self.assertEqual(hashed, passord, 'Encrypted pass not equal with MD5 hash')

    @patch('smsaero.conf.SMSAERO_PASSWORD_MD5', 'md5_hash')
    def test_get_no_encrypted_password(self):
        sender = SmsSender()
        hashed = sender._get_password()
        self.assertEqual(hashed, 'md5_hash', 'MD5 hash of password not equal')

    def test_parse_response_key_val(self):
        sender = SmsSender()
        key, val = sender.parse_response('key=val')

        self.assertEqual(key, 'key', 'Did not parse key from response')
        self.assertEqual(val, 'val', 'Did not parse value from response')

    def test_parse_response_key_only(self):
        sender = SmsSender()
        key, stuff = sender.parse_response('key')

        self.assertEqual(key, 'key', 'Did not parse key from response')
        self.assertIsNone(stuff, 'Value is not empty at parse of response without "="')

    def test_get_signature_by_id(self):
        sign = SignatureF()
        sign.save()
        sender = SmsSender()

        signature = sender.get_signature(sign.id)

        self.assertEqual(signature.id, sign.id)

    def test_get_first_signature(self):
        sign = SignatureF()
        sign.save()
        sender = SmsSender()

        signature = sender.get_signature()

        self.assertEqual(signature.id, sign.id)


class SmsAeroAPITest(TestCase):
    def test_send_sms(self):
        pass

    def test_get_sms_status(self):
        pass

    def test_get_balance(self):
        pass

    def test_get_signatures_name(self):
        pass
