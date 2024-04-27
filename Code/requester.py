import requests

url = 'http://chals.swampctf.com:64550/api/braille.php'
for i in range(255):
    payload = {'searchText': chr(i)}
    print(str(i)+":")
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Check for any HTTP errors
        print('Response:', response.text)
    except requests.exceptions.RequestException as e:
        print('Error:', e)
