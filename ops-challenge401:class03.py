from scapy.all import sr1, ICMP, IP 
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
from datetime import datetime

def send_icmp_packet(destination_ip):
    """
    Send an ICMP packet to destination IP
    Response will be success if packet is sent successfully, otherwise failure
    """
    try:
        response = sr1(IP(dst=destination_ip)/ICMP(), timeout=2, verbose=False)
        if response:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def send_email_notification(sender_email, sender_password, recipient_email, status, destination_ip):
    """
    Send an email notification with the given status
    """
    try:
        server = smtlib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_password)

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] =  recipient_email
        message['Subject'] = f'Uptime Sensor Status - {status}'
        body = f"ICMP packet sent to {destination_ip} is {status}"
        message.attach(MIMEText(body, 'plain'))

    server.send_message(message)
    server.quit()
    print("Email sent")
except Exception as e:
    print(f"Email failed")

if __name__ == "__main__":
    sender_email = input("Enter email: ")
    sender_password = getpass("Enter password: ")
    recipient_email = input("Enter recipient email: ")

    destination_ip = 8.8.8.8
    previous_status = None
    
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d")
        status = None
        if send_icmp_packet(destination_ip):
            status = "Success"
        else:
            status = "Failure"
        print(f"[{timestamp}] ICMP packet sent to {destination_ip}: {status}")

        time.sleep(2)