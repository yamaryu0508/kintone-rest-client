import os
import unittest
from unittest import mock

from kintone_rest_client import Client

class TestClient(unittest.TestCase):

  def setUp(self):
    self.kintone = Client(
      base_url=os.environ.get('KINTONE_BASE_URL'),
      auth={
        'username': os.environ.get('KINTONE_USERNAME'),
        'password': os.environ.get('KINTONE_PASSWORD')
      }
    )
    self.app = 759
    self.record_id = 20
    self.records_len = 150

  def test_add_record_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'record': {
        'Company_Name': {
          'value': 'Cybozu Inc.,'
        }
      }
    }
    response = kintone.Record.add_record(params)
    self.assertIn('id', response)
    self.assertIn('revision', response)

    return

  def test_add_records_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'records': [{
        'Company_Name': {
          'value': 'Cybozu Inc.,'
        }
      }]
    }
    response = kintone.Record.add_records(params)
    self.assertIn('ids', response)
    self.assertIn('revisions', response)
    self.assertEqual(len(response['ids']), 1)
    self.assertEqual(len(response['revisions']), 1)

    return

  def test_add_all_records_ok(self):
    records = []
    for i in range(self.records_len):
      records.append({
        'Company_Name': {
          'value': f'Cybozu Inc., - {i}'
        }
      })
    kintone = self.kintone
    params={
      'app': self.app,
      'records': records
    }
    response = kintone.Record.add_all_records(params)
    self.assertIn('ids', response)
    self.assertIn('revisions', response)
    self.assertEqual(len(response['ids']), self.records_len)
    self.assertEqual(len(set(response['ids'])), self.records_len)
    self.assertEqual(len(response['revisions']), self.records_len)

    return

  def test_update_record_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'id': self.record_id,
      'record': {
        'Company_Name': {
          'value': 'Kintone Corporation'
        }
      }
    }
    response = kintone.Record.update_record(params)
    self.assertIn('revision', response)

    return 

  def test_update_records_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'records': [{
        'id': self.record_id,
        'record': {
          'Company_Name': {
            'value': 'Kintone Corporation'
          }
        }
      }]
    }
    response = kintone.Record.update_records(params)
    self.assertIn('records', response)
    self.assertIn('id', response['records'][0])
    self.assertIn('revision', response['records'][0])

    return

  def test_update_all_records_ok(self):
    kintone = self.kintone
    records = []
    for i in range(self.records_len):
      records.append({
        'id': self.record_id + i,
        'record': {
          'Company_Name': {
            'value': f'Kintone Corporation - {i}'
          }
        }
      })
    params={
      'app': self.app,
      'records': records
    }
    response = kintone.Record.update_all_records(params)
    self.assertIn('records', response)
    self.assertIn('id', response['records'][0])
    self.assertIn('revision', response['records'][0])
    ids = [record['id'] for record in response['records']]
    self.assertEqual(len(set(ids)), self.records_len)

    return 

  def test_get_all_records_with_id_ok(self):
    kintone = self.kintone
    params={
      'app': self.app
    }
    response = kintone.Record.get_all_records_with_id(params)
    self.assertIn('records', response)

    return

  def test_get_all_records_with_id_with_condition_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'condition': '$id=1'
    }
    response = kintone.Record.get_all_records_with_id(params)
    self.assertIn('records', response)

    return

  def test_get_all_records_with_id_with_black_condition_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'condition': ''
    }
    response = kintone.Record.get_all_records_with_id(params)
    self.assertIn('records', response)

    return

  def test_get_all_records_with_id_with_fields_ok(self):
    kintone = self.kintone
    params={
      'app': self.app,
      'fields': ['$id']
    }
    response = kintone.Record.get_all_records_with_id(params)
    self.assertIn('records', response)

    return

if __name__ == '__main__':
  unittest.main(verbosity=2)