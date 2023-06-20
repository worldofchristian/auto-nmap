import csv
import json
import nmap

def scan_ip(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(ip_address, arguments='-sV --script vulners')
    return scanner[ip_address]

def main():
    # Open the CSV file and read the IP addresses
    with open('ip_addresses.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        ip_addresses = [row['IP Address'] for row in csv_reader]

    scan_results = []

    # Scan each IP address and store the results
    for ip_address in ip_addresses:
        result = scan_ip(ip_address)
        scan_results.append(result)

    # Write the scan results to a JSON file
    with open('scan_results.json', 'w') as json_file:
        json.dump(scan_results, json_file, indent=4)

if __name__ == '__main__':
    main()
