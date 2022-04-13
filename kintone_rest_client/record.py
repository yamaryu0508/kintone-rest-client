import copy

class Record(object):
  def __init__(self, client):
    self.client = client

  def add_record(self, params):
    return self.client.request(
      path='/k/v1/record',
      method='POST',
      params=params
    )

  def add_records(self, params):
    return self.client.request(
      path='/k/v1/records',
      method='POST',
      params=params
    )

  def update_record(self, params):
    return self.client.request(
      path='/k/v1/record',
      method='PUT',
      params=params
    )

  def update_records(self, params):
    return self.client.request(
      path='/k/v1/records',
      method='PUT',
      params=params
    )

  def get_all_records_with_id(self, params, last_record_id=0, data=None):
    if data == None:
      data = {'records':[]}

    query = '$id > {} order by $id asc limit {}'.format(last_record_id, 500)
    if 'condition' in params and len(params['condition']) > 0:
      query = '{} and {}'.format(params['condition'], query)

    body = {
      'app': params['app'],
      'query': query
    }

    if 'fields' in params:
      body['fields'] = params['fields']
      if '$id' not in body['fields']:
        body['fields'].append('$id')

    response = self.client.request(
      path='/k/v1/records',
      method='GET',
      params=body
    )

    data['records'].extend(response['records'])
    if len(response['records']) != 500:
      return data
    else:
      return self.get_all_records_with_id(
        params=params,
        last_record_id=int(response['records'][-1]['$id']['value']),
        data=data
      )

  def add_all_records(self, params):
    data = {'ids':[], 'revisions':[]}

    loop_size = 100
    start = 0
    end = loop_size

    while True:
      _params = copy.deepcopy(params)
      records = params['records'][start:end]
      _params['records'] = records
      r = self.add_records(_params)
      data['ids'].extend(r['ids'])
      data['revisions'].extend(r['revisions'])

      if len(records) < 100:
        break
      start = start + loop_size
      end = end + loop_size
    return data

  def update_all_records(self, params):
    data = {'records':[]}

    loop_size = 100
    start = 0
    end = loop_size

    while True:
      _params = copy.deepcopy(params)
      records = params['records'][start:end]
      _params['records'] = records
      r = self.update_records(_params)
      data['records'].extend(r['records'])

      if len(records) < 100:
        break
      start = start + loop_size
      end = end + loop_size
    return data