import socket


def scan_ports(ip, port_range):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def main():
    target_ip = input("Введите IP-адрес для сканирования: ")
    start_port = int(input("Введите начальный порт для сканирования: "))
    end_port = int(input("Введите конечный порт для сканирования: "))
    port_range = (start_port, end_port)
    open_ports = scan_ports(target_ip, port_range)

    if len(open_ports) > 0:
        print("PORTS:    STATUS")
        for port in open_ports:
            print(f"{port}/tcp   open")
    else:
        print("Нет открытых портов.")
# BaseException

if __name__ == "__main__":
    main()
