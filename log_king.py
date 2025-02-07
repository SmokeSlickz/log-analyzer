# imports
import re
from collections import defaultdict
from datetime import datetime

# Class
class LogFileAnalyzer:

    # Functions
    # Initialize
    def __init__(self, log_file):
        self.log_file = log_file
        self.ip_requests = defaultdict(int)
        self.error_requests = defaultdict(int)
        self.suspicious_ips = set()

    # Read
    def parse_log(self):
        with open(self.log_file, 'r') as file:
            for line in file:
                self.analyze_line(line)

    # Analyze
    def analyze_line(self, line):
        log_pattern = re.compile(
            r'(?P<ip>[\d\.]+) - - \[(?P<date>[^\]]+)\] "(?P<method>[A-Z]+) (?P<url>[^\s]+) HTTP/[0-9\.]+" (?P<status>\d{3}) (?P<size>\d+)'
        ) # Parse 
        match = log_pattern.match(line)
        if match:
            ip = match.group('ip')
            status = int(match.group('status'))

            # Count Requests Per IP
            self.ip_requests[ip] += 1

            # Count Error Requests (Codes 400 & Above)
            if status >= 400:
                self.error_requests[ip] += 1

            # Identify Suspicious Activity (More Than 100 Requests / 10 Errors = Pottential DOS)
            if self.ip_requests[ip] > 100 or self.error_requests[ip] > 10:
                self.suspicious_ips.add(ip)

    # Display
    def report(self):
        print("Total Requests by IP:")
        for ip, count in self.ip_requests.items():
            print(f"{ip}: {count} requests")

        print("\nError Requests by IP:")
        for ip, count in self.error_requests.items():
            print(f"{ip}: {count} error requests")

        print("\nSuspicious IPs:")
        for ip in self.suspicious_ips:
            print(ip)

# Main Thread
if __name__ == "__main__":
    log_analyzer = LogFileAnalyzer(r'C:\your_path\access.log')  # Path
    log_analyzer.parse_log()
    log_analyzer.report()
