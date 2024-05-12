print('''
QUESTION NO: 291
A company wants to implement a disaster recovery site for non-critical applications, which
can tolerate a short period of downtime. Which of the following types of sites should the
company implement to achieve this goal?
A. Hot
B. Cold
C. Warm
D. Passive

QUESTION NO: 292
A network technician wants to find the shortest path from one node to every other node in the
network. Which of the following algorithms will provide the FASTEST convergence time?
A. A static algorithm
B. A link-state algorithm
C. A distance-vector algorithm
D. A path-vector algorithm

QUESTION NO: 293
Which of the following would be used to forward requests and replies between a DHCP
server and client?
A. Relay
B. Lease
C. Scope
D. Range

QUESTION NO: 294
Users within a corporate network need to connect to the Internet, but corporate network
policy does not allow direct connections. Which of the following is MOST likely to be used?
A. Proxy server
B. VPN client
C. Bridge
D. VLAN

QUESTION NO: 295
Which of the following can be used to decrease latency during periods of high utilization of a
firewall?
A. Hot site
B. NIC teaming
C. HA pair
D. VRRP

QUESTION NO: 296
A rogue AP was found plugged in and providing Internet access to employees in the break
room.
Which of the following would be BEST to use to stop this from happening without physically
removing the WAP?
A. Password complexity
B. Port security
C. Wireless client isolation
D. Secure SNMP

QUESTION NO: 297
A network administrator is reviewing north-south traffic to determine whether a security threat
exists. Which of the following explains the type of traffic the administrator is reviewing?
A. Data flowing between application servers
B. Data flowing between the perimeter network and application servers
C. Data flowing in and out of the data center
D. Data flowing between local on-site support and backup servers

QUESTION NO: 298
The process of attempting to exploit a weakness in a network after being given permission by
the company is known as:
A. penetration testing
B. vulnerability scanning
C. reconnaissance
D. social engineering

QUESTION NO:299
Check Question NO:2999 for the simulation

QUESTION NO: 300
A security vendor needs to add a note to the DNS to validate the ownership of a company
domain before services begin. Which of the following records did the security company
MOST likely ask the company to configure?
A. TXT
B. AAAA
C. CNAME
D. SRV''')
answer = input(print("Do you have your answers"))
if answer == "yes":
    print('''

NO:291 = C\nExplanation: A warm site is appropriate for non-critical applications that can tolerate a short period of downtime. It is less expensive than a hot site and requires less setup time than a cold site.

NO:292 = B\nExplanation: Link-state algorithms, such as OSPF or IS-IS, provide the fastest convergence time in finding the shortest path from one node to every other node in a network by maintaining a full map of the network.

NO:293 = A\nExplanation: A DHCP relay agent (or DHCP relay) is used to forward DHCP messages between clients and servers when they are not on the same physical subnet, allowing clients to obtain IP addresses and configuration information from DHCP servers located on different subnets.

NO:294 = A\nExplanation: A proxy server allows users within a corporate network to access the Internet indirectly, enforcing corporate policies by filtering and caching web content and enhancing security.

NO:295 = B\nExplanation: NIC teaming combines multiple network interfaces into a single logical interface, distributing network traffic across multiple NICs to increase bandwidth and decrease latency during periods of high utilization of a firewall.

NO:296 = C\nExplanation: Wireless client isolation prevents wireless clients connected to the same access point from communicating directly with each other, mitigating the risk posed by rogue access points without physically removing them.

NO:297 = C\nExplanation: "North-south" traffic refers to data flowing in and out of the data center, allowing the network administrator to monitor and analyze traffic entering and leaving the organization's network to identify potential security threats.

NO:298 = A\nExplanation: Penetration testing involves attempting to exploit weaknesses in a network with permission from the company to assess the security posture and improve defenses.

NO:299 = Check question number 299 for the simulation

NO:300 = A\nExplanation: A TXT (Text) record in DNS is used for various purposes, including domain ownership validation, by storing arbitrary text information associated with a domain.
''')
