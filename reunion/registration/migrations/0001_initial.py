# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'registration_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'registration', ['Location'])

        # Adding model 'Reunion'
        db.create_table(u'registration_reunion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reunions', to=orm['registration.Location'])),
        ))
        db.send_create_signal(u'registration', ['Reunion'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'registration_location')

        # Deleting model 'Reunion'
        db.delete_table(u'registration_reunion')


    models = {
        u'registration.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'registration.reunion': {
            'Meta': {'object_name': 'Reunion'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reunions'", 'to': u"orm['registration.Location']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['registration']