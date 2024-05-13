print('''
QUESTION NO: 531
A user is having difficulty with video conferencing and is looking for assistance. Which of the
following would BEST improve performance?
A. Packet shaping
B. Quality of service
C. Port mirroring
D. Load balancing

QUESTION NO: 532
A network technician is working at a new office location and needs to connect one laptop to
another to transfer files. The laptops are newer models and do not have Ethernet ports.
Access points are not available either. Which of the following types of wireless network
SSIDs does the network technician need to configure to be able to connect the laptops
together?
A. Independent Basic Service Set
B. Extended Service Set
C. Distribution System Service
D. Basic Service Set

QUESTION NO: 533
A technician removes an old PC from the network and replaces it with a new PC that is
unable to connect to the LAN.
Which of the Mowing is MOST likely the cause of the issue?
A. Port security
B. Port tagging
C. Port aggregation
D. Port mirroring

QUESTION NO: 534
A network administrator wants to test the throughput of a new metro Ethernet circuit to verify
that its performance matches the requirements specified in the SLA.
Which of the following would BEST help measure the throughput?
A. iPerf
B. Ping
C. NetFlow
D. Netstat

QUESTION NO: 535
Which of the following should be configured on a separate network segment without access
to the primary company network when security is a concern?
A. Email server
B. IoT devices
C. Wireless LAN controller
D. Voice gateway

QUESTION NO: 536
A network technician is observing the behavior of an unmanaged switch when a new device
is added to the network and transmits data.
Which of the following BEST describes how the switch processes this information?
A. The data is flooded out of every port. including the one on which it came in.
B. The data is flooded out of every port but only in the VLAN where it is located.
C. The data is flooded out of every port, except the one on which it came in
D. The data is flooded out of every port, excluding the VLAN where it is located

QUESTION NO: 537
Which of the following DHCP settings would be used to ensure a device gets the same IP
address each time it is connected to the network?
A. Scope options
B. Reservation
C. Exclusion
D. Relay
E. Pool

QUESTION NO: 538
A systems administrator is looking for operating system information, running services, and
network ports that are available on a server. Which of the following software tools should the
administrator use to accomplish this task?
A. nslookup
B. nmap
C. traceroute
D. netstat

QUESTION NO: 539
A technician is configuring a network switch to be used in a publicly accessible location.
Which of the following should the technician configure on the switch to prevent unintended
connections?
A. DHCP snooping
B. Geofencing
C. Port security
D. Secure SNMP

QUESTION NO: 540
A network technician is investigating a trouble ticket for a user who does not have network
connectivity. All patch cables between the wall jacks and computers in the building were
upgraded over the weekend from Cat 5 to Cat 6. The newly installed cable is crimped with a
TIA/EIA 568A on one end and a TIA/EIA 568B on the other end. Which of the following
should the technician do to MOST likely fix the issue?
A. Ensure the switchport has PoE enabled.
B. Crimp the cable as a straight-through cable.
C. Ensure the switchport has STP enabled,
D. Crimp the cable as a rollover cable.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 531
Answer: B
Explanation: Quality of service (QoS).
To improve performance for video conferencing, Quality of Service (QoS) would be the best option. QoS is a network management technique used to prioritize certain types of traffic over others. By implementing QoS policies, network administrators can ensure that video conferencing traffic receives sufficient bandwidth, low latency, and minimal packet loss, thereby improving the overall quality of the video conferencing experience.

QUESTION NO: 532
Answer: A
Explanation: Independent Basic Service Set (IBSS).
The network technician needs to configure the laptops to connect to each other directly without the use of access points. This can be achieved by configuring them to form an Independent Basic Service Set (IBSS), also known as an ad-hoc network. In an IBSS, devices communicate with each other directly without the need for an access point, allowing the laptops to transfer files wirelessly between them.

QUESTION NO: 533
Answer: A
Explanation: Port security.
Port security is the most likely cause of the issue where a new PC is unable to connect to the LAN after replacing an old PC. Port security is a feature that allows network administrators to restrict access to Ethernet ports based on MAC address. If port security is enabled and configured to allow only specific MAC addresses, the new PC may not be able to connect until its MAC address is added to the allowed list.

QUESTION NO: 534
Answer: A
Explanation: iPerf.
To measure the throughput of a new metro Ethernet circuit, the network administrator would best use iPerf. iPerf is a widely used tool for measuring TCP and UDP throughput between two endpoints. By running iPerf between two devices connected to the metro Ethernet circuit, the administrator can generate network traffic and measure the actual throughput achieved, helping to verify whether it meets the requirements specified in the SLA.

QUESTION NO: 535
Answer: B
Explanation: IoT devices.
IoT (Internet of Things) devices should be configured on a separate network segment without access to the primary company network when security is a concern. IoT devices often have limited security features and may be vulnerable to exploitation. Placing them on a separate network segment helps isolate them from critical company resources and reduces the risk of unauthorized access or attacks targeting the primary network.

QUESTION NO: 536
Answer: A
Explanation: The data is flooded out of every port, including the one on which it came in.
When a new device is added to the network and transmits data on an unmanaged switch, the switch processes the information by flooding the data out of every port, including the one on which it came in. Since unmanaged switches do not maintain a MAC address table or perform any packet filtering, they forward incoming data to all ports except the one it was received on, leading to broadcast storms in large networks.

QUESTION NO: 537
Answer: B
Explanation: Reservation.
To ensure a device gets the same IP address each time it is connected to the network, DHCP reservation should be used. DHCP reservation allows the DHCP server to assign a specific IP address to a device based on its MAC address. This ensures consistency in IP address assignment for devices that require static IP configurations without manually configuring each device.

QUESTION NO: 538
Answer: D
Explanation: netstat.
The systems administrator should use netstat to gather operating system information, running services, and network ports that are available on a server. netstat is a command-line tool available on most operating systems that displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

QUESTION NO: 539
Answer: C
Explanation: Port security.
To prevent unintended connections on a network switch in a publicly accessible location, the technician should configure port security. Port security is a feature that allows administrators to restrict access to Ethernet ports based on MAC address. By enabling port security and configuring allowed MAC addresses on switch ports, the technician can prevent unauthorized devices from connecting to the network through physical Ethernet ports.

QUESTION NO: 540
Answer: B
Explanation: Crimp the cable as a straight-through cable.
The technician should crimp the cable as a straight-through cable. The use of different wiring standards on each end of the cable (TIA/EIA 568A on one end and TIA/EIA 568B on the other end) results in a crossover cable configuration. However, in this scenario, the intention is to connect two devices directly, which requires a straight-through cable configuration on both ends for proper communication. Therefore, crimping the cable as a straight-through cable would likely fix the issue.
''')
