# -*- coding: utf-8 -*-

from django.db import models


class Signature(models.Model):
    name = models.CharField('Имя', max_length=128)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подпись'
        verbose_name_plural = 'Подписи сообщений'


class SMSMessage(models.Model):
    STATUS_CONNECTION = 'connection error'
    STATUS_ACCEPTED = 'accepted'
    STATUS_EMPTY_FIELD = 'empty field. reject.'
    STATUS_INCORRECT_USER = 'incorrect user or password. reject'
    STATUS_NO_CREDITS = 'no credits'
    STATUS_INCORRECT_NAME = 'incorrect sender name. reject'
    STATUS_INCORRECT_ADRESS = 'incorrect destination adress. reject'
    STATUS_INCORRECT_DATE = 'incorrect date. reject'
    STATUS_DELIVERY_SUCCESS = 'delivery success'
    STATUS_DELIVERY_FAILURE = 'delivery failure'
    STATUS_SMSC_SUBMIT = 'smsc submit'
    STATUS_SMSC_REJECT = 'smsc reject'
    STATUS_QUEUE = 'queue'
    STATUS_WAIT_STATUS = 'wait status'
    STATUS_INCORRECT_ID = 'incorrect id. reject'

    STATUS_CHOICES = (
        (STATUS_CONNECTION, 'Ошибка при соединение с сервером'),
        (STATUS_ACCEPTED, 'Сообщение принято сервисом'),
        (STATUS_EMPTY_FIELD, 'Не все обязательные поля заполнены'),
        (STATUS_INCORRECT_USER, 'Ошибка авторизации'),
        (STATUS_NO_CREDITS, ' 	Недостаточно SMS на балансе'),
        (STATUS_INCORRECT_NAME, 'Неверная (незарегистрированная) подпись отправителя'),
        (STATUS_INCORRECT_ADRESS, 'Неверно задан номер тефона (формат 71234567890)'),
        (STATUS_INCORRECT_DATE, 'Неправильный формат дат'),
        (STATUS_DELIVERY_SUCCESS, 'Сообщение доставлено'),
        (STATUS_DELIVERY_FAILURE, 'Ошибка доставки SMS'),
        (STATUS_SMSC_SUBMIT, 'Сообщение доставлено в SMSC'),
        (STATUS_SMSC_REJECT, 'Отвергнуто SMSC'),
        (STATUS_QUEUE, ' 	Ожидает отправки'),
        (STATUS_WAIT_STATUS, 'Ожидание статуса (запросите позднее)'),
        (STATUS_INCORRECT_ID, 'Неверный идентификатор сообщения'),
    )

    phone = models.CharField('Телефон', max_length=10) # TODO: realise phone num validator
    signature = models.ForeignKey(Signature, verbose_name='Подпись')
    text = models.TextField('Текст')
    sms_id = models.IntegerField('ID SMS', db_index=True, blank=True, null=True, editable=False)
    status = models.CharField('Статус', max_length=128)
    created = models.DateTimeField('Создано', auto_created=True)

    def __unicode__(self):
        return '{0} <{1}>'.format(self.phone, self.get_status_display())

    class Meta:
        ordering = ('created', )
        verbose_name = 'Сообщение'
        verbose_name_plural = 'SMS сообщения'