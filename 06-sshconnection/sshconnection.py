import paramiko
import time
from getpass import getpass

HOST="192.168.50.7"
#HOST="192.168.50.8"
#HOST="192.168.0.2"
USER="salvador"

if __name__ == '__main__':
	#print("hello world!")
	try:
		client=paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		#password=getpass("Password: ")

		#client.connect(HOST,username=USER, password=password)
		client.connect(HOST,username=USER)

		stdin, stdout, stderr=client.exec_command("ls | grep unison")
		time.sleep(1)

		#print(type(stdout.read().decode()))

		result = stdout.read().decode()

		print(result)

		client.close()

	except paramiko.ssh_exception.AuthenticationException as error:
		print("Autenticacion fallida")

	except paramiko.ssh_exception.NoValidConnectionsError as error2:
		print(f"Server {HOST} unavailable.")
