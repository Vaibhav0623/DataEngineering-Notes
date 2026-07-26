import requests

# Normal Way to use the API

"""
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print('Status-Code:',response.status_code)
print('Content-Type:',response.headers.get("Content-type"))


data = response.json() # parse json into a python dict

print("Post Title:", data["title"])

print(data)
"""

# getting Data From API Using parameters

url = "https://reqres.in/api/users"
params = {"page":2}

response = requests.get(url, params=params)
print("Final Url:",response.url) # shows ?page=2

# response.raise_for_status() # raises error for 4xx/5xx 

data = response.json()
print("Page:", data["page"])
for user in data["data"]:
    print(user["email"])
