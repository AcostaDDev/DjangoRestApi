import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
#endpoint = "http://localhost:8000/" # http://127.0.0.1:8000/
endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/

get_response = requests.get(endpoint, params={"product_id": 123}) #API -> HTTP Request  || REST APIs -> Web APIs

#print(get_response.text) # print raw text response
print(get_response.json()) # print json response
#print(get_response.status_code)
