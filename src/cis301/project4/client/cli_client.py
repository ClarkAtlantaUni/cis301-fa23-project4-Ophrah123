#TODO Implement the client application
import json
import sys

import requests

from cis301.project4 import phonecall
from cis301.project4.phonecall import PhoneCall
from cis301.project4.util import Util


class PhoneBillClient():

    def __init__(self, hostname="localhost", port="8000"):
        self.__host = hostname
        self.__port = port
        self.__uname = None
        self.__password = None


    def get_username(self):
        return self.__uname

    def get_password(self):
        return self.__password

    def set_username(self, uname):
         self.__uname = uname

    def set_password(self, passwd):
         self.__password = passwd

    def register_user(self):
        pass

    def add_phonecall(self, phone_call):
        # convert data to JSON
        phonecallJSON = Util.phonecallToJSON(phone_call, True)
        #generate a request
        #every request needs authentication
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email":f"{self.__uname}", "password":f"{self.__password}", "client":True}

        headers={'content-type':'application/json',}
        auth_res = requests.post( url, data=json.dumps(data), headers= headers )

        # check response
        print( auth_res )
        print( auth_res.text )
        # send request (POST)
        url = 'http://'+self.__host+':'+self.__port+'/user/add'
        res = requests.post(url, data=json.dumps(phonecallJSON), cookies=auth_res.cookies,headers=headers )

        #check response
        print(res)
        print( res.text )#\
    def delete_phonecall(self,phone_call_id):
        data = dict()
        data["client"]=True
        data["phone_call_id"] = True
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email": f"{self.__uname}", "password": f"{self.__password}", "client": True}

        headers = {'content-type': 'application/json', }
        auth_res = requests.post(url, data=json.dumps(data), headers=headers)

        # check response
        print(auth_res)
        print(auth_res.text)
        # send request (POST)
        url = 'http://' + self.__host + ':' + self.__port + '/user/del'
        res = requests.post(url, data=json.dumps(data), cookies=auth_res.cookies, headers=headers)
        res = json.loads(res.text)['res']
        if res =="200":
            print((f"Phone Call {phone_call_id} deleted!\n"))
        else:
            print(f"Operation Failed!: Could not delete phone call record {phone_call_id}\n\t{res}")


    def update_phonecall(self,phone_call_id, phone_call):
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email": f"{self.__uname}", "password": f"{self.__password}", "client": True}

        headers = {'content-type': 'application/json', }
        auth_res = requests.post(url, data=json.dumps(data), headers=headers)

        # check response
        print(auth_res)
        print(auth_res.text)
        # send request (POST)
        url = 'http://' + self.__host + ':' + self.__port + '/user/update'
        res = requests.post(url, data=json.dumps({"phonecall_id": str(phone_call_id)}), cookies=auth_res.cookies,
                            headers=headers)
        # to here !!!!!!
        if json.loads(res.text)['res'] == "200":
            print(f'Phonecall UPDATED: {phonecall.__str__()}')
        else:
            print(f'ERROR: could not update record {phone_call_id} \n\t{json.loads(res.text)["res"]}')
    def search_caller(self,caller,callee):
        data=dict()
        data["caller"] = True
        data["callee"] = True
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email": f"{self.__uname}", "password": f"{self.__password}", "client": True}

        headers = {'content-type': 'application/json', }
        auth_res = requests.post(url, data=json.dumps(data), headers=headers)

        # check response
        print(auth_res)
        print(auth_res.text)
        # send request (POST)
        url = 'http://' + self.__host + ':' + self.__port + '/user/searchcaller'
        res = requests.post(url, data=json.dumps(data), cookies=auth_res.cookies, headers=headers)
        res = json.loads(res.text)['res']
    def search_date(self,start_date,end_date):
        data = dict()
        data["start_date"] = True
        data["end_date"] = True
        url = 'http://' + self.__host + ':' + self.__port + '/auth'
        data = {"email": f"{self.__uname}", "password": f"{self.__password}", "client": True}

        headers = {'content-type': 'application/json', }
        auth_res = requests.post(url, data=json.dumps(data), headers=headers)

        # check response
        print(auth_res)
        print(auth_res.text)
        # send request (POST)
        url = 'http://' + self.__host + ':' + self.__port + '/user/searchdate'
        res = requests.post(url, data=json.dumps(data), cookies=auth_res.cookies, headers=headers)
        print(res)
        res = json.loads(res.text)['res']

if __name__ == '__main__':
    pass
    # username = "admin@cau.edu"
    # password = "1234"
    # phonecall = PhoneCall('123-880-4567', '404-880-9632', '11/11/2020 15:10', '11/11/2020 15:25')
    # pbc = PhoneBillClient()
    # pbc.set_username(username)
    # pbc.set_password(password)
    # pbc.add_phonecall(phonecall)
    # pbc.delete_phonecall(5)




