# To make POST, PUT, PATCH, DELETE requests

import requests

def get_requests(url,auth,in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response

