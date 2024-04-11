import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
#endpoint = "http://localhost:8000/" # http://127.0.0.1:8000/
endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={"title": "ABC123","content": "Hello World", "price": "123"}) #API -> HTTP Request  || REST APIs -> Web APIs

#print(get_response.headers)
#print(get_response.text) # print raw text response
print(get_response.json()) # print json response
#print(get_response.status_code)
