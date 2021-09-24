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

  def test__build_user_agent(self):
    kintone = self.kintone
    user_agent = kintone._build_user_agent()
    self.assertIn('kintone_rest_client', user_agent)

    return

if __name__ == '__main__':
  unittest.main(verbosity=2)