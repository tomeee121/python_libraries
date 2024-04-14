import requests

payload = {
    "name": "Mike",
    "age": 25
}
response = requests.post('https://httpbin.org/post', data=payload)
print(response.json())

response = requests.get('https://httpbin.org/status/404')
if response.status_code == requests.codes.not_found:
    print('not found')
else:
    print(response.status_code)





headers = {
    'Accept': 'image/jpeg'
}
resp = requests.get('https://httpbin.org/image', headers=headers)
with open('myimage.jpg', 'wb') as f:
    f.write(resp.content)

def print_url(r, **kwargs):
    print(r.url)
requests.get('https://httpbin.org/get', hooks=dict(response=print_url))
