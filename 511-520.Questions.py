print('''
QUESTION NO: 511
A network technician has identified a breach and is attempting to determine how the attacker
connected to a device on the network. The technician uses tcpdump to perform a port scan
and receives the following result:
 10.10.10.19:9444    10.10.10.44:59824    SYN-ACK
 10.10.10.19:24123   10.10.10.51:22       SYN
 10.10.10.51:22      10.10.10.19:24123    SYN-ACK
 10.10.10.19:52091   10.10.10.51:23       SYN
 10.10.10.51:23      10.10.10.19:52091    RST
 10.10.10.19:42786   10.10.10.51:3389     SYN
 10.10.10.19:42787   10.10.10.51:3389     SYN
 10.10.10.44:59824   10.10.10.19:9444     SYN-ACK
Which of the following describes how the attacker connected to the device?
A. The attacker used Telnet.
B. The attacker used VNC.
C. The attacker used SSH.
D. The attacker used RDP.

QUESTION NO: 512
A network manager wants to view network traffic for devices connected to a switch. A
network engineer connects an appliance to a free port on the switch and needs to configure
the switch port connected to the appliance. Which of the following is the best option for the
engineer to enable?
A. Trunking
B. Port mirroring
C. Full duplex
D. SNMP

QUESTION NO: 513
Which of the following tools would a technician use to determine if a CAT6 cable is properly
terminated?
A. Cable tester
B. Punch down tool
C. Crimper
D. Multimeter

QUESTION NO: 514
A user reports a weak signal when walking 20ft (61 m) away from the WAP in one direction,
but a strong signal when walking 20ft in the opposite direction. The technician has reviewed
the configuration and confirmed the channel type is correct. There is no jitter or latency on
the connection. Which of the following would be the MOST likely cause of the issue?
A. Antenna type
B. Power levels
C. Frequency
D. Encryption type

QUESTION NO: 515
Which of the following routing protocols uses an autonomous system number?
A. IS-IS
B. EIGRP
C. OSPF
D. BGP

QUESTION NO: 516
The management team has instituted a 48-hour RTO as part of the disaster recovery plan.
Which of the following procedures would meet the policy's requirements?
A. Recover all systems to a loss of 48 hours of data.
B. Limit network downtime to a maximum of 48 hours per year.
C. Recover all systems within 48 hours.
D. Require 48 hours of system backup maintenance.

QUESTION NO: 517
An organization set up its offices so that a desktop is connected to the network through a
VoIP phone. The VoIP vendor requested that voice traffic be segmented separately from
non-voice traffic. Which of the following would allow the organization to configure multiple
devices with network isolation on a single switch port?
A. Subinterfaces
B. Link aggregation
C. Load balancing
D. Tunneling

QUESTION NO: 518
Users are reporting that all of a sudden some of the files stored on the remote file server
share are becoming corrupted and cannot be opened. A technician is dispatched to the
server room to troubleshoot. The technician verifies that no changes to the network
infrastructure occurred recently. Which of the following tools is MOST likely to reveal why
files are becoming corrupted?
A. Environmental monitor
B. OTDR
C. Cable tester
D. Punch down tool

QUESTION NO: 519
A network administrator is investigating reports about network performance and finds high
utilization on a switch uplink. The administrator is unsure whether this is an anomaly or
normal behavior that will require an upgrade to resolve. Which of the following should the
administrator reference to gain historical perspective?
A. Device configuration review
B. ARP table export
C. Service-level agreement
D. Network performance baseline

QUESTION NO: 520
Several users with older devices are reporting intermittent connectivity while in an outdoor
patio area. After some research, the network administrator determines that an outdoor WAP
might help with the issue. However, the company does not want the signal to bleed into the
building and cause interference. Which of the following should the network administrator
perform to BEST resolve the issue?
A. Disable the SSID broadcast on the WAP in the patio area.
B. Install a WAP and enable 5GHz only within the patio area.
C. Install a directional WAP in the direction of the patio.
D. Install a repeater on the back wall of the patio area.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 511
Answer: D
Explanation: The attacker used RDP (Remote Desktop Protocol).
Looking at the tcpdump results, the connections indicate attempts to establish various connections to different ports on different devices. The connection between IP addresses 10.10.10.19 and 10.10.10.51 on port 23 (TCP) shows a SYN packet from 10.10.10.19 to port 23 on 10.10.10.51, followed by a RST (reset) packet from 10.10.10.51 to 10.10.10.19. This sequence of packets is indicative of an attempt to establish an RDP (Remote Desktop Protocol) connection, as port 23 is typically associated with Telnet, not RDP.

QUESTION NO: 512
Answer: B
Explanation: Port mirroring.
Port mirroring is the best option for the engineer to enable. Port mirroring, also known as SPAN (Switched Port Analyzer) or RSPAN (Remote Switched Port Analyzer), allows network traffic from multiple ports to be monitored simultaneously by forwarding a copy of that traffic to a designated monitoring port. This enables the network manager to view network traffic for devices connected to the switch without disrupting normal network operation.

QUESTION NO: 513
Answer: A
Explanation: Cable tester.
A cable tester is used to determine if a CAT6 cable is properly terminated. It verifies the connectivity and integrity of the cable by checking for continuity, shorts, and other common wiring issues. By connecting the cable to the tester, technicians can quickly identify any faults in the cable's termination.

QUESTION NO: 514
Answer: A
Explanation: Antenna type.
The most likely cause of the issue is the antenna type. Different antenna types have different radiation patterns, which can result in uneven coverage areas. In this scenario, the weak signal when walking in one direction but a strong signal in the opposite direction suggests that the antenna's radiation pattern may be directional, favoring one direction over the other.

QUESTION NO: 515
Answer: D
Explanation: BGP (Border Gateway Protocol).
BGP (Border Gateway Protocol) is the routing protocol that uses an autonomous system number (ASN). BGP is commonly used in large-scale networks, such as the Internet, for routing between autonomous systems (ASes). Autonomous system numbers are used to uniquely identify individual ASes on the Internet.

QUESTION NO: 516
Answer: C
Explanation: Recover all systems within 48 hours.
To meet the policy's requirement of a 48-hour RTO (Recovery Time Objective), the organization should ensure that all systems can be recovered within 48 hours of a disaster. This means having plans and procedures in place to restore critical systems and services within the specified timeframe to minimize downtime and maintain business continuity.

QUESTION NO: 517
Answer: A
Explanation: Subinterfaces.
Subinterfaces allow the organization to configure multiple devices with network isolation on a single switch port. By creating separate logical interfaces (subinterfaces) on the switch port and assigning each interface to a different VLAN (Virtual Local Area Network), the organization can achieve network segmentation and isolation for voice and non-voice traffic while using a single physical connection.

QUESTION NO: 518
Answer: A
Explanation: Environmental monitor.
An environmental monitor is the most likely tool to reveal why files are becoming corrupted. Environmental monitors are devices that track environmental conditions such as temperature, humidity, and power fluctuations in server rooms and data centers. Corrupted files can sometimes be caused by environmental factors such as overheating or power surges, which an environmental monitor can detect and alert administrators to.

QUESTION NO: 519
Answer: D
Explanation: Network performance baseline.
To gain historical perspective on network utilization and performance, the administrator should reference the network performance baseline. A network performance baseline is a collection of historical data that represents typical network behavior under normal operating conditions. By comparing current network utilization to the baseline, administrators can determine whether the high utilization on the switch uplink is abnormal or within expected levels.

QUESTION NO: 520
Answer: C
Explanation: Install a directional WAP in the direction of the patio.
To best resolve the issue, the network administrator should install a directional WAP (Wireless Access Point) in the direction of the patio. A directional antenna focuses the Wi-Fi signal in a specific direction, reducing signal bleed and interference in other areas. This solution ensures that the outdoor patio area receives strong and reliable Wi-Fi coverage without causing interference inside the building.
''')
