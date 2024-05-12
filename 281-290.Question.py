print('''
QUESTION NO: 281
A company built a new building at its headquarters location. The new building is connected to
the company's LAN via fiber-optic cable. Multiple users in the new building are unable to
access the company's intranet site via their web browser, but they are able to access internet
sites. Which of the following describes how the network administrator can resolve this issue?
A. Correct the DNS server entries in the DHCP scope
B. Correct the external firewall gateway address
C. Correct the NTP server settings on the clients
D. Correct a TFTP Issue on the company's server

QUESTION NO: 282
A technician is utilizing SNMPv3 to monitor network statistics. Which of the following actions
would occur immediately of a server's utilization spikes above the prescribed value?
A. A trap message is sent via UDP to the monitoring workstation.
B. The SET function pushes an alert to the MIB database.
C. The object identifier is modified and reported during the next monitoring cycle.
D. A response message is sent from the agent to the manager.

QUESTION NO: 283
Which of the following types of planes propagates routing information in an SDWAN solution
?
A. Orchestration plane
B. Management plane
C. Control plane
D. Data plane

QUESTION NO: 284
A hacker used a packet sniffer on the network to capture the hardware address of the server.
Which of the following types of attacks can the hacker perform now?
A. Piggybacking
B. MAC spoofing
C. Evil twin
D. VLAN hopping

QUESTION NO: 285
An employee walked into a secure facility and allowed a newly hired employee to walk in as
well.
Which of the following is the BEST solution to prevent this from happening again?
A. "No tailgating" sign
B. Awareness training
C. Entry log
D. Camera

QUESTION NO: 286
Which of the following BEST describes a split-tunnel client-to-server VPN connection?
A. The client sends all network traffic down the VPN tunnel.
B. The client has two different IP addresses that can be connected to a remote site from two
different ISPs to ensure availability.
C. The client sends some network traffic down the VPN tunnel and other traffic to the local
gateway.
D. The client connects to multiple remote sites at the same time.

QUESTION NO: 287
The address 6FFE:FFFF:0000:2F3B:04AC:00FF:FEBE:5C4A is an example of which of the
following?
A. APIPA
B. MAC
C. IPv4
D. IPv6

QUESTION NO: 288
A technician needs to configure a routing protocol for an internet-facing edge router. Which of
the following routing protocols will the technician MOST likely use?
A. BGP
B. RIPv2
C. OSPF
D. EIGRP

QUESTION NO: 289
A corporate client is experiencing global system outages. The IT team has identified multiple
potential underlying causes throughout the enterprise. Each team member has been
assigned an area to troubleshoot. Which of the following approaches is being used?
A. Divide-and-conquer
B. Top-to-bottom
C. Bottom-to-top
D. Determine if anything changed

QUESTION NO: 290
A security administrator is trying to prevent incorrect IP addresses from being assigned to
clients on the network. Which of the following would MOST likely prevent this and allow the
network to continue to operate?
A. Configuring DHCP snooping on the switch
B. Preventing broadcast messages leaving the client network
C. Blocking ports 67/68 on the client network
D. Enabling port security on access ports''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO:281 = A
Explanation: Correcting the DNS server entries in the DHCP scope would ensure that the users in the new building can resolve the company's intranet site domain names to their corresponding IP addresses.

NO:282 = A
Explanation: With SNMPv3, when a server's utilization spikes above the prescribed value, a trap message is immediately sent via UDP to the monitoring workstation, alerting the administrator to the issue.

NO:283 = C
Explanation: In an SDWAN solution, the control plane propagates routing information, determining the best paths for traffic based on network conditions and policies.

NO:284 = B
Explanation: After capturing the server's hardware address, the hacker can perform MAC spoofing, where they impersonate the server by altering their own MAC address to match that of the server.

NO:285 = B
Explanation: Providing awareness training to employees is the best solution to prevent unauthorized individuals from gaining access to secure facilities by exploiting the trust of employees.

NO:286 = C
Explanation: In a split-tunnel client-to-server VPN connection, the client sends some network traffic down the VPN tunnel while other traffic is routed to the local gateway, allowing for more efficient use of network resources.

NO:287 = D
Explanation: The given address is an example of an IPv6 address, as it follows the format defined for IPv6 addresses.

NO:288 = A
Explanation: Border Gateway Protocol (BGP) is commonly used for routing on internet-facing edge routers due to its scalability and ability to handle complex routing policies and multiple paths to destinations.

NO:289 = A
Explanation: The approach being used is "divide-and-conquer," where each team member is assigned a specific area to troubleshoot, allowing for efficient problem-solving by focusing on individual components or areas of the enterprise.

NO:290 = A
Explanation: Configuring DHCP snooping on the switch would prevent incorrect IP addresses from being assigned to clients by monitoring DHCP messages and only allowing trusted DHCP servers to respond to client requests, ensuring network integrity.
''')
