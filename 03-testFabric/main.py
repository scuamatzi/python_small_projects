import getpass
import re
from fabric import Connection, Config

#password=getpass.getpass("Enter password for server 50.7: ")

#config = Config(overrides={'sudo':{'password':password}})

#conn = Connection("192.168.50.7", user="salvador", config=config)
conn = Connection("192.168.50.7", user="salvador")

#with conn.cd("/home/salvador/etc"):
#with conn.cd("~/etc"):
#    conn.run("ls -lh")

#conn.sudo("date")

ethdata=conn.run("ifconfig",hide=True)

lines=ethdata.stdout.split("\n")
inet_lines=[l for l in lines if "inet " in l and "127.0.0.1" not in l]

span=re.search("inet ([0-9]+\.){3}[0-9]+", inet_lines[0]).span()
ip_address=inet_lines[0][span[0]+5:span[1]]

print(ip_address)