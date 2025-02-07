# Imports
import random
from datetime import datetime, timedelta

# IP Pool
ip_addresses = [
    "192.168.1.1", "192.168.1.2", "203.0.113.1", "198.51.100.1",
    "172.16.0.1", "10.0.0.1", "203.0.113.5", "192.0.2.1",
    "203.0.113.10", "198.51.100.5"
]

http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD"] # Method Pool
urls = ["/index.html", "/about.html", "/contact.html", "/products.html", "/services.html"] # File Pool
status_codes = [200, 404, 500, 301, 403] # Codes
log_file_path = r'C:\your_path\access.log' # Path

# Functions

# Generator
def generate_log_entry(ip):
    method = random.choice(http_methods)
    url = random.choice(urls)
    status = random.choice(status_codes)
    size = random.randint(100, 5000)  # Random Size
    timestamp = datetime.now() - timedelta(days=random.randint(0, 30))  # Random Timestamp
    formatted_time = timestamp.strftime("%d/%b/%Y:%H:%M:%S +0000")
    
    return f"{ip} - - [{formatted_time}] \"{method} {url} HTTP/1.1\" {status} {size}"

# Writer
def generate_access_log(num_entries):
    with open(log_file_path, 'w') as log_file:
        for _ in range(num_entries):
            ip = random.choice(ip_addresses)
            log_entry = generate_log_entry(ip)
            log_file.write(log_entry + "\n")

if __name__ == "__main__":
    num_entries = 100  # Number of entries
    generate_access_log(num_entries)
    print(f"Generated {num_entries} log entries in '{log_file_path}'.") # Confirmation
