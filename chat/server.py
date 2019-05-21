import socket
import time


host = socket.gethostbyname(socket.gethostname())
port = 9090

#второй параметр socket_type может быть SOCK_STREAM(для TCP)
#или SOCK_DGRAM(для UDP)
udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_s.bind((host, port))
quit = False
print("[SERVER STARTED IP " + host +"]")

clients = []

while not quit:
    try:
        # recvfrom - получает UDP сообщения
        data, addr = udp_s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        # preprocessing data
        timeing = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        print("["+addr[0]+"] = ["+str(addr[1])+"] = ["+timeing+"]/", end="")
        print(data.decode('utf-8'))

        # sendto - передача сообщения UDP
        for client in clients:
            if addr != client:
            # отправитель не получает собственные сообщения
                udp_s.sendto(data, client)

    except:
        print("\nSERVER STOPPED")
        quit = True

udp_s.close()