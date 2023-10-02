import socket

# Input file name
file_name = "ip_list.txt"

# Output file name
output_file_name = "ptr_records.txt"

try:
    with open(file_name, "r") as file:
        ip_list = file.readlines()

    with open(output_file_name, "w") as output_file:
        for ip in ip_list:
            ip = ip.strip()
            try:
                ptr_record = socket.gethostbyaddr(ip)[0]
                output_file.write(f"IP: {ip} - PTR Record: {ptr_record}\n")
            except socket.herror:
                output_file.write(f"No PTR record found for IP: {ip}\n")
    print(f"PTR records are saved to {output_file_name} file.")
except FileNotFoundError:
    print(f"{file_name} not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
