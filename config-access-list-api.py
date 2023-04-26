import requests
import json

import os

"""
Modify these please
"""
#For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
#For basic authentication using username & pwd, set 'client_cert_auth' to False.
client_cert_auth=False
switchuser='admin'
switchpassword='C!scoI23'
client_cert= False
client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='http://10.71.157.159/ins'
myheaders={'content-type':'application/json-rpc'}



payload = []
id = 1

### config access-list

for filename in os.listdir('./test-access-list'):
    with open(os.path.join('./test-access-list', filename), 'r') as file:
        cmds = file.read().strip().split('\n')  # ファイルの中身を読み込んで、改行で分割する

    for cmd in cmds:
        payload.append({
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
                "cmd": cmd.strip(),
                "version": 1
            },
            "id": id
        })
        id += 1

if client_cert_auth is False:
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

else:
    url='https://10.71.157.159/ins'
    response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert)

