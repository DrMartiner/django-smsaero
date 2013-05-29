# -*- coding: utf-8 -*-

from mock import patch
from hashlib import md5
from django.test import TestCase
from .utils import SmsSender
from .utils import send_sms
from .models import SMSMessage
from .factoey import SignatureF
from .factoey import SMSMessageF


class SmsSenderTest(TestCase):
    def _fake_urlopen(self):
        class FakeStreamReader(object):
            def read(self):
                return '123=accepted'
        return FakeStreamReader()

    @patch('smsaero.conf.SMSAERO_PASSWORD', 'FAKE')
    @patch('urllib2.urlopen', _fake_urlopen)
    def test_send_request(self):
        sender = SmsSender()
        response = sender.send_request('/link/', {})
        self.assertIn(SMSMessage.STATUS_ACCEPTED, response)

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
    def _get_sms(self, to, text):
        return '0=accepted'

    @patch('smsaero.utils.SmsSender.send_request', _get_sms)
    def test_send_sms(self):
        signature = SignatureF()
        signature.save()

        sent_sms = send_sms('71234567890', 'Message0')
        sms = SMSMessageF()

        self.assertEquals(sent_sms.phone, sms.phone, 'Not equals phone of sent SMS')
        self.assertEquals(sent_sms.text, sms.text, 'Not equals text of sent SMS')
        self.assertEquals(sent_sms.sms_id, str(sms.sms_id), 'Not equals SMS ID in response')
        self.assertEquals(sent_sms.status, SMSMessage.STATUS_ACCEPTED, 'Status of sent SMS is not ACCEPTED')
        self.assertEquals(sent_sms.signature, signature, 'Not equals signature of sent SMS')

    def test_get_sms_status(self):
        pass

    def test_get_balance(self):
        pass

    def test_get_signatures_name(self):
        pass
