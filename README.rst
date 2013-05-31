=====
Dajngo SMS Aero
=====

Simple Django application for send SMS via smsaero.ru

=====
Quick start
=====

1. Add "smsaero" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
            ...
            'smsaero',
      )

2. Define SMSAERO_USER and SMSAERO_PASSWORD (raw password) or SMSAERO_PASSWORD_MD5 (hash of password) at settings.py::

      SMSAERO_USER = 'username'
      SMSAERO_PASSWORD = '123'
      # or
      SMSAERO_PASSWORD_MD5 = '202cb962ac59075b964b07152d234b70'


3. Run ```python manage.py syncdb``` to create the smsaero models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a smsaero (you'll need the Admin app enabled).

=====
Usage
=====

Send SMS, check the SMS status, get account balance and get signatures::

      from smsaero.urils import send_sms
      from smsaero.urils import get_sms_status
      from smsaero.urils import get_balance
      from smsaero.urils import get_signatures_name
      from smsaero.models import SMSMessage
      
      # Send SMS
      sms = send_sms('79998881122', 'Some text...') # sms has SMSMessage type
      print sms.sms_id # id of accepted message
      print sms.get_status_display() # status
      
      # Check SMS status
      status = get_sms_status(sms.sms_id) # returned string
      
      # Get balance of accaunt
      print get_balance() # returned the rubbles
      
      # Get array of signature names
      print get_signatures_name() # Array of string

Async send SMS::

      from smsaero.urils import send_sms_async
      from smsaero.urils import get_sms_status_async
      from smsaero.urils import get_balance_async
      from smsaero.urils import get_signatures_name_async
      from smsaero.models import SMSMessage

      # Send SMS
      job = send_sms_async('79998881122', 'Some text...')
      job.result # result has SMSMessage type

      job = get_sms_status_async(sms.sms_id)
      job.result # return string

      job = get_balance_asunc()
      job.result # returned the rubbles

      job = get_signatures_name()
      job.result # Array of string
