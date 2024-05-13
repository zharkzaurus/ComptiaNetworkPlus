print('''
QUESTION NO: 421
An organization wants to perform maintenance on any of its web servers without affecting the
service availability during a scheduled change window. Which of the following network
devices would be required to provide this functionality?
A. Router
B. Forward proxy
C. Load balancer
D. Firewall

QUESTION NO: 422
A network administrator decided to use SLAAC in an extensive IPv6 deployment to alleviate
IP address management. The devices were properly connected into the LAN but
autoconfiguration of the IP address did not occur as expected. Which of the following should
the network administrator verify?
A. The network gateway is configured to send router advertisements.
B. A DHCP server is present on the same broadcast domain as the clients.
C. The devices support dual stack on the network layer.
D. The local gateway supports anycast routing.

QUESTION NO: 423
A technician recently set up a small office network for nine users. When the installation was
complete, all the computers on the network showed addresses ranging from 169.254.0.0 to
169.254.255.255. Which of the following types of address ranges does this represent?
A. Private
B. Public
C. APIPA
D. Classless

QUESTION NO: 424
A network engineer turned on logging to assist with troubleshooting a suspected
configuration issue. Which of the following would provide the network engineer with the most
informative log information?
A. FATAL
B. ERROR
C. DEBUG
D. WARN

QUESTION NO: 425
Which of the following most likely determines the size of a rack for installation? (Choose two.)
A. KVM size
B. Switch depth
C. Hard drive size
D. Cooling fan speed
E. Outlet amperage
F. Server height

QUESTION NO: 426
Which of the following communication modes has the LOWEST overhead necessary to
support streaming protocols such as RTP?
A. Connectionless
B. Stateful
C. Full Duplex
D. Quality of Service

QUESTION NO: 427
Which of the following is the DNS feature that controls how long a lookup is stored in cache
on a server?
A. CNAME
B. TTL
C. SOA
D. SRV

QUESTION NO: 428
A company needs to virtualize a replica of its internal physical network without changing the
logical topology and the way that devices behave and are managed. Which of the following
technologies meets this requirement?
A. NVF
B. SDWAN
C. VIP
D. MPLS

QUESTION NO: 429
Which of the following would be best suited for use at the access layer in a three-tier
architecture system?
A. Router
B. Multilayer switch
C. Layer 2 switch
D. Access point

QUESTION NO: 430
Which of the following ports is a secure protocol?
A. 20
B. 23
C. 443
D. 445
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 421
Answer: C
Explanation: To perform maintenance on web servers without affecting service availability, a load balancer would be required. Load balancers distribute incoming traffic across multiple servers, ensuring high availability and scalability by directing requests only to servers that are online and healthy. During maintenance on one server, the load balancer can redirect traffic to other available servers, minimizing downtime.

NO: 422
Answer: A
Explanation: In an extensive IPv6 deployment using SLAAC (Stateless Address Autoconfiguration), the network gateway needs to be configured to send router advertisements (RA). Router advertisements are used to announce network prefixes and other configuration parameters to hosts on the local network, enabling them to configure their IPv6 addresses automatically.

NO: 423
Answer: C
Explanation: The address range 169.254.0.0 to 169.254.255.255 represents the Automatic Private IP Addressing (APIPA) range. APIPA addresses are self-assigned IPv4 addresses used when a DHCP server is not available to assign IP addresses dynamically. This range is reserved for local communication within a subnet and is not routable on the internet.

NO: 424
Answer: C
Explanation: For troubleshooting purposes, the network engineer would likely obtain the most informative log information by setting the log level to DEBUG. DEBUG level logging provides detailed information about the system's operation, including debug messages that can help diagnose configuration issues and trace the flow of execution through the system.

NO: 425
Answer: B, F
Explanation: The size of a rack for installation is primarily determined by the depth of the switches (B) and the height of the servers (F). The depth of the switches is important to ensure they fit within the rack without protruding, while the height of the servers determines how many units (U) of rack space they will occupy vertically.

NO: 426
Answer: A
Explanation: The connectionless communication mode has the lowest overhead necessary to support streaming protocols such as Real-Time Transport Protocol (RTP). In a connectionless mode, each packet is sent independently without establishing a dedicated connection, making it efficient for real-time streaming where low latency and minimal overhead are critical.

NO: 427
Answer: B
Explanation: Time-To-Live (TTL) is the DNS feature that controls how long a lookup is stored in cache on a server. TTL specifies the amount of time, in seconds, that a DNS resolver caches the response for a DNS query before it expires and needs to be refreshed by querying the authoritative DNS server again.

NO: 428
Answer: A
Explanation: Network Function Virtualization (NFV) allows the virtualization of network services without changing the logical topology and the way that devices behave and are managed. NFV enables the deployment of virtual network functions (VNFs) on standard server hardware, providing flexibility, scalability, and cost savings compared to traditional physical network appliances.

NO: 429
Answer: C
Explanation: In a three-tier architecture system, the Layer 2 switch would be best suited for use at the access layer. The access layer connects end devices such as computers, printers, and access points to the network. Layer 2 switches operate at the data link layer and provide basic connectivity and VLAN support at the access layer.

NO: 430
Answer: C
Explanation: Port 443 is associated with the HTTPS (HTTP Secure) protocol, which is a secure protocol used for secure communication over a computer network. HTTPS encrypts the data exchanged between a web server and a client's browser, providing a secure connection for transmitting sensitive information such as login credentials and financial transactions.
''')
