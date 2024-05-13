print('''
QUESTION NO: 601
Which of the following cable types would MOST likely be used to provide high-speed network
connectivity between nearby buildings?
A. UTP
B. Coaxial
C. Fiber
D. Cat 5
E. Twinaxial

QUESTION NO: 602
A technician needs to verify an Ethernet run is functioning properly.
Which of the following tools should be used?
A. Protocol analyzer
B. Crimper
C. Cable tester
D. Punch down tool

QUESTION NO: 603
A help desk engineer needs to configure two servers to have the same public IP addresses.
Which of the following technologies should the engineer use?
A. NAT
B. VIP
C. DNS caching
D. RFC 1918
E. SDWAN

QUESTION NO: 604
A disgruntled employee decides to leak critical information about a company's new product.
The employee places keyloggers on the department's computers, allowing the information to
be sent out to the Internet.
Which of the following attacks is occurring?
A. Man-in-the-middle
B. Logic bomb
C. Insider threat
D. Social engineering

QUESTION NO: 605
A new technician has been tasked with implementing a QoS policy for the Network. The
technician decides it would be best to monitor the information traversing the network to gain
statistical information on ports and protocols utilized. Which of the following tools should the
technician use to complete this objective QUICKEST?
A. Traffic analyzer
B. Network sniffer
C. SNMPv3
D. System logs

QUESTION NO: 606
Which of the following is used to prioritize Internet usage per application and per user on the
network?
A. Bandwidth management
B. Load balance routing
C. Border Gateway Protocol
D. Administrative distance

QUESTION NO: 607
In order to prepare for a fire or natural disaster, a Chief Executive Officer would like the
network administrator to set up a site with no equipment. Which of the following should the
network administrator set up?
A. A warm site
B. A cold site
C. A hot site
D. A site provided by the ISP

QUESTION NO: 608
Which of the following DNS record types is an alias?
A. CNAME
B. PTR
C. NS
D. SRV

QUESTION NO: 609
A network administrator is planning a WLAN for a soccer stadium and was advised to use
MU- MIMO to improve connection performance in high-density areas. The project requires
compatibility with clients connecting using 2.4GHz or 5GHz frequencies. Which of the
following would be the BEST wireless standard for this project?
A. 80211ac
B. 802.11ax
C. 802.11g
D. 80211n

QUESTION NO: 610
A network technician is considering opening ports on the firewall for an upcoming VoIP PBX
implementation. Which of the following protocols is the technician MOST likely to consider?
(Choose three.)
A. SIP
B. NTP
C. H.323
D. SMB
E. ICMP
F. RTP
G. IPSec
H. RDP
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 601
Answer: C. Fiber
Explanation: Fiber optic cable would most likely be used to provide high-speed network connectivity between nearby buildings. Fiber offers high bandwidth, low attenuation, and immunity to electromagnetic interference, making it suitable for long-distance and high-speed data transmission.

QUESTION NO: 602
Answer: C. Cable tester
Explanation: To verify an Ethernet run is functioning properly, a cable tester should be used. A cable tester checks the integrity of network cables by testing for continuity, wiring configuration, and any faults or breaks in the cable.

QUESTION NO: 603
Answer: B. VIP
Explanation: The help desk engineer should use Virtual IP (VIP) technology to configure two servers to have the same public IP addresses. VIP technology allows multiple servers to share the same IP address, providing redundancy and load balancing.

QUESTION NO: 604
Answer: C. Insider threat
Explanation: The scenario described involves an employee leaking critical information about the company's new product by placing keyloggers on department computers. This type of attack is known as an insider threat, where an individual with authorized access to an organization's network or systems deliberately causes harm or exposes sensitive information.

QUESTION NO: 605
Answer: B. Network sniffer
Explanation: The technician should use a network sniffer to monitor the information traversing the network and gain statistical information on ports and protocols utilized. A network sniffer captures and analyzes network traffic in real-time, providing insights into network behavior and usage patterns.

QUESTION NO: 606
Answer: A. Bandwidth management
Explanation: Bandwidth management is used to prioritize Internet usage per application and per user on the network. It allows network administrators to allocate bandwidth resources according to predefined policies and priorities.

QUESTION NO: 607
Answer: B. A cold site
Explanation: A cold site is a disaster recovery site that provides office space and infrastructure but does not have pre-installed IT equipment. It is typically less expensive to maintain than warm or hot sites but requires longer recovery times as equipment needs to be installed and configured in the event of a disaster.

QUESTION NO: 608
Answer: A. CNAME
Explanation: A CNAME (Canonical Name) record is an alias record used in DNS to map one domain name to another. It is commonly used to create aliases for existing domain names, allowing multiple domain names to resolve to the same IP address.

QUESTION NO: 609
Answer: B. 802.11ax
Explanation: 802.11ax would be the best wireless standard for the project because it supports MU-MIMO (Multi-User, Multiple Input, Multiple Output) technology, which improves connection performance in high-density areas. Additionally, 802.11ax is backward compatible with clients connecting using 2.4GHz or 5GHz frequencies.

QUESTION NO: 610
Answers:
A. SIP
C. H.323
F. RTP
Explanation: The technician would most likely consider opening ports for the following protocols related to VoIP PBX implementation:
- SIP (Session Initiation Protocol): Used for call setup, termination, and other signaling tasks.
- H.323: Another VoIP signaling protocol.
- RTP (Real-time Transport Protocol): Used for transmitting audio and video data in VoIP communications.
''')
