import paramiko
import time
#from getpass import getpass

HOST="apicloud.ddns.net"
#HOST="192.168.0.2"
USER="ubuntu"

if __name__ == '__main__':
	#print("hello world!")
	try:
		client=paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		#password=getpass("Password: ")

		#client.connect(HOST,username=USER, password=password)
		client.connect(HOST,username=USER, key_filename="/home/diablo/.ssh/aws/nodejs.pem")

		stdin, stdout, stderr=client.exec_command("dfh")
		#stdin, stdout, stderr=client.exec_command("free -m")
		time.sleep(1)

		result = stdout.read().decode()

		print(result)
		print("error message")
		print(stderr.read().decode())

		client.close()

	except paramiko.ssh_exception.AuthenticationException as error:
		print("Autenticacion fallida")
