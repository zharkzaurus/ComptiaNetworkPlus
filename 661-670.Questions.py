print('''
QUESTION NO: 661
Which of the following networking devices operates at Layer1?
A. Router
B. Firewall
C. Hub
D. Bridge

QUESTION NO: 662
A systems administrator needs to improve WiFi performance in a densely populated office
tower and use the latest standard.
There is a mix of devices that use 2.4 GHz and 5 GHz.
Which of the following should the systems administrator select to meet this requirement?
A. 802.11ac
B. 802.11ax
C. 802.11g
D. 802.11n

QUESTION NO: 663
A switch is connected to another switch. Incompatible hardware causes a surge in traffic on
both switches. Which of the following configurations will cause traffic to pause, allowing the
switches to drain buffers?
A. Speed
B. Flow control
C. 802.1Q
D. Duplex

QUESTION NO: 664
A technician notices that equipment is being moved around and misplaced in the server
room, even though the room has locked doors and cabinets. Which of the following would be
the BEST solution to identify who is responsible?
A. Install motion detection.
B. Install cameras.
C. Install tamper detection.
D. Hire a security guard.

QUESTION NO: 665
Which of the following is a characteristic of the application layer?
A. It relies upon other layers for packet delivery.
B. It checks independently for packet loss.
C. It encrypts data in transit.
D. It performs address translation.

QUESTION NO: 666
There are two managed legacy switches running that cannot be replaced or upgraded. These
switches do not support cryptographic functions, but they are password protected.
Which of the following should a network administrator configure to BEST prevent
unauthorized access?
A. Enable a management access list
B. Disable access to unnecessary services.
C. Configure a stronger password for access
D. Disable access to remote management
E. Use an out-of-band access method.

QUESTION NO: 667
Which of the following BEST describes a North-South traffic flow?
A. A public Internet user accessing a published web server
B. A database server communicating with another clustered database server
C. A Layer 3 switch advertising routes to a router
D. A management application connecting to managed devices

QUESTION NO: 668
A network engineer is monitoring a fiber uplink to a remote office and notes the uplink has
been operating at 100% capacity for a long duration. Which of the following performance
metrics is MOST likely to be impacted with sustained link saturation?
A. Latency
B. Jitter
C. Speed
D. Bandwidth

QUESTION NO: 669
A network administrator is configuring a firewall to allow for a new cloud-based email server.
The company standard is to use SMTP to route email traffic. Which of the following ports, by
default, should be reserved for this purpose?
A. 23
B. 25
C. 53
D. 110

QUESTION NO: 670
After installing a new 6E wireless router in a small office, a technician notices that some
wireless devices are not able to achieve the rated speeds. Which of the following should the
technician check to troubleshoot the issue? (Choose two.)
A. Client device compatibility
B. Back-end cabling
C. Weather phenomena
D. Voltage source requirements
E. Interference levels
F. Processing power
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 661
Answer: C. Hub
Explanation: A hub operates at Layer 1 of the OSI model, which is the physical layer. Hubs simply forward data to all ports, regardless of the destination, making them unaware of the higher-layer protocols or addresses.

QUESTION NO: 662
Answer: B. 802.11ax
Explanation: To improve WiFi performance in a densely populated office tower with a mix of devices using 2.4 GHz and 5 GHz, the systems administrator should select the latest standard, which is 802.11ax. This standard, also known as Wi-Fi 6, offers improved efficiency, higher throughput, and better performance in crowded environments compared to previous standards.

QUESTION NO: 663
Answer: B. Flow control
Explanation: Flow control is a mechanism used to manage the flow of data between devices to prevent congestion and buffer overflow. When incompatible hardware causes a surge in traffic on both switches, enabling flow control can cause traffic to pause, allowing the switches to drain buffers and prevent data loss.

QUESTION NO: 664
Answer: B. Install cameras.
Explanation: Installing cameras would be the best solution to identify who is responsible for moving and misplacing equipment in the server room. Cameras can capture video footage of individuals entering and leaving the room, providing visual evidence to determine who is responsible for the actions.

QUESTION NO: 665
Answer: A. It relies upon other layers for packet delivery.
Explanation: The application layer of the OSI model relies upon lower layers, such as the transport layer and the network layer, for packet delivery. It provides services to applications, including data encryption, session management, and application-specific protocols, but it does not independently handle packet delivery.

QUESTION NO: 666
Answer: A. Enable a management access list
Explanation: Enabling a management access list would be the best option to prevent unauthorized access to the managed legacy switches. By creating a list of authorized IP addresses or management stations, the network administrator can restrict access to the switches to only authorized users or devices.

QUESTION NO: 667
Answer: A. A public Internet user accessing a published web server
Explanation: North-South traffic flow refers to traffic moving between a client and a server located in different network zones. A public Internet user accessing a published web server represents North-South traffic flow because the traffic traverses different network zones (i.e., the user's network and the server's network).

QUESTION NO: 668
Answer: A. Latency
Explanation: When a fiber uplink operates at 100% capacity for a long duration, the most likely performance metric to be impacted is latency. Latency refers to the delay experienced in the transmission of data over a network, and high network utilization can cause increased latency as packets queue up for transmission.

QUESTION NO: 669
Answer: B. 25
Explanation: By default, SMTP (Simple Mail Transfer Protocol) uses port 25 for email traffic. Therefore, to allow for the new cloud-based email server, the network administrator should reserve port 25 on the firewall to facilitate SMTP communication.

QUESTION NO: 670
Answer: A. Client device compatibility
Explanation: When troubleshooting why some wireless devices are not able to achieve the rated speeds after installing a new 6E wireless router, the technician should check client device compatibility. Not all devices may support the new Wi-Fi 6E standard, so ensuring compatibility with the router is important. Additionally, interference levels in the environment should be checked, as they can affect wireless performance.
''')
