import socket
import network
from time import sleep
import machine
from machine import Pin
import neopixel

ssid = 'mrsh77'
password = '1m77n2299215r77#'


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    address = (ip,80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    #print(connection)
    return connection


neopixel_pin = Pin(0)
led_num = 8
brightness = 0.2  # Adjust the brightness (0.0 - 1.0)

rgb_ring = neopixel.NeoPixel(neopixel_pin, led_num)


def brightnessfcn(color):
    r, g, b= color
    
    r = int(r * brightness)
    g = int(g * brightness)
    b = int(b * brightness)
    return (r,g,b)


try:
    ip = connect()
    connection = open_socket(ip)
    while True:
        # Accept a connection from a client
        client, addr = connection.accept()
        print(f'Connected to {addr}')
        while True:
            # Receive data from the client
            data = client.recv(1024)
            if data:
                # Print the data to the console
                print(data)
                if data == b'sad':
                    lamp_color = (255,255,255)
                    final_color = brightnessfcn(lamp_color)
                    
                    rgb_ring.fill(final_color)
                    rgb_ring.write()
                    
                elif data == b'fear':
                    lamp_color = (128,0,128)
                    final_color = brightnessfcn(lamp_color)
                    
                    rgb_ring.fill(final_color)
                    rgb_ring.write()
                
                elif data == b'angry':
                    lamp_color = (0,0,255)
                    final_color = brightnessfcn(lamp_color)
                    
                    rgb_ring.fill(final_color)
                    rgb_ring.write()
                elif data == b'happy':
                    lamp_color = (255,165,0)
                    final_color = brightnessfcn(lamp_color)
                    
                    rgb_ring.fill(final_color)
                    rgb_ring.write()
                    
                elif data == b'neutral':
                    lamp_color = (255,255,255)
                    final_color = brightnessfcn(lamp_color)
                    
                    rgb_ring.fill(final_color)
                    rgb_ring.write()
                    
                # Send a response back to the client
                client.send(b'OK')
            else:
                # Break the loop if no data is received
                break
        # Close the client socket
        client.close()
except KeyboardInterrupt:
    # Close the server socket
    connection.close()
    machine.reset()

