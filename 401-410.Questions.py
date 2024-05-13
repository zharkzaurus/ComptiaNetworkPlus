print('''
QUESTION NO: 401
Which of the following will reduce routing table lookups by performing packet forwarding
decisions independently of the network layer header?
A. MPLS
B. mGRE
C. EIGRP
D. VRRP

QUESTION NO: 402
Which of the following types of devices can provide content filtering and threat protection,
and manage multiple IPSec site-to-site connections?
A. Layer 3 switch
B. VPN headend
C. Next-generation firewall
D. Proxy server
E. Intrusion prevention

QUESTION NO: 403
Which of the following is a requirement when certifying a network cabling as Cat 7?
A. Ensure the patch panel is certified for the same category.
B. Limit 10Gb transmissions to 180ft (55m).
C. Use F-type connectors on the network terminations.
D. Ensure the termination standard is TIA/EIA-568-A.

QUESTION NO: 404
Look at question Number 404 to look at the simulator

QUESTION NO: 405
Which of the following protocols is widely used in large-scale enterprise networks to support
complex networks with multiple routers and balance traffic load on multiple links?
A. OSPF
B. RIPv2
C. QoS
D. STP

QUESTION NO: 406
Which of the following WAN transmission mediums is the fastest and can travel the longest
distance?
A. Satellite
B. Copper
C. Wireless
D. Fiber

QUESTION NO: 407
Which of the following devices have the capability to allow communication between two
different subnetworks? (Select TWO).
A. IDS
B. Access point
C. Layer 2 switch
D. Layer 3 switch
E. Router
F. Media converter

QUESTION NO: 408
A new student is given credentials to log on to the campus Wi-Fi. The student stores the
password in a laptop and is able to connect; however, the student is not able to connect with
a phone when only a short distance from the laptop. Given the following information:
 | Signal strength               | 90% |
 | Coverage                      | 80% |
 | Interference                  | 15% |
 | Number of connection attempts | 10  |
Which of the following is MOST likely causing this connection failure?
A. Transmission speed
B. Incorrect passphrase
C. Channel overlap
D. Antenna cable attenuation/signal loss

QUESTION NO: 409
Which of the following topologies requites the MOST connections when designing a network?
A. Mesh
B. Star
C. Bus
D. Ring

QUESTION NO: 410
A client has just leased a new office space in a busy commercial building and would like to
install a wireless network. Several other tenants are on the same floor. Multiple wireless
networks are present in the building. Which of the following can be changed on the client's
wireless network to help ensure that interference from other wireless networks is at a
minimum?
A. WPA encryption key selection
B. Channel selection
C. Antenna types
D. Disable SSID
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 401
Answer: A
Explanation: MPLS (Multiprotocol Label Switching) will reduce routing table lookups by performing packet forwarding decisions independently of the network layer header. MPLS adds a label to packets at the network layer, allowing routers to forward packets based on labels rather than examining the network layer header.

NO: 402
Answer: C
Explanation: Next-generation firewalls can provide content filtering and threat protection, as well as manage multiple IPSec site-to-site connections. These firewalls incorporate advanced security features such as intrusion prevention, application control, and SSL inspection, making them suitable for securing enterprise networks.

NO: 403
Answer: A
Explanation: When certifying a network cabling as Cat 7, it is a requirement to ensure the patch panel is certified for the same category. The patch panel plays a crucial role in maintaining the performance and integrity of the Cat 7 cabling infrastructure.

NO: 405
Answer: A
Explanation: OSPF (Open Shortest Path First) is widely used in large-scale enterprise networks to support complex networks with multiple routers and balance traffic load on multiple links. OSPF is a dynamic routing protocol that calculates the shortest path to destination networks based on link-state information.

NO: 406
Answer: D
Explanation: Fiber is the fastest WAN transmission medium and can travel the longest distance compared to other options. Fiber optic cables transmit data using light signals through glass or plastic fibers, offering high bandwidth and low latency over long distances.

NO: 407
Answer: D, E
Explanation: Layer 3 switches and routers have the capability to allow communication between two different subnetworks. They operate at the network layer of the OSI model and can route traffic between different IP subnets.

NO: 408
Answer: C
Explanation: Channel overlap is most likely causing this connection failure. Channel overlap occurs when neighboring Wi-Fi networks use overlapping channels, leading to interference and degraded performance. Adjusting the Wi-Fi channel to a less congested one can help alleviate this issue.

NO: 409
Answer: A
Explanation: A mesh network topology requires the most connections when designing a network. In a mesh topology, each node is connected to every other node, resulting in a fully interconnected network. This redundancy ensures robustness but requires a large number of connections.

NO: 410
Answer: B
Explanation: Channel selection can be changed on the client's wireless network to help ensure that interference from other wireless networks is at a minimum. By selecting a less congested channel, the client's wireless network can avoid interference from neighboring networks on the same frequency band.
''')
