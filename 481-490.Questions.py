print('''
QUESTION NO: 481
A network technician is troubleshooting an issue that involves connecting to a server via
SSH.
The server has one network interface that does not support subinterfaces. The technician
runs a command on the server and receives the following output:
 Proto  Local address   Foreign address      State
 TCP    0.0.0.0:22      0.0.0.0:0            LISTENING
 TCP    0.0.0.0:23      0.0.0.0:0            LISTENING
 TCP    0.0.0.0:443     0.0.0.0:0            LISTENING
 TCP    10.10.10.15.22  10.10.10.42.21231    ESTABLISHED
On the host, the technician runs another command and receives the following:
 Destination   Gateway       Genmask        Flags    Iface
 default       31.242.12.9   0.0.0.0        UG       eth0
 192.168.1.0   0.0.0.0       255.255.255.0  UG       eth1
Which of the following best explains the issue?
A. A firewall is blocking access to the server.
B. The server is plugged into a trunk port.
C. The host does not have a route to the server.
D. The server is not running the SSH daemon.

QUESTION NO: 482
A network administrator is preparing new switches that will be deployed to support a network
extension project. The lead network engineer has already provided documentation to ensure
the switches are set up properly. Which of the following did the engineer most likely provide?
A. Physical network diagram
B. Site survey reports
C. Baseline configurations
D. Logical network diagram

QUESTION NO: 483
A network technician is troubleshooting an area where the wireless connection to devices is
poor.
The technician theorizes that the signal-to-noise ratio in the area is causing the issue. Which
of the following should the technician do NEXT?
A. Run diagnostics on the relevant devices.
B. Move the access point to a different location.
C. Escalate the issue to the vendor's support team.
D. Remove any electronics that might be causing interference.

QUESTION NO: 484
Which of the following would be used on a network to ensure access to resources if a critical
host becomes unavailable?
A. QoS
B. CARP
C. VLAN
D. DHCP server

QUESTION NO: 485
A network technician is planning a network scope. The web server needs to be within
12.31.69.1 to 12.31.69.29. Which of the following would meet this requirement?
A. Lease time
B. Range reservation
C. DNS
D. Superscope

QUESTION NO: 486
A network administrator is securing the wireless network in a multitenant building. The
network uses a passphrase for authentication so it is easy to allow guests onto the wireless
network, but management would like to prevent users from outside the office space from
accessing the network. Which of the following security mechanisms would BEST meet this
requirement?
A. MAC filtering
B. WPA-PSK
C. 802.1X
D. Geofencing

QUESTION NO: 487
A network device is configured to send critical events to a syslog server; however, the
following alerts are not being received:
Severity 5 LINK-UPDOWN: Interface 1/1, changed state to down
Severity 5 LINK-UPDOWN: Interface 1/3, changed state to down
Which of the following describes the reason why the events are not being received?
A. The network device is not configured to log that level to the syslog server
B. The network device was down and could not send the event
C. The syslog server is not compatible with the network device
D. The syslog server did not have the correct MIB loaded to receive the message

QUESTION NO: 488
A network administrator is decommissioning a server. Which of the following will the network
administrator MOST likely consult?
A. Onboarding and off boarding policies
B. Business continuity plan
C. Password requirements
D. Change management documentation

QUESTION NO: 489
Following the implementation of a BYOD policy, some users in a high-density environment
report slowness over the wireless connection. Some wireless controller reports indicate high
latency and airttime contention. Which of the following is the most probable root cause?
A. The AP is configured with 2.4GHz frequency, which the new personal devices do not
support.
B. The AP is configured with 2.4GHz frequency without band-steering capabilities.
C. The AP is configured with 5Ghz frequency with band-steering capabilities.
D. The AP is configured with 5Ghz frequency, which the new personal devices do not suppor
t

QUESTION NO: 490
A company recently upgraded all of its printers to networked multifunction devices. Users can
print to the new devices, but they would also like the ability to scan and fax files from their
computers. Which of the following should the technician update to allow this functionality?
A. Device software
B. Printer drivers
C. Printer firmware
D. NIC drivers
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 481
Answer: C
Explanation: The correct answer is C. The host does not have a route to the server. The output provided indicates that the server's IP address (10.10.10.15) falls within the subnet 192.168.1.0/24. However, the destination 10.10.10.15 does not have a corresponding route in the routing table of the host. Therefore, the host does not have a route to reach the server, resulting in connectivity issues when attempting to connect via SSH.

QUESTION NO: 482
Answer: C
Explanation: The correct answer is C. Baseline configurations. Baseline configurations are documentation that outlines the standard configuration settings and parameters for network devices. They ensure that new devices are set up properly and consistently according to the network's requirements. Providing baseline configurations helps ensure uniformity and consistency in the network deployment process.

QUESTION NO: 483
Answer: B
Explanation: The correct answer is B. Move the access point to a different location. If the technician suspects that the signal-to-noise ratio (SNR) is causing poor wireless connection quality, the next step should be to move the access point to a different location. By relocating the access point, the technician can potentially improve the wireless coverage and reduce interference, resulting in better SNR and improved connectivity for devices in the area.

QUESTION NO: 484
Answer: B
Explanation: The correct answer is B. CARP (Common Address Redundancy Protocol). CARP is a protocol used for achieving high availability and redundancy in network environments. It allows multiple hosts on the network to share a common IP address, ensuring that access to resources remains available even if a critical host becomes unavailable.

QUESTION NO: 485
Answer: B
Explanation: The correct answer is B. Range reservation. Range reservation allows specific IP address ranges to be reserved for certain purposes or devices on the network. In this case, configuring a range reservation for IP addresses 12.31.69.1 to 12.31.69.29 ensures that these addresses are allocated for use by the web server, meeting the requirement specified by the network administrator.

QUESTION NO: 486
Answer: A
Explanation: The correct answer is A. MAC filtering. MAC filtering allows the network administrator to control which devices can connect to the wireless network based on their MAC addresses. By configuring MAC filtering, the administrator can restrict access to only authorized devices, preventing users from outside the office space from accessing the network, while still allowing guests with approved MAC addresses to connect.

QUESTION NO: 487
Answer: D
Explanation: The correct answer is D. The syslog server did not have the correct MIB loaded to receive the message. The issue described indicates that the syslog server did not receive the events due to a mismatch in the Management Information Base (MIB) configuration. The syslog server needs to have the correct MIB loaded to interpret and process the syslog messages sent by the network device.

QUESTION NO: 488
Answer: D
Explanation: The correct answer is D. Change management documentation. When decommissioning a server, the network administrator would most likely consult change management documentation. Change management documentation includes records of all changes made to the network infrastructure, including decommissioning activities, to ensure proper documentation and adherence to established processes.

QUESTION NO: 489
Answer: B
Explanation: The correct answer is B. The AP is configured with 2.4GHz frequency without band-steering capabilities. Band steering is a technique used in wireless networks to optimize client connectivity by steering dual-band-capable clients to the less congested 5GHz frequency band. Without band-steering capabilities, devices may remain connected to the 2.4GHz band, leading to high latency and contention, especially in high-density environments.

QUESTION NO: 490
Answer: A
Explanation: The correct answer is A. Device software. To enable scanning and faxing functionality from computers to the networked multifunction devices (MFDs), the technician should update the device software or install additional software applications provided by the MFD manufacturer. This software typically includes drivers and utilities that allow users to interact with the MFDs' scanning and faxing features from their computers.
''')
