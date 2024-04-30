from scapy.all import sr1, ICMP, IP 
import time

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

if __name__ == "__main__":
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d")
        status = None
        if send_icmp_packet(destination_ip):
            status = "Success"
        else:
            status = "Failure"
        print(f"[{timestamp}] ICMP packet sent to {destination_ip}: {status}")

        time.sleep(2)