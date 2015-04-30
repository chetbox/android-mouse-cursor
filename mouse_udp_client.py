import socket


def getch():   # define non-Windows version
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


UDP_IP = "192.168.0.21"
UDP_PORT = 9999

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print ""
print "W, A, S, D - Move mouse"
print "Space      - Click"
print "Q          - Quit"


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
    key = ord(getch())
    if key == 119: # W
        # print 'up'
        sock.sendto('0', (UDP_IP, UDP_PORT))
    elif key == 97: # A
        # print 'left'
        sock.sendto('2', (UDP_IP, UDP_PORT))
    elif key == 115: # S
        # print 'down'
        sock.sendto('1', (UDP_IP, UDP_PORT))
    elif key == 100: # D
        # print 'right'
        sock.sendto('3', (UDP_IP, UDP_PORT))
    elif key == 113: # Q
        break
    elif key == 32: # Space
        # print 'click'
        sock.sendto('4', (UDP_IP, UDP_PORT))


