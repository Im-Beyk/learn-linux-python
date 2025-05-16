import socket
import platform

print("System Info:")
print(f"Platform: {platform.system()}")
print(f"Platform Version: {platform.version()}")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("\nNetwork Info:")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")