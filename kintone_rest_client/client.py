import base64
import logging
import os
from urllib.parse import urlparse

from simple_http_client import Client as HTTPClient, FormData, HTTPError

from .record import Record
from .file import File
from .version import __version__

logger = logging.getLogger(__name__)

class Client(object):
  def __init__(
    self,
    base_url=None,
    auth=None,
    guest_space_id=None,
    user_agent=None
  ):
    self.base_url =  base_url or os.environ.get('KINTONE_BASE_URL')
    self.auth = auth
    self.guest_space_id = guest_space_id
    self.user_agent = user_agent
    self.version = __version__

  def _build_user_agent(self):
    if self.user_agent == None:
      return '{}{}{}'.format('kintone_rest_client/', self.version, ';python')
    else:
      return self.user_agent

  def create_url(self, path):
    if 'json' not in path:
      path = '{}.json'.format(path)
    if self.guest_space_id is None:
      url = '{}{}'.format(self.base_url, path)
    else:
      path = path.split('/k')
      path[0] = '/k/guest/'
      url = '{}{}{}{}'.format(self.base_url, path[0], self.guest_space_id, path[1])
    return url

  def _build_auth_token(
    self,
    username,
    password,
  ):
    return base64.b64encode((
      '{}:{}'.format(
        username,
        password
      )
    ).encode()).decode()

  def _build_auth_header(self):
    headers = {}
    username = self.auth['username'] or os.environ.get('KINTONE_USERNAME')
    password = self.auth['password'] or os.environ.get('KINTONE_PASSWORD')
    if 'api_token' in self.auth:
      headers.update({'X-Cybozu-API-Token': self.auth['api_token']})
    if 'bearer_token' in self.auth:
      headers.update({'Authorization': 'Bearer {}'.format(self.auth['bearer_token'])})
    if username and password:
      auth_token = self._build_auth_token(username, password)
      headers.update({'X-Cybozu-Authorization': auth_token})
    return headers

  def request(self, path='/k/v1/records', method='GET', params=None):
    client = HTTPClient()
    url = self.create_url(path)
    parsed_url = urlparse(url)

    headers = self._build_auth_header()
    headers.update({'X-HTTP-Method-Override': method})
    headers.update({'User-Agent': self._build_user_agent()})
    response = client.request(
      url='{}://{}{}'.format(parsed_url.scheme, parsed_url.netloc, parsed_url.path),
      method='POST',
      headers=headers,
      body=params
    )
    if method == 'GET' and 'file' in path:
      return {'data': response.body}
    return response.to_dict

  @property
  def Record(self):
    return Record(self)

  @property
  def File(self):
    return File(self)