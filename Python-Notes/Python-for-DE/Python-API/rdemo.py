import requests

# We are trying to get the contant from the web browser by using requests

# payload = {'page': 2, 'count':25}
payload = {'username': 'vaibhav', 'password': 'testing'}
r = requests.post('https://httpbin.org/get', data=payload)

# Use text for getting website HTMl Code
## print(r.text)

# Now we are printing / saving the image of that website Using Content
"""
with open('comic.png','wb') as f:
    f.write(r.content)

"""

# by the use of status_code we can know what is the HTML Code

## print(r.status_code)

## print(r.ok) # It Give the True Value on the bases of status_code is greater than 400
            # 400 is server error
            # 500 is client error

# print(r.url)

# we can also use json format
# print(r.json())







