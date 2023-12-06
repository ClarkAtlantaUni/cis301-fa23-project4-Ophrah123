#Issue a request, url =
import requests
from flask import json

'''
Methods of http:get,post,put,update,delete
get is used to fetch(search and navigate), post is used to upload(collect forms/upload files)
requests has the ability to format data, submit payloads, understand cookies
when you use post: using json is common/to submit form data/diff type of information
'''
def get_example():
    url = "http://localhost:5000/sample_phonecall"
    headers ={'content-type':'text/html'}
    res = requests.get(url = url,headers=headers)
    print(f"text:{res.text}\n")
    print(f"text:{res.content}\n")

def post_examples():
    url = "http://localhost:5000/auth"
    headers = {'content-type': 'application/json'}
    data={"username":"admin", "password":"fall2023"}
    res = requests.post(url, data=json.dumps(data), headers = headers)
    print(f"text:{res.text}\n")
    print(f"text:{res.content}\n")

def authenticate():
    url = "http://localhost:5000/auth"
    headers = {'content-type': 'application/json'}
    data = {"username": "admin", "password": "fall2023"}
    res = requests.post(url, data=json.dumps(data), headers=headers)
    print(f"text:{res.text}\n")
    print(f"text:{res.content}\n")
    return res
def search_byname():
    search_query = input("Enter a name: ")
    url = "http://localhost:5000/auth"
    headers = {'content-type': 'application/json'}
    data = {"username": "admin", "password": "fall2023"}
    res = requests.post(url, data=json.dumps(data), headers=headers)
    url = "http://localhost:5000/search"+"?name"+search_query

    res=requests.get(url,cookies=res.cookies,headers=headers)
    print(res.content)

if __name__ =='__main__':
    # print(authenticate())
    # post_examples()
    print(search_byname())
