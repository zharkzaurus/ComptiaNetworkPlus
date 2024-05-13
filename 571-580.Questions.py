print('''
QUESTION NO: 571
A company is reviewing ways to cut the overall cost of Its IT budget. A network technician
suggests removing various computer programs from the IT budget and only providing these
programs on an as-needed basis. Which of the following models would meet this
requirement?
A. Multitinency
B. laaS
C. SaaS
D. VPN

QUESTION NO: 572
Which of the following IP transmission types encrypts all of the transmitted data?
A. ESP
B. AH
C. GRE
D. UDP
E. TCP

QUESTION NO: 573
A technician is working on a ticket for a user in the human resources department who
received a new PC that does not connect to the internet. All users in human resources can
access the internet. The technician can ping the PC from the human resources router but not
from the IT network. Which of the following is the most likely cause of the issue?
A. Duplicate IP address
B. Misconfigured RIP
C. Improper VLAN assignment
D. Incorrect default gateway

QUESTION NO: 574
A network technician receives a report about a performance issue on a client PC that is
connected to port 1/3 on a network switch. The technician observes the following
configuration output from the switch:
 | 1/1 | Client PC | Connected | Full | 1000 |
 | 1/2 | Client PC | Connected | Full | 1000 |
 | 1/3 | Client PC | Connected | Full | 10   |
Which of the following is a cause of the issue on port 1/3?
A. Speed
B. Duplex
C. Errors
D. VLAN

QUESTION NO: 575
Which of the following would be used to indicate when unauthorized access to physical
internal hardware has occurred?
A. Motion detectors
B. Radio frequency identification tags
C. Tamper evident seal
D. Locking racks

QUESTION NO: 576
Which of the following VPN configurations should be used to separate Internet and corporate
traffic?
A. Split-tunnel
B. Remote desktop gateway
C. Site-to-site
D. Out-of-band management

QUESTION NO: 577
A company's VoIP phone connection is cutting in and out. Which of the following should be
configured to resolve this issue?
A. 802.1Q tagging
B. Jumbo frames
C. Native VLAN
D. Link aggregation

QUESTION NO: 578
A network administrator views a network pcap and sees a packet containing the following:
 community: public
 request-id: 13438
 get-responce 1.3.6.1.2.1.1.3.0 Value:206801150
Which of the following are the BEST ways for the administrator to secure this type of traffic?
(Choose two.)
A. Migrate the network to IPv6.
B. Implement 802.1 X authentication.
C. Set a private community string.
D. Use SNMPv3.
E. Incorporate SSL encryption.
F. Utilize IPSec tunneling.

QUESTION NO: 579
Which of the following assists a network administrator in reverse engineering malware and
viruses?
A. Virtual switches
B. Virtual machines
C. VLANs
D. IDS

QUESTION NO: 580
A lab environment hosts Internet-facing web servers and other experimental machines, which
technicians use for various tasks. A technician installs software on one of the web servers to
allow communication to the company's file server, but it is unable to connect to it Other
machines in the building are able to retrieve files from the file server.
Which of the following is the MOST likely reason the web server cannot retrieve the files, and
what should be done to resolve the problem?
A. The lab environment's IDS is blocking the network traffic. The technician can whitelist the
new application in the IDS.
B. The lab environment is located in the DM2, and traffic to the LAN zone is denied by
default. The technician can move the computer to another zone or request an exception from
the administrator.
C. The lab environment has lost connectivity to the company router, and the switch needs to
be rebooted. The technician can get the key to the wiring closet and manually restart the
switch
D. The lab environment is currently set up with hubs instead of switches, and the requests
are getting bounced back. The technician can submit a request for upgraded equipment to
management.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 571
Answer: C. SaaS
Explanation: Software as a Service (SaaS) model allows software to be provided on an as-needed basis, typically through a subscription-based pricing model. Users can access the software over the internet without the need for installing or maintaining it locally, thereby reducing overall IT costs.

QUESTION NO: 572
Answer: A. ESP
Explanation: Encapsulating Security Payload (ESP) is an IPsec protocol that encrypts the entire payload of a packet, providing confidentiality and integrity for IP transmissions.

QUESTION NO: 573
Answer: D. Incorrect default gateway
Explanation: If the PC in the human resources department can be pinged from the department's router but not from the IT network, the most likely cause is an incorrect default gateway configured on the PC. The default gateway should point to the router interface connected to the IT network.

QUESTION NO: 574
Answer: B. Duplex
Explanation: The issue on port 1/3 is likely caused by a duplex mismatch. The configuration indicates that the client PC connected to port 1/3 is set to operate at full duplex, but the switch port is operating at only 10 Mbps, which suggests a duplex mismatch between the client PC and the switch port.

QUESTION NO: 575
Answer: C. Tamper evident seal
Explanation: Tamper-evident seals are used to indicate when unauthorized access to physical internal hardware has occurred. These seals are designed to break or show signs of tampering if the hardware enclosure has been opened without authorization.

QUESTION NO: 576
Answer: A. Split-tunnel
Explanation: A split-tunnel VPN configuration should be used to separate Internet and corporate traffic. In a split-tunnel VPN, only traffic destined for the corporate network is routed through the VPN tunnel, while Internet-bound traffic is routed directly to the Internet.

QUESTION NO: 577
Answer: C. Native VLAN
Explanation: To resolve the issue of VoIP phone connections cutting in and out, configuring the native VLAN correctly is important. The native VLAN is the VLAN to which untagged frames are assigned. Ensuring that VoIP traffic is correctly tagged and assigned to the appropriate VLAN can help improve VoIP performance.

QUESTION NO: 578
Answer: C. Set a private community string.
             D. Use SNMPv3.
Explanation: The BEST ways for the administrator to secure this type of traffic are:
- Set a private community string: This ensures that SNMP traffic is secured by requiring devices to use a specific community string for authentication.
- Use SNMPv3: SNMP version 3 provides enhanced security features, including encryption and authentication, to protect SNMP traffic from unauthorized access and tampering.

QUESTION NO: 579
Answer: B. Virtual machines
Explanation: Virtual machines (VMs) assist a network administrator in reverse engineering malware and viruses by providing isolated environments for analysis. VM snapshots can be taken before running potentially malicious software, allowing for easy rollback and analysis of changes made by the malware.

QUESTION NO: 580
Answer: A. The lab environment's IDS is blocking the network traffic. The technician can whitelist the new application in the IDS.
Explanation: The most likely reason the web server cannot retrieve files from the company's file server is that the lab environment's Intrusion Detection System (IDS) is blocking the network traffic. To resolve the problem, the technician should whitelist the new application in the IDS to allow its traffic to pass through without being blocked.
''')
