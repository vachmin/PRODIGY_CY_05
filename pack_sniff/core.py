import socket

def main():
    # Replace this IP with your actual machine's IP
    HOST = "172.16.65.93"

    try:
        # Create raw socket for IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.bind((HOST, 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        print("🛰️ Sniffing IP packets... Press Ctrl+C to stop.")
        while True:
            packet = s.recvfrom(65565)
            print(packet[0])
    except KeyboardInterrupt:
        print("\n❌ Sniffing stopped.")
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    except Exception as e:
        print(f"⚠️ Error: {e}")

