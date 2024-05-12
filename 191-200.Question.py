print("Question NO:191\nA wireless technician is working to upgrade the wireless infrastructure for a company. The company currently uses the 802.11g wireless standard on all access points. The company requires backward compatibility and is requesting the least expensive solution. Which of the following should the technician recommend to the company?\n A. 802.11a\n B. 802.11ac\n C. 802.11ax\n D. 802.11n")
print("\nQuestion NO:192\nA technician knows the MAC address of a device and is attempting to find the device's IP address. Which of the following should the technician look at to find the IP address? (Choose two.)\n A. ARP table\n B. DHCP leases\n C. IP route table\n D. DNS cache\n E. MAC address table\n F. STP topology")
print("\nQuestion NO:193\nWhich of the following attacks can be effectively protected against by using techniques to check if a connection was made by a human user? (Choose two.)\n A. Brute-force\n B. Dictionary\n C. On-path attack\n D. Phishing \n E. Shoulder surfing\n F. Evil twin")
print("\nQuestion NO:194\nAn engineer is using a tool to run an ICMP sweep of a network to find devices that are online. When reviewing the results, the engineer notices a number of workstations that are currently verified as being online are not listed in the report.\nThe tool was configured to scan using the following information:\n- Network address: 172.28.16.0\n- CIDR: /22\nThe engineer collected the following information from the client workstation:\n- IP address: 172.28.17.206\n- Subnet mask: 255.255.252.0 \nWhich of the following MOST likely explains why the tool is failing to detect some workstations?\n A. The scanned network range is incorrect.\n B. The subnet mask on the client is misconfigured.\n C. The workstation has a firewall enabled. \n D. The tool is unable to scan remote networks.")
print("\nQuestion NO:195\nA customer wants to log in to a vendor's server using a web browser on a laptop. Which of the following would require the LEAST configuration to allow encrypted access to the server?\n A. Secure Sockets Layer\n B. Site-to-site VPN\n C. Remote desktop gateway\n D. Client-to-site VPN")
print("\nQuestion NO:196\nWhich of the following provides redundancy on a file server to ensure the server is still connected to a LAN even in the event of a port failure on a switch?\n A. NIC teaming\n B. Load balancer\n C. RAID array\n D. PDUs")
print("\nQuestion NO:197\nA network technician needs to set up an access method for Ann, a manager, to work from home. Ann needs to locally mapped corporate resources to perform her job. Which of the following would provide secure access to the corporate resources?\n A. Utilize an SSH connection to the corporate server.\n B. Use TFTP to transfer files to corporate resources.\n C. Allow RDP through an external firewall.\n D. Connect utilizing client-to-site VPN.")
print("\nQuestion NO:198\nWhich of the following architectures would allow the network-forwarding elements to adapt to new business requirements with the least amount of operating effort?\n A. Software-defined network\n B. Spine and leaf\n C. Three-tier\n D. Backbone")
print("\nQuestion NO:199\nNewly crimped 26ft (8m) STP Cat 6 patch cables were recently installed in one room to replace cables that were damaged by a vacuum cleaner. Now, users in that room are unable to connect to the network. A network technician tests the existing cables first. The 177ft (54m) cable that runs from the core switch to the access switch on the floor is working, as is the 115ft (35m) cable run from the access switch to the wall jack in the office. Which of the following is the MOST likely reason the users cannot connect to the network?\n A. Mixed UTP and STP cables are being used. \n B. The patch cables are not plenum rated.\n C. The cable distance is exceeded.\n D. An incorrect pinout on the patch cable is being used.")
print("\nQuestion NO:200\nA user notifies a network administrator about losing access to a remote file server. The network administrator is able to ping the server and verifies the current firewall rules do not block access to the network fileshare. Which of the following tools would help identify which ports are open on the remote file server?\n A. dig\n B. nmap\n C. tracert\n D. nslookup\n")
answer = input(print("Do you have your answers?\n yes/no"))
if answer == "yes":
    print('''
Question NO: 191 = D
Explanation: The technician should recommend the "802.11n" standard to the company. 802.11n provides backward compatibility with older standards like 802.11g while offering improved performance, range, and reliability. It is also likely to be the least expensive option compared to newer standards like 802.11ac and 802.11ax.

Question NO: 192 = A, B
Explanation: To find the IP address of a device knowing its MAC address, the technician should look at:
A. ARP table: The Address Resolution Protocol (ARP) table maps IP addresses to MAC addresses, allowing devices to communicate on the same network.
B. DHCP leases: Dynamic Host Configuration Protocol (DHCP) servers assign IP addresses to devices dynamically. The DHCP lease table maintains a record of assigned IP addresses along with corresponding MAC addresses.

Question NO: 193 = D, E
Explanation: The attacks effectively protected against by using techniques to check if a connection was made by a human user are:
D. Phishing: Phishing attacks attempt to deceive users into providing sensitive information by impersonating legitimate entities. Techniques like CAPTCHA or user interaction verification can help detect and prevent automated phishing attempts.
E. Shoulder surfing: Shoulder surfing involves unauthorized individuals observing sensitive information, such as passwords or PINs, by looking over someone's shoulder. While not a technical attack, implementing physical security measures like privacy screens can prevent shoulder surfing.

Question NO: 194 = C
Explanation: The MOST likely explanation why the tool is failing to detect some workstations is that "The workstation has a firewall enabled." Firewalls commonly block ICMP (Internet Control Message Protocol) traffic, including ICMP echo requests used in ICMP sweeps or ping scans. Therefore, the workstations with enabled firewalls may not respond to ICMP requests, leading to their exclusion from the scan results.

Question NO: 195 = A
Explanation: To allow encrypted access to the vendor's server using a web browser on a laptop with the least configuration, the technician should recommend "Secure Sockets Layer (SSL)." SSL provides secure communication over the Internet by encrypting data transmitted between the web browser and the server. It requires minimal configuration compared to VPN solutions like site-to-site VPN or client-to-site VPN.

Question NO: 196 = A
Explanation: "NIC teaming" provides redundancy on a file server to ensure the server is still connected to a LAN even in the event of a port failure on a switch. NIC teaming involves aggregating multiple network interface cards (NICs) into a single logical interface, improving network performance and providing fault tolerance by distributing network traffic across multiple NICs.

Question NO: 197 = D
Explanation: To provide secure access to corporate resources for Ann, a manager working from home, the network technician should recommend "Connect utilizing client-to-site VPN." A client-to-site VPN (Virtual Private Network) allows remote users to securely connect to the corporate network over the Internet, providing encrypted access to corporate resources while maintaining data confidentiality and integrity.

Question NO: 198 = A
Explanation: The architecture that would allow the network-forwarding elements to adapt to new business requirements with the least amount of operating effort is "Software-defined network (SDN)." SDN decouples the network control plane from the forwarding plane, allowing centralized management and programmability of network devices through software-defined controllers. This flexibility enables rapid adaptation to changing business needs without extensive manual configuration.

Question NO: 199 = C
Explanation: The MOST likely reason the users cannot connect to the network is that "The cable distance is exceeded." Ethernet standards have maximum cable length limits, and exceeding these limits can result in signal degradation and connectivity issues. In this scenario, the newly installed 26ft (8m) patch cables may have exceeded the maximum distance allowed for reliable network connectivity.

Question NO: 200 = B
Explanation: To identify which ports are open on the remote file server, the network administrator should use "nmap." Nmap (Network Mapper) is a powerful network scanning tool that can be used to discover hosts and services on a network, including identifying open ports on remote servers. Using nmap, the administrator can perform port scans to determine which ports are listening and accessible on the file server.
''')

