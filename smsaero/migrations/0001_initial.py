# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Signature'
        db.create_table(u'smsaero_signature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'smsaero', ['Signature'])

        # Adding model 'SMSMessage'
        db.create_table(u'smsaero_smsmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('signature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['smsaero.Signature'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('sms_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'smsaero', ['SMSMessage'])


    def backwards(self, orm):
        # Deleting model 'Signature'
        db.delete_table(u'smsaero_signature')

        # Deleting model 'SMSMessage'
        db.delete_table(u'smsaero_smsmessage')


    models = {
        u'smsaero.signature': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Signature'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'smsaero.smsmessage': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'SMSMessage'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'signature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['smsaero.Signature']"}),
            'sms_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['smsaero']