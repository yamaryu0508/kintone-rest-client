# Kintone REST Client for Python

## Installation

### Prerequisites
- Python version 3.7+

### Install Package
```
pip install git+https://github.com/yamaryu0508/kintone-rest-client
```

## Quick Start
Here is a quick example:
```python
import os
from kintone_rest_client import Client as KintoneRESTClient

kintone = KintoneRESTClient(
  base_url=os.environ.get('KINTONE_BASE_URL'),
  auth={
    'username': os.environ.get('KINTONE_USERNAME'),
    'password': os.environ.get('KINTONE_PASSWORD')
  }
) 

app = 759

params={
  'app': app,
  'fields': ['$revision']
}

try:
  response = kintone.Record.get_all_records_with_id(params)
  print(response)
except Exception as e:
  print(e.to_dict)
```

### Exception class
Exception class is described [here](https://github.com/yamaryu0508/simple-http-client#exception-class).

## Usage
- [Example Code](https://github.com/yamaryu0508/kintone-rest-client/tree/main/examples)

## License
[The MIT License (MIT)](https://github.com/yamaryu0508/kintone-rest-client/blob/main/LICENSE)