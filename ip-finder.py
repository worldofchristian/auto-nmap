import pickle
import requests

def search_dehashed(email):
    # Perform a search using Dehashed API
    url = f"https://api.dehashed.com/search?query={email}"
    headers = {
        "Authorization": "Bearer API_KEY"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["entries"]
    else:
        return []

def main():
    # Load the email addresses from the Python file
    with open('emails.py', 'rb') as python_file:
        emails = pickle.load(python_file)

    scannable_ips = {}

    # Search each email address and store the associated IP addresses
    for email in emails:
        entries = search_dehashed(email)

        for entry in entries:
            ip_address = entry.get("ip_address")
            if ip_address:
                scannable_ips[email] = ip_address

    # Write the scannable IPs to a JSON file
    with open('scannable-ip.json', 'w') as json_file:
        json.dump(scannable_ips, json_file, indent=4)

if __name__ == '__main__':
    main()