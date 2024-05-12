print('''
QUESTION NO: 301
Given the following information:
| Protocol |   Local address  |  Foreign address  |    State    | 
|    TCP   | 127.0.0.1: 57779 | Desktop-Open:57780| Established |
|    TCP   | 127.0.0.1: 57780 | Desktop-Open:57779| Established |
Which of the following command-line tools would generate this output?
A. netstat
B. arp
C. dig
D. tracert

QUESTION NO: 302
A network engineer installed a new fiber uplink for an office and wants to make sure that the
link meets throughput requirements. Which of the following tools should the engineer use to
verify that the new link is sufficient?
A. tcpdump
B. ping
C. iperf
D. netstat

QUESTION NO: 303
Which of the following services provides the network information for the address when IPv6 is
used for SLAAC addressing?
A. DHCPv6
B. Router advertisement
C. EUI-64
D. IPv6 unicast routing

QUESTION NO: 304
A network administrator needs to provide remote clients with access to an internal web
application. Which of the following methods provides the HIGHEST flexibility and
compatibility while encrypting only the connection to the web application?
A. Clientless VPN
B. Virtual desktop
C. Virtual network computing
D. mGRE tunnel

QUESTION NO: 305
A network technician needs to determine the IPv6 address of a malicious website. Which of
the following record types would provide this information?
A. A
B. AAAA
C. CNAME
D. PTR

QUESTION NO: 306
A technician is troubleshooting a client's report about poor wireless performance. Using a
client monitor, the technician notes the following information:
|    SSID   | Signal (RSSI) | Channel |
| Corporate |      -50      |    9    |
| Corporate |      -69      |    10   |
| Corporate |      -67      |    11   |
| Corporate |      -63      |    6    |
Which of the following is MOST likely the cause of the issue?
A. Channel overlap
B. Poor signal
C. Incorrect power settings
D. Wrong antenna type

QUESTION NO: 307
Which of the following protocols is used to allow multiple hosts to share a common IP
address?
A. HTTPS
B. ARP
C. CARP
D. NAT

QUESTION NO: 308
A local service provider connected 20 schools in a large city with a fiber-optic switched
network.
Which of the following network types did the provider set up?
A. LAN
B. MAN
C. CAN
D. WAN

QUESTION NO: 309
A company has been given a Class C address to be utilized for all devices. The company has
several subnets and the largest subnet has 15 hosts. Which of the following represents the
MINIMUM CIDR notation of this subnet mask?
A. /26
B. /27
C. /28
D. /29

QUESTION NO: 310
An IT officer is installing a new WAP. Which of the following must the officer change to
connect users securely to the WAP?
A. AES encryption
B. Channel to the highest frequency within the band
C. TKIP encryption protocol
D. Dynamic selection of the frequency''')
answer = input(print("Do you have answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 301
Answer: A. netstat
Explanation: Netstat is a command-line tool used to display network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

QUESTION NO: 302
Answer: C. iperf
Explanation: Iperf is a tool used for measuring the maximum TCP and UDP bandwidth performance. It can be used to test throughput and quality of a network link.

QUESTION NO: 303
Answer: B. Router advertisement
Explanation: In IPv6 Stateless Address Autoconfiguration (SLAAC), router advertisement messages are used to provide network information to hosts, enabling them to generate their own addresses.

QUESTION NO: 304
Answer: A. Clientless VPN
Explanation: Clientless VPN allows remote clients to securely access internal resources through a web browser without requiring installation of a VPN client software.

QUESTION NO: 305
Answer: B. AAAA
Explanation: AAAA records (also known as IPv6 address records) provide IPv6 addresses associated with a domain name. 

QUESTION NO: 306
Answer: A. Channel overlap
Explanation: Channel overlap occurs when neighboring access points use the same or overlapping channels, causing interference and degraded wireless performance.

QUESTION NO: 307
Answer: D. NAT
Explanation: Network Address Translation (NAT) allows multiple hosts on a private network to share a single public IP address for accessing resources on the Internet.

QUESTION NO: 308
Answer: B. MAN
Explanation: MAN (Metropolitan Area Network) is a network that spans a larger geographic area than a LAN but smaller than a WAN, typically covering a city or town.

QUESTION NO: 309
Answer: C. /28
Explanation: A Class C address has a default subnet mask of /24. To accommodate 15 hosts, at least 4 additional bits are needed for host addresses, resulting in a subnet mask of /28 (32 - 28 = 4 bits for hosts).

QUESTION NO: 310
Answer: A. AES encryption
Explanation: AES (Advanced Encryption Standard) is a secure encryption algorithm commonly used for securing wireless connections. It provides strong encryption for WAP connections.
''')
