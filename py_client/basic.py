import requests

# endpoint = "http://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"Hello World"}) #API -> HTTP Request  || REST APIs -> Web APIs

# print(get_response.text) # print raw text response

# print(get_response.json()) # print json response

print(get_response.status_code)
