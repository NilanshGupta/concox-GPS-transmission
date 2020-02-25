import socket                   # Import socket module


log= login()
hrt = heart()

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 8080                    # Reserve a port for your service.
s.connect((host, port))
s.send(log)


with open('received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=78 78 11 01 03 51 60 80 80 77 92 88 22 03 32 01 01 AA 53 36 0D 0A', (data))
        if not data:
            break
        # write data to a file
        f.write(data)



print('Successfully got the file')

#GPS MODULE

f2 = open("output.txt", "a")
f.write("78 78 22 22 0F 0C 1D 02 33 05 C9 02 7A C8 18 0C 46 58 60 00 14 00 01 CC 00 28 7D 00 1F 71 00 00 01 00 08 20 86 0D 0A")
f.close()

#open and read the file after the appending:
f = open("output.txt", "r")


print(f.read())
s.send(hrt)
f.close()


s.close()
print('connection closed')