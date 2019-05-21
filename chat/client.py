import socket
import time
import threading
import errno


host_client = socket.gethostbyname(socket.gethostname())
port_client = 0

host_server = "10.17.160.97"
port_server = 9090

server = (host_server, port_server)
client = (host_client, port_client)

key = 8194

shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                decrypt = "";
                k = False
                for i in data.decode("utf-8") :
                    if i == ":":
                        decrypt += i;
                        k = True
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)
        except socket.error:
            if socket.error.errno == errno.EAGAIN:
                time.sleep(0.1)
            else:
                raise socket.error





s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((client))


alias = input("Username -> ")

# target is a functions
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

while not shutdown:
    if not join:
        s.sendto(("{"+alias+"} => join chat").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input("-->")
            # start
            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt
            # end

            if message != "":
                s.sendto(("{" + alias + "} ::" + message).encode("utf-8"), server)
            time.sleep(0.2)
        except:
            s.sendto(("{" + alias + "}  <= left chat").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
