print('''
QUESTION: 451
Which of the following is MOST likely to generate significant East-West traffic in a
datacenter?
A. A backup of a large video presentation to cloud storage for archival purposes
B. A duplication of a hosted virtual server to another physical server for redundancy
C. A download of navigation data to a portable device for offline access
D. A query from an IoT device to a cloud-hosted server for a firmware update

QUESTION NO: 452
A network technician is investigating an issue with a desktop that is not connecting to the
network. The desktop was connecting successfully the previous day, and no changes were
made to the environment. The technician locates the switchport where the device is
connected and observes the LED status light on the switchport is not lit even though the
desktop is turned on Other devices that arc plugged into the switch are connecting to the
network successfully.
Which of the following is MOST likely the cause of the desktop not connecting?
A. Transceiver mismatch
B. VLAN mismatch
C. Port security
D. Damaged cable
E. Duplex mismatch

QUESTION NO: 453
A firewall administrator observes log entries of traffic being allowed to a web server on port
80 and port 443. The policy for this server is to only allow traffic on port 443. The firewall
administrator needs to investigate how this change occurred to prevent a reoccurrence.
Which of the following should the firewall administrator do next?
A. Consult the firewall audit logs.
B. Change the policy to allow port 80.
C. Remove the server object from the firewall policy.
D. Check the network baseline.

QUESTION NO: 454
A network administrator is configuring logging on an edge switch. The requirements are to
log each time a switch port goes up or down. Which of the following logging levels will
provide this information?
A. Warnings
B. Notifications
C. Alert
D. Errors

QUESTION NO: 455
A network administrator is installing a wireless network at a client's office.
Which of the following IEEE 802.11 standards would be BEST to use for multiple
simultaneous client access?
A. CDMA
B. CSMA/CD
C. CSMA/CA
D. GSM

QUESTION NO: 456
Which of the following DNS records maps an alias to a true name?
A. AAAA
B. NS
C. TXT
D. CNAME

QUESTION NO: 457
A network technician is troubleshooting a network issue for employees who have reported
issues with speed when accessing a server in another subnet. The server is in another
building that is
410ft (125m) away from the employees' building. The 10GBASE-T connection between the
two buildings uses Cat 5e. Which of the following BEST explains the speed issue?
A. The connection type is not rated for that distance.
B. A broadcast storm is occurring on the subnet.
C. The cable run has interference on it.
D. The connection should be made using a Cat 6 cable.

QUESTION NO: 458
A network technician at a university is assisting with the planning of a simultaneous software
deployment to multiple computers in one classroom in a building.
Which of the following would be BEST to use?
A. Multicast
B. Anycast
C. Unicast
D. Broadcast

QUESTION NO: 459
A network technician is investigating an IP phone that does not register in the VoIP system
Although it received an IP address, it did not receive the necessary DHCP options The
information that is needed for the registration is distributes by the OHCP scope All other IP
phones are working properly. Which of the following does the technician need to verify?
A. VLAN mismatch
B. Transceiver mismatch
C. Latency
D. DHCP exhaustion

QUESTION NO: 460
An administrator is working with the local ISP to troubleshoot an issue. Which of the following
should the ISP use to define the furthest point on the network that the administrator is
responsible for troubleshooting?
A. Firewall
B. A CSU/DSU
C. Demarcation point
D. Router
E. Patch panel
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 451
Answer: B
Explanation: Option B, "A duplication of a hosted virtual server to another physical server for redundancy," is most likely to generate significant East-West traffic in a datacenter. East-West traffic refers to the data flow between servers or devices within the same datacenter or network segment. Duplicating a hosted virtual server to another physical server for redundancy would involve transferring data between servers within the datacenter, resulting in significant East-West traffic.

QUESTION NO: 452
Answer: D
Explanation: The most likely cause of the desktop not connecting is a damaged cable. Since other devices connected to the switch are successfully connecting to the network, issues such as transceiver mismatch, VLAN mismatch, port security, or duplex mismatch are less probable. A damaged cable would prevent the desktop from establishing a connection even if the device is turned on.

QUESTION NO: 453
Answer: A
Explanation: The firewall administrator should consult the firewall audit logs to investigate how the change occurred and to prevent a reoccurrence. Firewall audit logs provide detailed information about the changes made to firewall policies, including who made the changes, when they were made, and what changes were implemented. Reviewing the audit logs will help identify any unauthorized or unintended modifications to the firewall policy.

QUESTION NO: 454
Answer: B
Explanation: The logging level that will provide information about each time a switch port goes up or down is "Notifications." Logging at the "Notifications" level captures informational messages, including events such as port status changes. Therefore, configuring the edge switch to log at the "Notifications" level will meet the requirement to log each time a switch port goes up or down.

QUESTION NO: 455
Answer: C
Explanation: The IEEE 802.11 standard that would be best to use for multiple simultaneous client access is CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance). CSMA/CA is the collision avoidance mechanism used in Wi-Fi networks to manage multiple clients accessing the wireless medium. It ensures that only one client transmits at a time, thereby reducing collisions and maximizing efficiency in scenarios with multiple clients.

QUESTION NO: 456
Answer: D
Explanation: The DNS record that maps an alias to a true name is a CNAME (Canonical Name) record. A CNAME record is used to alias one domain name to another. It allows multiple domain names to resolve to the same IP address. For example, you can create a CNAME record to map "www.example.com" to "example.com."

QUESTION NO: 457
Answer: C
Explanation: The speed issue is most likely due to interference on the cable run between the two buildings. Despite being within the maximum distance limit for Cat 5e cable, interference can degrade the signal quality, leading to reduced data transmission speeds. Upgrading to Cat 6 cable, which provides better shielding against interference, would help mitigate this issue and ensure optimal performance for the 10GBASE-T connection.

QUESTION NO: 458
Answer: A
Explanation: The best method to use for a simultaneous software deployment to multiple computers in one classroom in a building is multicast. Multicast allows the transmission of data from one source to multiple recipients simultaneously. In the context of software deployment, multicast enables efficient distribution of software updates or installations to multiple computers within the same network segment.

QUESTION NO: 459
Answer: A
Explanation: The technician needs to verify a VLAN mismatch. Since the IP phone received an IP address but did not receive the necessary DHCP options for registration, it suggests that the phone may be in the wrong VLAN. DHCP options are used to provide additional configuration parameters to devices, such as the VLAN information for VoIP phones. A VLAN mismatch could prevent the phone from communicating with the VoIP system.

QUESTION NO: 460
Answer: C
Explanation: The ISP should use the demarcation point to define the furthest point on the network that the administrator is responsible for troubleshooting. The demarcation point, also known as the "demarc," is the physical point where the responsibility shifts from the service provider's network to the customer's network. It typically marks the boundary between the ISP's infrastructure and the customer's premises, making it the logical starting point for troubleshooting network issues.
''')
