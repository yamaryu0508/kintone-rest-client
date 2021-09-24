import os

from simple_http_client import FormData

class File(object):
  def __init__(self, client):
    self.client = client

  def upload_file(self, params):
    file = params['file']
    form = FormData()
    name = None
    if 'name' in file and 'data' in file:
      name = file['name']
      data = file['data']
    elif 'path' in file:
      path = file['path']
      name = os.path.basename(path)
      with open(path, 'rb') as f:
        data = f.read()

    form.add_file(
      'file',
      name,
      data
    )
    return self.client.request(
      path='/k/v1/file',
      method='POST',
      params=form
    )

  def download_file(self, params):
    return self.client.request(
      path='/k/v1/file',
      method='GET',
      params=params
    )