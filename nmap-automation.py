import json
import nmap
import pickle

def scan_ip(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(ip_address, arguments='-sV --script vulners')
    return scanner[ip_address]

def main():
    # Load the IP addresses from the JSON file
    with open('scannable-ip.json', 'rb') as json_file:
        ip_addresses = pickle.load(json_file)

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
