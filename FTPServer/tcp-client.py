import socket

if __name__ == "__main__":
    
    # define the socket parameters
    host = "127.0.0.1"
    port = 8080
    #totalClients = int(input('Enter number of clients: '))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((host, port))

    # File transfer loop
    while True:
        filename = input('Input filename you wanto to transfer: ')
        try:
            fi = open(filename, 'r')
            data = fi.read()
            if not data:
                break
            while data:
                sock.send(str(data).encode())
                data = fi.read()
            fi.close()
        except IOError:
            print("File does not exist")