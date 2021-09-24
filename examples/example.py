import io
import logging
import os

from kintone_rest_client import Client

logging.basicConfig(level=logging.ERROR)
logging.getLogger('simple_http_client').setLevel(level=logging.DEBUG)

kintone = Client(
  base_url=os.environ.get('KINTONE_BASE_URL'),
  auth={
    'username': os.environ.get('KINTONE_USERNAME'),
    'password': os.environ.get('KINTONE_PASSWORD')
  }
)

app = 759
record_id = 20
file_key = '20210924194537F38439049CD548A890C30A4428C78675148'

try:
  response = kintone.request(params={
    'app': app
  })
  print(response)
except Exception as e:
  print(e.to_dict)

try:
  response = kintone.Record.add_record({
    'app': app,
    'record': {
      'Company_Name': {
        'value': 'Cybozu Inc.,'
      }
    }
  })
  print(response)
except Exception as e:
  print(e.body)

try:
  response = kintone.Record.add_records({
    'app': app,
    'records': [{
      'Company_Name': {
        'value': 'Cybozu Inc.,'
      }
    }]
  })
  print(response)
except Exception as e:
  print(e.body)

try:
  response = kintone.Record.update_record({
    'app': app,
    'id': record_id,
    'record': {
      'Company_Name': {
        'value': 'Kintone Corporation'
      }
    }
  })
  print(response)
except Exception as e:
  print(e.to_dict)

try:
  response = kintone.Record.update_records({
    'app': app,
    'records': [{
      'id': record_id,
      'record': {
        'Company_Name': {
          'value': 'Kintone Corporation'
        }
      }
    }]
  })
  print(response)
except Exception as e:
  print(e.to_dict)

try:
  response = kintone.Record.get_all_records_with_id({
    'app': app,
    'fields': ['$revision']
  })
  print(response['records'])
except Exception as e:
  print(e.body)

try:
  response = kintone.File.upload_file({
    'file': {
      'path': './logo.png'
    }
  })
  print(response)
except Exception as e:
  print(e.body)

try:
  response = kintone.File.upload_file({
    'file': {
      'name': 'hello.txt',
      'data': io.BytesIO(b'Hello, Python Kintone developer').read()
    }
  })
  print(response)
except Exception as e:
  print(e.body)

try:
  response = kintone.File.download_file({
    'fileKey': file_key
  })
  print(response)
except Exception as e:
  print(e.body)