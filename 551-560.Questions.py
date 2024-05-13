print('''
QUESTION NO: 551
An engineer needs to verify the external record for SMTP traffic. The engineer logged in to
the server and entered the nslookup command. Which of the following commands should the
engineer send before entering the DNS name?
A. set type=A
B. ls -d company.mail.com
C. set domain=company.mail.com
D. set querytype=MX

QUESTION NO: 552
A SaaS provider has decided to leave an unpatched VM available via a public DMZ port.
With which of the following concepts is this technique MOST closely associated?
A. Insider threat
B. War driving
C. Evil twin
D. Honeypot

QUESTION NO: 553
A network administrator is looking at switch features and is unsure whether to purchase a
model with PoE. Which of the following devices that commonly utilize PoE should the
administrator consider? (Choose two.)
A. VoIP phones
B. Cameras
C. Printers
D. Cable modems
E. Laptops
F. UPSs

QUESTION NO: 554
A user is experimenting with audio transmissions and would like the transmissions to reach
several specific devices simultaneously over the IP network. The user requests assistance
from a network technician to configure the appropriate features within the SOHO. Which of
the following should the technician configure to meet the requirements?
A. Unicast
B. Multicast
C. Anycast
D. Broadcast

QUESTION NO: 555
A company is implementing a secure remote access solution for multiple employees. Which
of the following should the company use?
A. Remote desktop connection
B. Virtual desktop
C. Site-to-site VPN
D. Client-to-site VPN

QUESTION NO: 556
A technician needs to allow a device to maintain the same IP address lease based on the
physical address of a network card. Which of the following should the technician use?
A. MAC address reservation
B. Static IP address
C. Custom DNS server entry
D. IP address exclusion

QUESTION NO: 557
At which of the following OSI model layers would a technician find an IP header?
A. Layer 1
B. Layer 2
C. Layer 3
D. Layer 4

QUESTION NO: 558
A user from a remote office is reporting slow file transfers. Which of the following tools will an
engineer MOST likely use to get detailed measurement data?
A. Packet capture
B. iPerf
C. NetFlow analyzer
D. Internet speed test

QUESTION NO: 559
Which of the following physical security methods Is the MOST effective to prevent tailgating?
A. Biometrics in an access control vestibule
B. IP cameras with motion detection
C. Smart lockers with tamper protection
D. Badge readers plus a PIN pad

QUESTION NO: 560
Which of the following is the most secure way to provide site-to-site connectivity?
A. VXLAN
B. IKE
C. GRE
D. IPSec
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 551
Answer: A
Explanation: set type=A
Before entering the DNS name in nslookup, the engineer should use the "set type=A" command to specify the query type as an A record. This command tells nslookup to query for the IPv4 address associated with the DNS name.

QUESTION NO: 552
Answer: D
Explanation: Honeypot
Leaving an unpatched VM available via a public DMZ port is most closely associated with the concept of a honeypot. A honeypot is a security mechanism set up to detect, deflect, or counteract attempts at unauthorized use of information systems. It is deliberately left vulnerable to attract attackers and gather information about their methods and motives.

QUESTION NO: 553
Answer: A, B
Explanation: VoIP phones, Cameras
Devices that commonly utilize Power over Ethernet (PoE) include VoIP phones and cameras. PoE enables these devices to receive power and data over the same Ethernet cable, simplifying installation and reducing the need for separate power sources.

QUESTION NO: 554
Answer: B. Multicast
Explanation: Multicast
To transmit audio transmissions to several specific devices simultaneously over the IP network, the technician should configure multicast. Multicast allows for the efficient distribution of data to multiple recipients simultaneously, making it suitable for applications such as audio and video streaming.

QUESTION NO: 555
Answer: D. Client-to-site VPN
Explanation: Client-to-site VPN
For secure remote access for multiple employees, the company should use a client-to-site VPN (Virtual Private Network). This type of VPN allows individual users to securely connect to the company's network from remote locations over the internet.

QUESTION NO: 556
Answer: A. MAC address reservation
Explanation: MAC address reservation
To allow a device to maintain the same IP address lease based on the physical address of a network card, the technician should use MAC address reservation. This feature in DHCP (Dynamic Host Configuration Protocol) allows specific IP addresses to be assigned to devices based on their MAC addresses.

QUESTION NO: 557
Answer: C. Layer 3
Explanation: Layer 3
An IP header is found at Layer 3 of the OSI model. Layer 3, the Network Layer, is responsible for routing packets across different networks. The IP header contains information such as source and destination IP addresses, as well as other control information required for packet routing.

QUESTION NO: 558
Answer: C. NetFlow analyzer
Explanation: NetFlow analyzer
To get detailed measurement data about slow file transfers from a remote office, an engineer would most likely use a NetFlow analyzer. NetFlow is a network protocol used for collecting IP traffic information. A NetFlow analyzer provides detailed insights into network traffic patterns, including bandwidth usage, application performance, and network bottlenecks.

QUESTION NO: 559
Answer: A. Biometrics in an access control vestibule
Explanation: Biometrics in an access control vestibule
The most effective physical security method to prevent tailgating is biometrics in an access control vestibule. Biometric systems use unique physical characteristics such as fingerprints or iris patterns to verify a person's identity before granting access. Placing biometric scanners in an access control vestibule ensures that only authorized individuals can enter, preventing tailgating.

QUESTION NO: 560
Answer: D. IPSec
Explanation: IPSec
The most secure way to provide site-to-site connectivity is IPSec (Internet Protocol Security). IPSec is a suite of protocols used to secure internet communications by authenticating and encrypting each IP packet of a communication session. It provides robust security for site-to-site VPNs, ensuring confidentiality, integrity, and authenticity of data transmitted between network locations.
''')
