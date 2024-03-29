import json
from pwn import remote


SERVER_ADDRESS = '35.221.65.23'
PORT = 11224


def main():
    nc = remote(SERVER_ADDRESS, PORT)

    with open('C:\\Users\\pika1\\source\\repos\\JJponce0913\\CyberSecurity\\Challenges\\dist\\client\\sign.der', 'rb') as f:
        sign = f.read()
        hex_sign = sign.hex()
    
    nc.send(hex_sign.encode('utf-8') + b'\n') 
    ret = nc.read().decode('utf-8')
    flag = json.loads(ret)
    print(flag)

main()