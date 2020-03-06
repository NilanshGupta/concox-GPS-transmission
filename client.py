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

#GPS PACKET DECODING
lst= [78 ,78 ,22 ,22 ,"0F" ,"0C" ,"1D" ,"02" ,33 ,"05" ,"C9" ,"02" ,"7A", "C8", 18, "0C" ,46 ,58 ,60 ,00 ,14 ,00 ,"01","CC" ,00, 28 ,"7D" ,00 ,"1F" ,71 ,00, 00 ,"01" ,00 ,"08",20 ,86 ,"0D" ,"0A"]


start_bit=lst[:2]
packet_length=lst[2]
Protocol_Number = lst[3]
date_time = lst[3:9]
quantity_of_GPS = lst[9]
latitude = lst[9:15]
longitude = lst[14:19]
speed = lst[19]
status = lst[19:22]
MCC = lst[22:25]
MNC = lst[25]
LAC = lst[25:28]
cell_id = lst[28:32]
ACC = lst[32]
data_upload = lst[33]
GPS_reupload = lst[34]
milage = lst[34:39]
serial_no = lst[39:42]
error_check = lst[42:45]
stop_bit= lst [45:]

print(start_bit)
print(packet_length)
print(Protocol_Number)
print(date_time)
print(quantity_of_GPS)
print(latitude)
print(longitude)
print(speed)
print(status)
print(MCC)
print(MNC)
print(LAC)
print(cell_id)
print(ACC)
print(data_upload)
print(GPS_reupload)
print(milage)
print(serial_no)
print(error_check)
print(stop_bit)

with open('output.txt', 'w') as file:
    a=' '.join(map(str, start_bit))
    b = ' '.join(map(str, packet_length))
    c = ' '.join(map(str,Protocol_Number ))
    d = ' '.join(map(str,date_time ))
    e = ' '.join(map(str, quantity_of_GPS))
    f = ' '.join(map(str, latitude))
    g = ' '.join(map(str, longitude))
    h = ' '.join(map(str, speed))
    i = ' '.join(map(str, status))
    j = ' '.join(map(str, MCC))
    k = ' '.join(map(str, MNC))
    l = ' '.join(map(str, LAC))
    m = ' '.join(map(str, cell_id))
    n = ' '.join(map(str, ACC))
    o = ' '.join(map(str, data_upload))
    p = ' '.join(map(str, GPS_reupload))
    q = ' '.join(map(str, milage))
    r = ' '.join(map(str, serial_no))
    s = ' '.join(map(str, error_check))
    t = ' '.join(map(str, stop_bit))
    file.write('\na=''\''+a+'\'')
    file.write('\na=''\''+c+'\'')
    file.write('\na=''\''+d+'\'')
    file.write('\na=''\''+e+'\'')
    file.write('\na=''\''+f+'\'')
    file.write('\na=''\''+g+'\'')
    file.write('\na=''\''+h+'\'')
    file.write('\na=''\''+i+'\'')
    file.write('\na=''\''+j+'\'')
    file.write('\na=''\''+k+'\'')
    file.write('\na=''\''+l+'\'')
    file.write('\na=''\''+m+'\'')
    file.write('\na=''\''+n+'\'')
    file.write('\na=''\''+o+'\'')
    file.write('\na=''\''+p+'\'')
    file.write('\na=''\''+q+'\'')
    file.write('\na=''\''+r+'\'')
    file.write('\na=''\''+s+'\'')
    file.write('\na=''\''+t+'\'')

#GPS MODULE


f.close()


#open and read the file after the appending:
f = open("output.txt", "r")


print(f.read())
s.send(hrt)
f.close()


s.close()
print('connection closed')
