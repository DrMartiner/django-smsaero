=====
Dajngo SMS Aero
=====

Simple Django application for send SMS via smsaero.ru

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "smsaero" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'smsaero',
      )

2. Run `python manage.py syncdb` to create the smsaero models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a smsaero (you'll need the Admin app enabled).

Usage
-----

from smsaero.urils import send_sms
from smsaero.urils import get_sms_status
from smsaero.urils import get_balance
from smsaero.urils import get_signatures_name
