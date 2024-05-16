print('''
QUESTION NO: 701
A network administrator is implementing an IPS on VLAN 1 and wants the IPS to learn what
to prevent on its own. Which of the following would MOST likely be installed?
A. Honeynet
B. Signature based IPS
C. Behavior based IPS
D. Host based IPS

QUESTION NO: 702
Which of the following is the first step a network administrator should take in the
troubleshooting methodology?
A. Establish a plan of action.
B. Document findings and outcomes.
C. Test the theory to determine cause.
D. Identify the problem.

QUESTION NO: 703
A network technician is troubleshooting a port channel issue. When logging in to one of the
switches, the technician sees the following information displayed:
Native VLAN mismatch detected on interface g0/1
Which of the following layers of the OSI model is most likely to be where the issue resides?
A. Layer 2
B. Layer 3
C. Layer 5
D. Layer 6

QUESTION NO: 704
A network administrator wants to analyze attacks directed toward the company's network.
Which of the following must the network administrator implement to assist in this goal?
A. A honeypot
B. Network segmentation
C. Antivirus
D. A screened subnet

QUESTION NO: 705
An organization purchased an allocation of public IPv4 addresses. Instead of receiving the
network address and subnet mask, the purchase paperwork indicates the allocation is a /28.
This type of notation is referred to as:
A. CIDR
B. classful
C. classless
D. RFC1918

QUESTION NO: 706
An ISP is providing internet to a retail store and has terminated its point of connection using a
standard Cat 6 pin-out. Which of the following terminations should the technician use when
running a cable from the ISP's port to the front desk?
A. F-type connector
B. TIA/EIA-568-B
C. LC
D. SC

QUESTION NO: 707
Client devices cannot enter a network, and the network administrator determines the DHCP
scope is exhausted. The administrator wants to avoid creating a new DHCP pool.
Which of the following can the administrator perform to resolve the issue?
A. Install load balancers
B. Install more switches
C. Decrease the number of VLANs
D. Reduce the lease time

QUESTION NO: 708
An administrator wants to host services on the internet using an internal server. The server is
configured with an RFC1918 address, and the administrator wants to make the services that
are hosted on the server available on one of the company's public IP addresses. Which of
the following should the administrator configure to allow this access?
A. IPv6 tunneling
B. Virtual IP
C. Dual stack
D. EUI-64

QUESTION NO: 709
Given the following output:
Which of the following attacks is this MOST likely an example of?
A. ARP poisoning
B. VLAN hopping
C. Rogue access point
D. Amplified DoS

QUESTION NO: 710
Within the realm of network security, Zero Trust:
 192.168.22.1    00-13-5d-00-06-23
 192.168.22.15   00-15-88-00-58-00
 192.168.22.10   00-13-5d-00-06-23
 192.168.22.100  00-13-5d-00-06-23
A. prevents attackers from moving laterally through a system.
B. allows a server to communicate with outside networks without a firewall.
C. block malicious software that is too new to be found in virus definitions.
D. stops infected files from being downloaded via websites.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 701
Answer: C. Behavior-based IPS
Reason: A behavior-based IPS learns and adapts to network behavior over time, allowing it to detect and prevent suspicious or malicious activities without relying solely on predefined signatures. This approach is suitable for the administrator's goal of having the IPS learn what to prevent on its own.

QUESTION NO: 702
Answer: D. Identify the problem.
Reason: In the troubleshooting methodology, the first step is to identify the problem. This involves gathering information, observing symptoms, and understanding the nature of the issue before proceeding with further analysis and resolution.

QUESTION NO: 703
Answer: A. Layer 2
Reason: A native VLAN mismatch typically indicates an issue at Layer 2 of the OSI model. The native VLAN is associated with Layer 2 trunking protocols like IEEE 802.1Q, so a mismatch suggests a problem with how VLAN tagging is configured on the switch interfaces.

QUESTION NO: 704
Answer: A. A honeypot
Reason: A honeypot is a trap set up to detect, deflect, or counteract attempts at unauthorized use of information systems. By deploying a honeypot, the network administrator can analyze attacks directed towards the company's network, study attack patterns, and gather information about potential threats.

QUESTION NO: 705
Answer: A. CIDR
Reason: CIDR (Classless Inter-Domain Routing) notation is used to represent IP address allocations more flexibly than traditional subnet masks. In the given scenario, a /28 allocation indicates that the network is using CIDR notation to specify the subnet size.

QUESTION NO: 706
Answer: B. TIA/EIA-568-B
Reason: TIA/EIA-568-B is a standard for structured cabling, including Ethernet cables like Cat 6. Using this standard ensures proper termination and compatibility, which is essential for maintaining network connectivity and performance.

QUESTION NO: 707
Answer: D. Reduce the lease time
Reason: By reducing the lease time for DHCP leases, the administrator can reclaim unused IP addresses more quickly, thereby alleviating the exhaustion of the DHCP scope without the need to create a new DHCP pool.

QUESTION NO: 708
Answer: B. Virtual IP
Reason: By configuring a Virtual IP (VIP), the administrator can route traffic from the company's public IP address to the internal server with an RFC1918 address. This allows external access to the server's hosted services while keeping its internal IP address private.

QUESTION NO: 709
Answer: A. ARP poisoning
Reason: The given output suggests that ARP (Address Resolution Protocol) poisoning is occurring, where malicious actors manipulate ARP tables to redirect network traffic to their own devices. This is often associated with man-in-the-middle attacks.

QUESTION NO: 710
Answer: A. prevents attackers from moving laterally through a system.
Reason: Zero Trust is a security model that assumes no trust by default, requiring strict identity verification and access controls for every user and device attempting to access resources on a network. One of its key principles is to prevent lateral movement by restricting access privileges based on dynamic risk assessments.
''')
