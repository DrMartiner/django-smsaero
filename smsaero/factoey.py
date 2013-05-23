# -*- coding: utf-8 -*-

import factory
from .models import Signature
from .models import SMSMessage


class SignatureF(factory.Factory):
    FACTORY_FOR = Signature

    # id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'Name{0}'.format(n))


class SMSMessageF(factory.Factory):
    FACTORY_FOR = SMSMessage

    # id = factory.Sequence(lambda n: n)
    phone = factory.Sequence(lambda n: '7123456789{0}'.format(n))
    signature = factory.LazyAttribute(lambda a: SignatureF())
    text = factory.Sequence(lambda n: 'Message{0}'.format(n))
    status = SMSMessage.STATUS_CONNECTION