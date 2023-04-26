import requests
import json

import os

import paramiko


# SSH接続情報
ip_address = "10.71.157.159"
username = "admin"
# password = "C!scoI23"
key_filename = "/Users/sarimits/.ssh/id_rsa"


### NXAPI関連設定 ###
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

### SSH接続設定 ###

# SSH接続情報
ip_address = "10.71.157.159"
username = "admin"
# password = "C!scoI23"
key_filename = "/Users/sarimits/.ssh/id_rsa"


### apply access-list

for filename in os.listdir('./test-svi-apply-list'):
    with open(os.path.join('./test-svi-apply-list', filename), 'r') as file:
        cmds = file.read().strip().split('\n')  # ファイルの中身を読み込んで、改行で分割する

        # showコマンドを最後に追加
        cmds.append("show ip access-lists summary")
        # cmds.append("show hardware access-list resource entries")
        # cmds.append("show hardware access-list resource utilization")
        # cmds.append("show system internal aclqos info spl database summary")

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
    
    #1Fileアプライする毎に、SSHしてLogを保存する
    # SSHセッションを開始する
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh_client.connect(ip_address, username=username, password=password)
    ssh_client.connect(ip_address, username=username, key_filename=key_filename)

    # コマンドを実行する
    commands = ["show hardware access-list resource entries", "show hardware access-list resource utilization", "show hardware access-list resource utilization", "show system internal aclqos info spl database summary"]
    results = []
    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        results.append(stdout.read().decode())

    # 結果をファイルに保存する
    # 結果をファイルに保存する
    path = "./logs/{}".format(filename)
    if not os.path.exists(path):
        os.makedirs(path)
    

    with open(path + "/result_entries.txt", "w") as f:
        f.write(results[0])
    with open(path + "/result_utilization.txt", "w") as f:
        f.write(results[1])
    with open(path + "/show hardware access-list resource utilization", "w") as f:
        f.write(results[2])
    with open(path + "/show system internal aclqos info spl database summary", "w") as f:
        f.write(results[3])


# print(payload)

# if client_cert_auth is False:
#     response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
#     print(response)
# else:
#     url='https://10.71.157.159/ins'
#     response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert)



##############################################################

###ログ機能実装前

# import requests
# import json

# import os

# """
# Modify these please
# """
# #For NXAPI to authenticate the client using client certificate, set 'client_cert_auth' to True.
# #For basic authentication using username & pwd, set 'client_cert_auth' to False.
# client_cert_auth=False
# switchuser='admin'
# switchpassword='C!scoI23'
# client_cert= False
# client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
# ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

# url='http://10.71.157.159/ins'
# myheaders={'content-type':'application/json-rpc'}



# payload = []
# id = 1

# ### apply access-list

# for filename in os.listdir('./test-svi-apply-list'):
#     with open(os.path.join('./test-svi-apply-list', filename), 'r') as file:
#         cmds = file.read().strip().split('\n')  # ファイルの中身を読み込んで、改行で分割する

#         # showコマンドを最後に追加
#         cmds.append("show ip access-lists summary")
#         # cmds.append("show hardware access-list resource entries")
#         # cmds.append("show hardware access-list resource utilization")
#         # cmds.append("show system internal aclqos info spl database summary")

#     for cmd in cmds:
#         payload.append({
#             "jsonrpc": "2.0",
#             "method": "cli",
#             "params": {
#                 "cmd": cmd.strip(),
#                 "version": 1
#             },
#             "id": id
#         })
#         id += 1


# # print(payload)

# if client_cert_auth is False:
#     response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
#     print(response)
# else:
#     url='https://10.71.157.159/ins'
#     response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert)

