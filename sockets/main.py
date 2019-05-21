import socket

URLS = {
    '/' : 'hello index',
    '/blog': 'hello blog'
}

# парсим request
def parse_request(request):
      parsed = request.split(' ')
      method = parsed [0]
      url = parsed [1]
      return (method, url)


# генерируем заголовки
def generate_headers(method, url):
     if not method == 'GET':
         return ('HTTP/1.1 405 Method not allowed\n\n', 405)
     if not url in URLS:
         return ('HTTP:/1.1 404 Not found\n\n', 404)

     return ('HTTP:/1.1 OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return f'<h1>{URLS[url]}</h1>'



# распаковываем спарсенный запрос, генерируем заголовки, код ответа, тело ответа
def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()

def run():
    # INET - протокол IP 4v.,SOCK_STREAM - TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SOL_SOCKET - уровень НАШЕГО сокета, допускаем повторное использование адреса)
    # SO = socket option
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        # accept() returns touple
        client_socket, addr = server_socket.accept()
        # recv(receive) - получать, передаем кол-во байт
        request = client_socket.recv(1024)
        # если нужно норм. отображение запросов - декодируем request.decode('utf-8')
        print(request)
        print()
        print(addr)


        response = generate_response(request.decode('utf-8'))

        # cокеты не поминают строк -> мы должны их закодировать
        client_socket.sendall(response)
        # не увидим изменения, пока не закроем сокет
        client_socket.close()



if __name__ == '__main__':
    run()
