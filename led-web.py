#import libraries
import network
import socket
from time import sleep
from picozero import pico_led

#set up wifi
ssid = 'your-ssid'
password = 'your-password'

#Connect to Wifi and obtain IP address
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected == False:
        print("Waiting for connection...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
#Get IP address and conenct to port 80
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

#Render HTML
def webpage():
    #Template HTML
    with open("index.html", 'r') as f:
        html = f.read()
    return html

#Serve the page and include the logic here
def serve(connection):
    pico_led.off()
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == "/on?":
            pico_led.on()
        if request == "/off?":
            pico_led.off()
        html = webpage()
        client.send(html)
        client.close()

# Run the application 
try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
