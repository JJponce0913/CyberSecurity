import requests

url = 'http://guppy.utctf.live:7884/'

# GET Method
response_get = requests.get(url)
print(f'GET Response Code: {response_get.status_code}')

# POST Method
response_post = requests.post(url, data={'data': 'example'})
print(f'POST Response Code: {response_post.status_code}')

# PUT Method
response_put = requests.put(url, data={'data': 'example'})
print(f'PUT Response Code: {response_put.status_code}')

# DELETE Method
response_delete = requests.delete(url)
print(f'DELETE Response Code: {response_delete.status_code}')

# PATCH Method
response_patch = requests.patch(url, data={'data': 'example'})
print(f'PATCH Response Code: {response_patch.status_code}')

# HEAD Method
response_head = requests.head(url)
print(f'HEAD Response Code: {response_head.status_code}')

# OPTIONS Method
response_options = requests.options(url)
print(f'OPTIONS Response Code: {response_options.status_code}')

# TRACE Method
response_trace = requests.request('TRACE', url)
print(f'TRACE Response Code: {response_trace.status_code}')

# CONNECT Method
# Note: CONNECT method may not work with requests library as it is typically used for tunneling HTTPS connections
# response_connect = requests.request('CONNECT', url)

# LOCK Method (WebDAV)
response_lock = requests.request('LOCK', url)
print(f'LOCK Response Code: {response_lock.status_code}')

# UNLOCK Method (WebDAV)
response_unlock = requests.request('UNLOCK', url)
print(f'UNLOCK Response Code: {response_unlock.status_code}')

# COPY Method (WebDAV)
response_copy = requests.request('COPY', url, headers={'Destination': f'{url}new-resource'})
print(f'COPY Response Code: {response_copy.status_code}')

# MOVE Method (WebDAV)
response_move = requests.request('MOVE', url, headers={'Destination': f'{url}new-resource'})
print(f'MOVE Response Code: {response_move.status_code}')

# MKCOL Method (WebDAV)
response_mkcol = requests.request('MKCOL', f'{url}new-collection')
print(f'MKCOL Response Code: {response_mkcol.status_code}')

# PROPFIND Method (WebDAV)
response_propfind = requests.request('PROPFIND', url, headers={'Depth': '1'})
print(f'PROPFIND Response Code: {response_propfind.status_code}')

# PROPPATCH Method (WebDAV)
response_proppatch = requests.request('PROPPATCH', url, data={'property': 'value'})
print(f'PROPPATCH Response Code: {response_proppatch.status_code}')

# SEARCH Method
response_search = requests.request('SEARCH', url, data={'query': 'searchterm'})
print(f'SEARCH Response Code: {response_search.status_code}')
