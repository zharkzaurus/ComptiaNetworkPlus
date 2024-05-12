print('''
QUESTION NO: 391
Which of the following technologies would MOST likely be used to prevent the loss of
connection between a virtual server and network storage devices?
A. Multipathing
B. VRRP
C. Port aggregation
D. NIC teaming

QUESTION NO: 392
Which of the following can be used to store various types of devices and provide contactless
delivery to users?
A. Asset tags
B. Biometrics
C. Access control vestibules
D. Smart lockers

QUESTION NO: 393
A corporation is looking for a method to secure all traffic between a branch office and its data
center in order to provide a zero-touch experience for all staff members who work there.
Which of the following would BEST meet this requirement?
A. Site-to-site VPN
B. VNC
C. Remote desktop gateway
D. Virtual LANs

QUESTION NO: 394
At which layer of the OSI model do MAC addresses operate?
A. Data Link
B. Network
C. Application
D. Physical

QUESTION NO: 395
A technician is configuring a wireless network and needs to ensure users agree to an AUP
before connecting. Which of the following should be implemented to achieve this goal?
A. Captive portal
B. Geofencing
C. Wireless client isolation
D. Role-based access

QUESTION NO: 396
A network engineer is investigating issues on a Layer 2 switch. The department typically
shares a switchport during meetings for presentations, but after the first user shares, no other
users can connect. Which of the following is MOST likely related to this issue?
A. Spanning Tree Protocol is enabled on the switch.
B. VLAN trunking is enabled on the switch.
C. Port security is configured on the switch.
D. Dynamic ARP inspection is configured on the switch.

QUESTION NO: 397
A network administrator wants to balance the amount of data between two networking cards.
Which of the following can be used for two or more networking cards?
A. NIC bonding
B. Proxy server
C. Firewall ACLs
D. VLANs

QUESTION NO: 398
Which of the following spreads out each of the individual wires of a UTP cable onto their own
metal connector?
A. BNC connection
B. 110 block
C. Plenum
D. LC connector

QUESTION NO: 399
A user reports being unable to access network resources after making some changes in the
office. Which of the following should a network technician do FIRST?
A. Check the system's IP address
B. Do a ping test against the servers
C. Reseat the cables into the back of the PC
D. Ask what changes were made

QUESTION NO: 400
Which of the following would be used when connecting devices that have different physical
characteristics?
A. A proxy server
B. An industrial control system
C. A load balancer
D. A media converter
''')
answer = input(print("do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 391
Answer: A
Explanation: Multipathing is the technology most likely used to prevent the loss of connection between a virtual server and network storage devices. Multipathing involves using multiple physical paths between servers and storage arrays to increase redundancy and fault tolerance, ensuring continuous access to storage even if one path fails.

NO: 392
Answer: D
Explanation: Smart lockers can be used to store various types of devices and provide contactless delivery to users. Smart lockers are equipped with electronic locks and tracking systems, allowing users to securely store and retrieve items such as laptops, tablets, or mobile devices.

NO: 393
Answer: A
Explanation: A site-to-site VPN (Virtual Private Network) would best meet the corporation's requirement to secure all traffic between a branch office and its data center, providing a zero-touch experience for staff members. A site-to-site VPN creates a secure encrypted tunnel over the internet, allowing remote sites to connect securely to the central data center.

NO: 394
Answer: A
Explanation: MAC addresses operate at the Data Link layer (Layer 2) of the OSI model. They are used to uniquely identify devices within the same network segment and are essential for the operation of Ethernet networks.

NO: 395
Answer: A
Explanation: To ensure users agree to an Acceptable Use Policy (AUP) before connecting to a wireless network, a captive portal should be implemented. A captive portal is a web page that intercepts and redirects users' web traffic to a login page or an AUP page before allowing access to the network.

NO: 396
Answer: C
Explanation: Port security is most likely related to the issue described. Port security restricts the number of MAC addresses allowed to connect to a switch port, and if the maximum limit is reached, additional devices will be denied connection.

NO: 397
Answer: A
Explanation: NIC bonding, also known as NIC teaming or link aggregation, can be used to balance the amount of data between two or more networking cards. It combines multiple network interfaces into a single logical interface, providing redundancy and increased throughput.

NO: 398
Answer: B
Explanation: A 110 block is used to spread out each of the individual wires of a UTP cable onto their own metal connector. It is commonly used for terminating and connecting telephone and data cables.

NO: 399
Answer: D
Explanation: When a user reports being unable to access network resources after making changes, the network technician should FIRST ask what changes were made. Understanding the changes made can provide valuable insight into the cause of the issue and guide the troubleshooting process.

NO: 400
Answer: D
Explanation: A media converter would be used when connecting devices that have different physical characteristics, such as connecting fiber optic cabling to copper-based Ethernet devices. Media converters facilitate the conversion between different types of cabling and signaling, allowing interoperability between diverse network components.
''')
