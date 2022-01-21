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