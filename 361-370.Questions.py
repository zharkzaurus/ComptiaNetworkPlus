print('''
QUESTION NO: 361
A network administrator has been directed to present the network alerts from the past week
to the company's executive staff. Which of the following will provide the BEST collection and
presentation of this data?
A. A port scan printout
B. A consolidated report of various network devices
C. A report from the SIEM tool
D. A report from a vulnerability scan done yesterday

QUESTION NO: 362
The following instructions were published about the proper network configuration for a
videoconferencing device:
"Configure a valid static RFC1918 address for your network. Check the option to use a
connection over NAT." Which of the following is a valid IP address configuration for the
device?
A. FE80::1
B. 100.64.0.1
C. 169.254.1.2
D. 172.19.0.2
E. 224.0.0.12

QUESTION NO: 363
Which of the following technologies provides a failover mechanism for the default gateway?
A. FHRP
B. LACP
C. OSPF
D. STP

QUESTION NO: 364
A user would like to connect two laptops together and transfer files via the Ethernet ports.
Which of the following should MOST likely be provided to the user to accomplish this?
A. Crossover
B. Rollover
C. Loopback
D. Straight cable

QUESTION NO: 365
A coffee shop owner hired a network consultant to provide recommendations for installing a
new wireless network. The coffee shop customers expect high speeds even when the
network is congested. Which of the following standards should the consultant recommend?
A. 802.11ac
B. 802.11ax
C. 802.11g
D. 802.11n

QUESTION NO: 366
An administrator would like to have two servers at different geographical locations provide
fault tolerance and high performance while appearing as one URL to users. Which of the
following should the administrator implement?
A. Load balancing
B. Multipathing
C. NIC teaming
D. Warm site

QUESTION NO: 367
A network administrator is setting up a web-based application for a company. The application
needs to be continually accessible to all end users. Which of the following would best ensure
this need is fulfilled?
A. NIC teaming
B. Cold site
C. Snapshots
D. High availability

QUESTION NO: 368
An organization has a factory automation solution that requires accurate timing between
devices.
Which of the following should the network administrator implement?
A. PTP
B. NTP
C. NTS
D. DoT

QUESTION NO: 369
Which of the following systems would MOST likely be found in a screened subnet?
A. RADIUS
B. FTP
C. SQL
D. LDAP

QUESTION NO: 370
A network administrator creates a new network, 10.10.0.0/24, on a DHCP server. The
administrator wants to ensure that 10.10.0.10-10.10.0.15 are not allocated to other devices.
Which of the following features should the administrator configure?
A. Exclusion
B. Reservation
C. Scope
D. Relay
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 361
Answer: C. A report from the SIEM tool
Explanation: A Security Information and Event Management (SIEM) tool collects, analyzes, and presents network alerts and security events effectively, making it the best choice for presenting network alerts to executive staff.

QUESTION NO: 362
Answer: D. 172.19.0.2
Explanation: 172.19.0.2 is a valid IPv4 address within the RFC1918 address space, suitable for a private network configuration. Enabling the option to use a connection over NAT is also in line with typical network setups.

QUESTION NO: 363
Answer: A. FHRP
Explanation: First Hop Redundancy Protocol (FHRP) provides a failover mechanism for the default gateway, ensuring network reliability by allowing redundancy at the gateway level.

QUESTION NO: 364
Answer: A. Crossover
Explanation: Connecting two laptops directly via Ethernet ports typically requires a crossover cable, which allows for direct communication between the devices without the need for an intermediary device such as a switch.

QUESTION NO: 365
Answer: B. 802.11ax
Explanation: 802.11ax, also known as Wi-Fi 6, provides high-speed wireless connectivity even in congested environments, making it suitable for meeting the high-speed expectations of coffee shop customers.

QUESTION NO: 366
Answer: A. Load balancing
Explanation: Load balancing distributes incoming network traffic across multiple servers to enhance fault tolerance, ensure high performance, and provide a seamless user experience, making it suitable for the described scenario.

QUESTION NO: 367
Answer: D. High availability
Explanation: Implementing high availability ensures that the web-based application remains continually accessible to all end users by minimizing downtime and providing redundancy in case of failures.

QUESTION NO: 368
Answer: A. PTP
Explanation: Precision Time Protocol (PTP) is used for accurate timing synchronization between devices, making it suitable for applications such as factory automation where precise timing is essential.

QUESTION NO: 369
Answer: A. RADIUS
Explanation: RADIUS (Remote Authentication Dial-In User Service) is a system commonly found in a screened subnet, providing centralized authentication and authorization for network access.

QUESTION NO: 370
Answer: A. Exclusion
Explanation: The administrator should configure an exclusion range to prevent the DHCP server from assigning IP addresses within the range 10.10.0.10-10.10.0.15 to other devices, ensuring these addresses are reserved for specific use.
''')
