print('''
QUESTION NO: 591
A technician is concerned about unauthorized personnel moving assets that are installed in a
data center server rack. The technician installs a networked sensor that sends an alert when
the server rack door is opened. Which of the following did the technician install?
A. Cipher lock
B. Asset tags
C. Access control vestibule
D. Tamper detection

QUESTION NO: 592
Ann, a new user, is unable to communicate on the network from her computer. A technician
has verified that the cables are functioning properly. Based on the information below, which
action should the technician take to correct Ann's problem?
Computer_A Switch_A
IP: 10.0.0.60 Int VLAN10
SM: 255.255.255.0 IP address 10.0.0.1/28
GW: 10.0.0.1 Speed 100 Duplex Full
A. Change the duplex on the switch interface to half
B. Change the speed on the switch interface to 10Mbps
C. Change the subnet mask of the computer to 255.255.255.240
D. Change the IP address of the computer to 10.0.0.12

QUESTION NO: 593
A network technician is performing tests on a potentially faulty network card that is installed in
a server. Which of the following addresses will MOST likely be used during traffic diagnostic
tests?
A. 10.10.10.10
B. 127.0.0.1
C. 192.168.0.1
D. 255.255.255.0

QUESTION NO: 594
A user tries to ping 192.168.1.100 from the command prompt on the 192.168.2.101 network
but gets the following response: U.U.U.U. Which of the following needs to be configured for
these networks to reach each other?
A. Network address translation
B. Default gateway
C. Loopback
D. Routing protocol

QUESTION NO: 595
Which of the following routing protocols should be implemented to create a route between a
local area network and an ISP?
A. BGP
B. EIGRP
C. RIP
D. OSPF

QUESTION NO: 596
Which of the following can have multiple VLAN interfaces?
A. Hub
B. Layer 3 switch
C. Bridge
D. Load balancer

QUESTION NO: 597
Two network technicians are installing a fiber-optic link between routers. The technicians
used a light meter to verify the correct fibers. However, when they connect the fibers to the
router interface, the link does not connect. Which of the following would explain the issue?
(Choose two.)
A. They used the wrong type of fiber transceiver.
B. Incorrect TX/RX polarity exists on the link
C. The connection has duplexing configuration issues.
D. Halogen light fixtures are causing interference.
E. One of the technicians installed a loopback adapter.
F. The RSSI was not strong enough on the link

QUESTION NO: 598
Which of the following is used to limit the amount of bandwidth used on a link for different
applications to improve overall performance?
A. QoS
B. Fault tolerance
C. Load balancing
D. Traffic shaping

QUESTION NO: 599
A network technician needs to determine which RJ45 jack in a patch panel corresponds to
the RJ45 drop in the Chief Executive Officer's office. Which of the following tools would be
best for the technician to use?
A. Fusion splicer
B. Cable tester
C. Tone generator
D. Spectrum analyzer

QUESTION NO: 600
A network technician was hired to harden the security of a network. The technician is
required to enable encryption and create a password for AP security through the web
browser. Which of the following would BEST support these requirements?
A. ESP
B. WPA2
C. IPSec
D. ACL
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 591
Answer: D. Tamper detection
Explanation: The technician installed a networked sensor that sends an alert when the server rack door is opened. This type of sensor is used for tamper detection, which helps detect unauthorized access to server racks by sending alerts when the door is opened without authorization.

QUESTION NO: 592
Answer: A. Change the duplex on the switch interface to half
Explanation: Based on the information provided, the mismatch in duplex settings between the computer (full duplex) and the switch (presumably set to auto-negotiation) is likely causing the communication issue. To correct Ann's problem, the technician should change the duplex setting on the switch interface to half to match the computer's configuration.

QUESTION NO: 593
Answer: B. 127.0.0.1
Explanation: During traffic diagnostic tests on a potentially faulty network card installed in a server, the loopback address 127.0.0.1 (localhost) is commonly used for testing the network interface card (NIC) itself.

QUESTION NO: 594
Answer: D. Routing protocol
Explanation: To enable communication between the 192.168.1.100 and 192.168.2.101 networks, a routing protocol needs to be configured. Routing protocols are used to dynamically learn and advertise routes between different networks.

QUESTION NO: 595
Answer: A. BGP
Explanation: Border Gateway Protocol (BGP) should be implemented to create a route between a local area network (LAN) and an Internet Service Provider (ISP). BGP is the protocol used to exchange routing information between different autonomous systems (AS), such as an ISP's network and a customer's network.

QUESTION NO: 596
Answer: B. Layer 3 switch
Explanation: A Layer 3 switch can have multiple VLAN interfaces. Layer 3 switches operate at the network layer (Layer 3) of the OSI model and can perform routing functions between different VLANs.

QUESTION NO: 597
Answers: 
A. They used the wrong type of fiber transceiver.
B. Incorrect TX/RX polarity exists on the link
Explanation: The two most likely reasons for the link not connecting after using a light meter to verify the correct fibers are:
- They used the wrong type of fiber transceiver.
- Incorrect TX/RX polarity exists on the link. Polarity issues can occur when the transmit (TX) and receive (RX) fibers are not properly aligned.

QUESTION NO: 598
Answer: A. QoS
Explanation: Quality of Service (QoS) is used to limit the amount of bandwidth used on a link for different applications to improve overall performance. QoS allows network administrators to prioritize traffic based on factors such as application type, source/destination, and traffic characteristics.

QUESTION NO: 599
Answer: C. Tone generator
Explanation: The best tool for the network technician to use in determining which RJ45 jack in a patch panel corresponds to the RJ45 drop in the Chief Executive Officer's office is a tone generator. A tone generator is used to trace and identify cables in a network infrastructure.

QUESTION NO: 600
Answer: B. WPA2
Explanation: WPA2 (Wi-Fi Protected Access 2) would best support the requirements of enabling encryption and creating a password for AP security through the web browser. WPA2 is a security protocol that provides strong encryption and authentication for Wi-Fi networks.
''')
