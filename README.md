# auto-nmap
This tool is intended for performing security audits on a company network. It works by searching data dumps for IP addresses that are linked to company emails, then performs a vulnerability assessment using nmap.

# ip-finder.py
Takes in a list of company emails and searches publicly available breached datasets. Any IP addresses associated with the email address are written to a new json file.

# nmap-automation
Automatees the nmap tool to scan the returned IP addresses for vulnerabilities, writes them to a new json file.
