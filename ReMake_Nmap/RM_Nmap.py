a = """

▀███▀▀▀██▄                                  ▀███
  ██   ▀██▄                                   ██
  ██   ▄██   ▄▄█▀██▀████████▄█████▄  ▄█▀██▄   ██  ▄██▀  ▄▄█▀██
  ███████   ▄█▀   ██ ██    ██    ██ ██   ██   ██ ▄█    ▄█▀   ██
  ██  ██▄   ██▀▀▀▀▀▀ ██    ██    ██  ▄█████   ██▄██    ██▀▀▀▀▀▀
  ██   ▀██▄ ██▄    ▄ ██    ██    ██ ██   ██   ██ ▀██▄  ██▄    ▄
▄████▄ ▄███▄ ▀█████▀████  ████  ████▄████▀██▄████▄ ██▄▄ ▀█████▀



▀███▄   ▀███▀
  ███▄    █
  █ ███   █ ▀████████▄█████▄  ▄█▀██▄ ▀████████▄
  █  ▀██▄ █   ██    ██    ██ ██   ██   ██   ▀██
  █   ▀██▄█   ██    ██    ██  ▄█████   ██    ██
  █     ███   ██    ██    ██ ██   ██   ██   ▄██
▄███▄    ██ ▄████  ████  ████▄████▀██▄ ██████▀
                                       ██
                                     ▄████▄
-------------------------------------------------------------------
"""
# https://texteditor.com/font-converter/
import socket
import threading

print(a)
target_host = input("Enter target hostname or IP address:\n")
min_port = int(input("Enter minimum port number:\n"))
max_port = int(input("Enter maximum port number:\n"))

open_ports = []
lock = threading.Lock()


def port_scan(port, protocol="tcp"):
    try:
        if protocol == "tcp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol == "udp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0.2)
        if sock.connect_ex((target_host, port)) == 0:
            with lock:
                open_ports.append(port)
    except:
        pass


def scan_range(start_port, end_port, protocol):
    for port in range(start_port, end_port + 1):
        port_scan(port, protocol)


threads = []
num_threads = 10
ports_per_thread = (max_port - min_port) // num_threads

for i in range(num_threads):
    start_port = min_port + (i * ports_per_thread)
    end_port = start_port + ports_per_thread - 1
    if i == num_threads - 1:
        end_port = max_port
    thread = threading.Thread(target=scan_range, args=(start_port, end_port, "tcp"))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Open ports:")
print(open_ports)
