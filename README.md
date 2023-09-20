# Port-Scanner_Python_Project

## About:
* The primary function of a port scanner is to determine which ports on a networked device (like a router, server, or computer) are "open" or responsive to requests.

## Methods: 
* Different scanning methods are employed to determine this:
SYN scan (or half-open scan): The scanner sends a SYN (synchronization) packet to each port. If the target port responds with a SYN-ACK (synchronization acknowledged) packet, it is open. If it responds with an RST (reset) packet, it's closed. The scanner never completes the three-way handshake, hence the term "half-open." Connect scan: The scanner attempts to establish a full connection to the target port using the standard three-way handshake. This is more detectable than the SYN scan. UDP scan: This targets User Datagram Protocol ports. Since UDP is connectionless, this scan is generally less accurate than TCP scans.
Others: There are many other scanning techniques, like the FIN scan, Xmas scan, and Null scan, which utilize various flag settings in the TCP header to probe systems.

## Purpose:
* Security Assessments: 
  - Ethical hackers and security professionals use port scanners to identify open ports on a network as part of vulnerability assessments. Malicious Intent: Cybercriminals use port scanners to identify potential points of entry into a target system.

* Popular Port Scanners:
        Nmap (Network Mapper): One of the most well-known port scanners, it offers a wide range of scanning options and techniques.
        Netcat: Often dubbed the "Swiss army knife" of networking, it can write and read data across network connections.
        Masscan: Claims to be the fastest port scanner, able to scan the entire internet in under 6 minutes.

## Legality and Ethics: 
- Unauthorized port scanning is illegal in many jurisdictions and can be considered a form of trespassing or unauthorized surveillance. Always ensure you have permission to scan any network or system that doesn't belong to you.

It's important to note that just because a port is open doesn't necessarily mean the associated service is vulnerable. However, every open port is a potential point of entry and should be reviewed to determine if it needs to remain open and if additional protections, like firewalls or intrusion detection systems, are in place.
