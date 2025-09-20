import re
from collections import Counter

# Path to your log file
LOG_FILE = "access.log"

# Regex pattern for Apache/Nginx common log format
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s-\s-\s\[(?P<date>[^\]]+)\]\s"(?P<method>[A-Z]+)\s(?P<page>[^\s]+)\sHTTP/[0-9.]+"\s(?P<status>\d+)\s(?P<size>\d+)'
)

def analyze_log(file_path):
    ip_counter = Counter()
    page_counter = Counter()
    status_counter = Counter()

    with open(file_path, "r") as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                # Debugging: show parsed values
                print("MATCHED:", match.groupdict())

                ip = match.group("ip")
                page = match.group("page")
                status = match.group("status")

                ip_counter[ip] += 1
                page_counter[page] += 1
                status_counter[status] += 1
            else:
                print("NO MATCH:", line.strip())

    # Report
    print("\n--- Log Analysis Report ---\n")

    total_requests = sum(status_counter.values())
    if total_requests == 0:
        print("No valid log entries found.")
        return

    print(f"Total requests: {total_requests}")
    print(f"Total 404 errors: {status_counter.get('404', 0)}\n")

    print("Top 5 requested pages:")
    for page, count in page_counter.most_common(5):
        print(f"{page}: {count} requests")

    print("\nTop 5 IP addresses making requests:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} requests")


if __name__ == "__main__":
    analyze_log(LOG_FILE)