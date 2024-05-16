print('''
QUESTION NO: 711
At the destination host, which of the following OSI model layers will discard a segment with a
bad checksum in the UDP header?
A. Network
B. Data link
C. Transport
D. Session

QUESTION NO: 712
Branch users are experiencing issues with videoconferencing. Which of the following will the
company MOST likely configure to improve performance for these applications?
A. Link Aggregation Control Protocol
B. Dynamic routing
C. Quality of service
D. Network load balancer
E. Static IP addresses

QUESTION NO: 713
A network administrator is configuring a new switch and wants to ensure that only assigned
devices can connect to the switch. Which of the following should the administrator do?
A. Configure ACLs.
B. Implement a captive portal.
C. Enable port security.
D. Disable unnecessary services.

QUESTION NO: 714
Which of the following would be BEST suited for a long cable run with a 40Gbps bandwidth?
A. Cat 5e
B. Cat 6a
C. Cat 7
D. Cat 8

QUESTION NO: 715
Which of the following technologies allows traffic to be sent through two different ISPs to
increase performance?
A. Fault tolerance
B. Quality of service
C. Load balancing
D. Port aggregation

QUESTION NO: 716
An engineer notices some late collisions on a half-duplex link. The engineer verifies that the
devices on both ends of the connection are configured for half duplex. Which of the following
is the MOST likely cause of this issue?
A. The link is improperly terminated
B. One of the devices is misconfigured
C. The cable length is excessive
D. One of the devices has a hardware issue

QUESTION NO: 717
802.11n clients currently have no way to connect to the network. Which of the following
devices should be implemented to let the clients connect?
A. Router
B. Range extender
C. VoIP endpoint
D. Access point

QUESTION NO: 718
An older web server on a screened subnet is serving unencrypted web traffic. The server is
not capable of serving HTTPS traffic directly, but the firewall is capable of doing so. Which of
the following should be done to encrypt all traffic coming into the web server from outside the
network? (Choose two.)
A. A certificate should be installed on the server.
B. Incoming port 80 traffic at the firewall should be forwarded to port 443 on the server.
C. Incoming port 80 traffic at the firewall should be forwarded to port 80 on the server.
D. Incoming port 443 traffic at the firewall should be forwarded to port 80 on the server.
E. A certificate should be installed on the firewall.
F. A proxy server should be installed on the screened subnet.

QUESTION NO: 719
A network engineer is investigating reports of poor performance on a videoconferencing
application. Upon reviewing the report, the engineer finds that available bandwidth at the
WAN connection is low. Which of the following is the MOST appropriate mechanism to
handle this issue?
A. Traffic shaping
B. Flow control
C. NetFlow
D. Link aggregation

QUESTION NO: 720
A network administrator wants to control new router deployments via the use of application
programming interfaces (APIs). This would be an example of:
A. software-defined networking.
B. a three-tiered architecture.
C. collapsed backbone.
D. top-of-rack switching.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Here are the answers with explanations:

QUESTION NO: 711
Answer: C. Transport
Explanation: The UDP checksum is validated at the Transport layer (Layer 4) of the OSI model. If the checksum is bad, the segment will be discarded at this layer.

QUESTION NO: 712
Answer: C. Quality of service
Explanation: Quality of Service (QoS) mechanisms can prioritize video conferencing traffic, ensuring it receives sufficient bandwidth and low latency, thereby improving performance for these applications.

QUESTION NO: 713
Answer: C. Enable port security.
Explanation: Port security allows the administrator to restrict access to a switch port based on the MAC addresses of the connected devices, ensuring only assigned devices can connect.

QUESTION NO: 714
Answer: D. Cat 8
Explanation: Cat 8 cables are designed to support high bandwidths and are best suited for long cable runs with 40Gbps bandwidth.

QUESTION NO: 715
Answer: C. Load balancing
Explanation: Load balancing distributes network traffic across multiple ISPs, allowing traffic to be sent through different ISPs simultaneously to increase performance.

QUESTION NO: 716
Answer: B. One of the devices is misconfigured
Explanation: Late collisions on a half-duplex link often occur due to misconfiguration on one of the devices, such as incorrect duplex settings.

QUESTION NO: 717
Answer: D. Access point
Explanation: Access points are used to provide wireless connectivity for clients like 802.11n devices, allowing them to connect to the network wirelessly.

QUESTION NO: 718
Answers: B. Incoming port 80 traffic at the firewall should be forwarded to port 443 on the server.
                 E. A certificate should be installed on the firewall.
Explanation: Forwarding port 80 traffic to port 443 at the firewall enables HTTPS encryption, and installing a certificate on the firewall ensures secure communication between the firewall and clients accessing the server.

QUESTION NO: 719
Answer: A. Traffic shaping
Explanation: Traffic shaping can control bandwidth usage, ensuring critical applications like video conferencing receive sufficient bandwidth even with low available WAN bandwidth.

QUESTION NO: 720
Answer: A. Software-defined networking.
Explanation: Using APIs to control router deployments aligns with the principles of software-defined networking (SDN), where network functionality is controlled programmatically through software.
''')
