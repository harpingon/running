# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'runlog_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'runlog', ['Manufacturer'])

        # Adding model 'Shoe'
        db.create_table(u'runlog_shoe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('purchased', self.gf('django.db.models.fields.DateField')()),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['runlog.Manufacturer'])),
        ))
        db.send_create_signal(u'runlog', ['Shoe'])

        # Adding model 'Run'
        db.create_table(u'runlog_run', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rundate', self.gf('django.db.models.fields.DateField')()),
            ('distance', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('calories', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('shoe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['runlog.Shoe'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'runlog', ['Run'])


    def backwards(self, orm):
        # Deleting model 'Manufacturer'
        db.delete_table(u'runlog_manufacturer')

        # Deleting model 'Shoe'
        db.delete_table(u'runlog_shoe')

        # Deleting model 'Run'
        db.delete_table(u'runlog_run')


    models = {
        u'runlog.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'runlog.run': {
            'Meta': {'object_name': 'Run'},
            'calories': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'distance': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rundate': ('django.db.models.fields.DateField', [], {}),
            'shoe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['runlog.Shoe']"})
        },
        u'runlog.shoe': {
            'Meta': {'object_name': 'Shoe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['runlog.Manufacturer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'purchased': ('django.db.models.fields.DateField', [], {}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['runlog']