import io
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
    self.file_path = './logo.png'
    self.file_key = '2020081218343959F509DDF4924446B6843F359CFA57BB005'

  def test_upload_file_with_path_ok(self):
    kintone = self.kintone
    params={
      'file': {
        'path': self.file_path
      }
    }
    response = kintone.File.upload_file(params)
    self.assertIn('fileKey', response)

    return

  def test_upload_file_with_data_ok(self):
    kintone = self.kintone
    params={
      'file': {
        'name': 'hello.txt',
        'data': io.BytesIO(b'Hello, Python Kintone developer').read()
      }
    }
    response = kintone.File.upload_file(params)
    self.assertIn('fileKey', response)

    return

  def test_download_file_ok(self):
    kintone = self.kintone
    params={
      'fileKey': self.file_key
    }
    response = kintone.File.download_file(params)
    self.assertIn('data', response)

    return

if __name__ == '__main__':
  unittest.main(verbosity=2)