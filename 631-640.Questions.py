print('''
QUESTION NO: 631
Users are reporting performance issues when attempting to access the main fileshare server.
Which of the following steps should a network administrator perform NEXT based on the
network troubleshooting methodology?
A. Implement a fix to resolve the connectivity issues.
B. Determine if anything has changed.
C. Establish a theory of probable cause.
D. Document all findings, actions, and lessons learned.

QUESTION NO: 632
MIMO technology in the 802.11n standard provides for which of the following benefits?
A. Channel expansion
B. Gigabit wireless bandwidth
C. Multipath support
D. Channel bonding

QUESTION NO: 633
A technician reviews a network performance report and finds a high level of collisions
happening on the network. At which of the following layers of the OSI model would these
collisions be found?
A. Layer 1
B. Layer 3
C. Layer 4
D. Layer 7

QUESTION NO: 634
An engineer is designing a network topology for a company that maintains a large on-
premises private cloud. A design requirement mandates internet-facing hosts to be
partitioned off from the internal LAN and internal server IP ranges. Which of the following
defense strategies helps meet this requirement?
A. Implementing a screened subnet
B. Deploying a honeypot
C. Utilizing network access control
D. Enforcing a Zero Trust model

QUESTION NO: 635
A network administrator is trying to add network redundancy for the server farm. Which of the
following can the network administrator configure to BEST provide this capability?
A. VRRP
B. DNS
C. UPS
D. RPO

QUESTION NO: 636
Logs show an unauthorized IP address entering a secure part of the network every night at
8:00 pm. The network administrator is concerned that this IP address will cause an issue to a
critical server and would like to deny the IP address at the edge of the network.
Which of the following solutions would address these concerns?
A. Changing the VLAN of the web server
B. Changing the server's IP address
C. Implementing an ACL
D. Instating a rule on the firewall connected to the web server

QUESTION NO: 637
A technician is equipped with a tablet, a smartphone, and a laptop to troubleshoot a switch
with the help of support over the phone. However, the technician is having issues
interconnecting all these tools in troubleshooting the switch. Which of the following should the
technician use to gain connectivity?
A. PAN
B. WAN
C. LAN
D. MAN

QUESTION NO: 638
Which of the following can be used to aggregate logs from different devices and would make
analysis less difficult?
A. Syslog
B. SIEM
C. Event logs
D. NetFlow

QUESTION NO: 639
To comply with an industry regulation, all communication destined to a secure server should
be logged and archived on a storage device. Which of the Mowing can be configured to fulfill
this requirement?
A. QoS traffic classification
B. Port mirroring
C. Flow control
D. Link Aggregation Control Protocol

QUESTION NO: 640
An administrator wants to increase the availability of a server that is connected to the office
network. Which of the following allows for multiple NICs to share a single IP address and
offers maximum performance while providing fault tolerance in the event of a NIC failure?
A. Multipathing
B. Spanning Tree Protocol
C. First Hop Redundancy Protocol
D. Elasticity
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 631
Answer: B. Determine if anything has changed.
Explanation: In the network troubleshooting methodology, the next step after users report performance issues with accessing the main fileshare server is to determine if anything has changed. Changes in the network environment, such as configuration updates, hardware additions or modifications, or software changes, can often be the cause of performance issues. By identifying any recent changes, the network administrator can narrow down potential causes and proceed with troubleshooting more effectively.

QUESTION NO: 632
Answer: C. Multipath support
Explanation: MIMO (Multiple Input Multiple Output) technology in the 802.11n standard provides for the benefit of multipath support. MIMO enables multiple antennas to transmit and receive multiple data streams simultaneously, exploiting multipath propagation to improve wireless communication performance by reducing fading and increasing data throughput.

QUESTION NO: 633
Answer: A. Layer 1
Explanation: Collisions occur at Layer 1 (the physical layer) of the OSI model. Layer 1 deals with the physical transmission of data over the network medium, including the signaling of bits and the management of physical connections. Collisions can occur when two devices attempt to transmit data simultaneously on a shared medium, resulting in signal interference.

QUESTION NO: 634
Answer: A. Implementing a screened subnet
Explanation: Implementing a screened subnet, also known as a DMZ (Demilitarized Zone), helps meet the design requirement of partitioning internet-facing hosts from the internal LAN and server IP ranges. A DMZ provides an additional layer of security by placing internet-facing servers in a separate network segment, isolated from the internal network, while still allowing controlled access from the internet.

QUESTION NO: 635
Answer: A. VRRP
Explanation: To provide network redundancy for the server farm, the network administrator can configure Virtual Router Redundancy Protocol (VRRP). VRRP allows multiple routers or gateways to share a virtual IP address, providing failover capabilities in the event of a router or gateway failure. This ensures uninterrupted access to network resources for clients even if one router fails.

QUESTION NO: 636
Answer: D. Instating a rule on the firewall connected to the web server
Explanation: To address the concerns of unauthorized IP address access to a secure part of the network, the network administrator should instate a rule on the firewall connected to the web server. By configuring a firewall rule, the administrator can deny traffic from the unauthorized IP address at the network perimeter, preventing it from reaching the critical server.

QUESTION NO: 637
Answer: A. PAN
Explanation: The technician should use a Personal Area Network (PAN) to interconnect the tablet, smartphone, and laptop for troubleshooting the switch. A PAN allows devices in close proximity to communicate with each other wirelessly using technologies such as Bluetooth or Wi-Fi Direct.

QUESTION NO: 638
Answer: B. SIEM
Explanation: A Security Information and Event Management (SIEM) system can be used to aggregate logs from different devices and make analysis less difficult. SIEM solutions collect, store, and analyze log and event data from various sources across the network, providing centralized visibility into security events and facilitating efficient threat detection and response.

QUESTION NO: 639
Answer: B. Port mirroring
Explanation: Port mirroring can be configured to fulfill the requirement of logging and archiving all communication destined to a secure server. Port mirroring, also known as SPAN (Switched Port Analyzer), copies traffic from one or more switch ports to another port for monitoring and analysis purposes, allowing network administrators to capture and archive communication data for compliance purposes.

QUESTION NO: 640
Answer: A. Multipathing
Explanation: Multipathing allows for multiple NICs (Network Interface Cards) to share a single IP address and offers maximum performance while providing fault tolerance in the event of a NIC failure. With multipathing, multiple network interfaces are configured to work together as a single logical interface, enabling load balancing and redundancy for improved availability and performance.       
''')
