import socket
import threading
import time

# Function to scan a specific port on the target
def scan_port(target, port):
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt (1 second)
        sock.settimeout(1)
        # Attempt to connect to the target and port
        result = sock.connect_ex((target, port))
        if result == 0:
            # If the connection attempt is successful, the port is open
            print(f'Port {port}: OPEN')
        sock.close()
    except Exception as e:
        # Handle any exceptions that might occur during the connection attempt
        pass

# Main function for port scanning
def main():
    target = input('Enter host for scanning: ')
    target_IP = socket.gethostbyname(target)
    start_port = int(input('Start from which port? '))
    end_port = int(input('End at which port? '))
    print('Starting scan on host: ', target_IP, '(', start_port,'-', end_port, ')')
    
    threads = []  # List to hold our threads

    for port in range(start_port, end_port):
        # Create a thread for scanning each port
        thread = threading.Thread(target=scan_port, args=(target_IP, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("Time taken: ", time.time() - start_time)

if __name__ == "__main__":
    start_time = time.time()
    main()