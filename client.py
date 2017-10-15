#{"changed":true,"filter":false,"title":"server.py","tooltip":"/server.py","value":"import socket\nimport threading\nimport time\nimport sys\nimport pickle\nimport Event\n\n# Read in from hosts.txt to config NODE_ID and \n# cmd line will be like \"pyt
import socket

clientSocket = socket.socket()
host = socket.gethostname()
port = 8082
clientSocket.connect((host, port))
print(clientSocket.recv(1024))
clientSocket.close