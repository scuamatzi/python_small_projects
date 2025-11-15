import paramiko
import time
import re

HOST="apicloud.ddns.net"
USER="ubuntu"
KEYFILE="/home/diablo/.ssh/aws/nodejs.pem"
#HOST="192.168.0.2"
#USER="salvador"

try:
    connection=paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #connection.connect(HOST,username=USER)
    connection.connect(HOST,username=USER,key_filename=KEYFILE)

    #cmd="df -h / | tail -n1 | awk '{print $5}'"
    cmd="ifconfig"

    stdin, stdout, stderr = connection.exec_command(cmd)
    time.sleep(1)
    result=stdout.read().decode().splitlines()
    
    inet_lines=[l for l in result if "inet " in l and "127.0.0.1" not in l]

    span=re.search("inet ([0-9]+\.){3}[0-9]+",inet_lines[0]).span()
    ipaddress=inet_lines[0][span[0]+5:span[1]]

    print(ipaddress)

except:
    print("There was an error with the connection. ")