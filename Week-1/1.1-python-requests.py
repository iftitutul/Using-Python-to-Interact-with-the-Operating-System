#!/usr/bin/env python3.6
# https://pypi.org/project/requests/

import requests
respone = requests.get("https://www.google.com")
print (f'Length of URL: {len(respone.text)}')
print(f'Response code: {respone.status_code}')

"Gmail" in respone.content

