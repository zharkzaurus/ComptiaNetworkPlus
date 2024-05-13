print('''
QUESTION NO: 581
Which of the following would need to be configured to ensure a device with a specific MAC
address is always assigned the same IP address from DHCP?
A. Scope options
B. Reservation
C. Dynamic assignment
D. Exclusion
E. Static assignment

QUESTION NO: 582
Which of the following must be functioning properly in order for a network administrator to
create an accurate timeline during a troubleshooting process?
A. NTP
B. IP helper
C. Syslog
D. MySQL

QUESTION NO: 583
A user wants to secure a network closet and be able to tell if anyone makes changes in the
closet. Which of the following would be the BEST detective physical security devices in this
situation? (Choose two.)
A. Anti-tampering
B. Badges
C. Door locks
D. Key fob
E. Motion detection
F. Video surveillance

QUESTION NO: 584
A network technician has determined the cause of a network disruption. Which of the
following is the NEXT step for the technician to perform?
A. Validate the findings in a top-to-bottom approach
B. Duplicate the issue, if possible
C. Establish a plan of action to resolve the issue
D. Document the findings and actions

QUESTION NO: 585
An IT technician needs to increase bandwidth to a server. The server has multiple gigabit
ports.
Which of the following can be used to accomplish this without replacing hardware?
A. STP
B. 802.1Q
C. Duplex
D. LACP

QUESTION NO: 586
A network administrator notices excessive wireless traffic occurring on an access point after
normal business hours. The access point is located on an exterior wall. Which of the
following should the administrator do to limit wireless access outside the building?
A. Set up a private VLAN.
B. Disable roaming on the WAP.
C. Change to a directional antenna.
D. Stop broadcasting of the SSID.

QUESTION NO: 587
Which of the following network types is composed of computers that can all communicate
with one another with equal permissions and allows users to directly share what is on or
attached to their computers?
A. Local area network
B. Peer-to-peer network
C. Client-server network
D. Personal area network

QUESTION NO: 588
A network administrator is configuring a static DSL connection on the perimeter router to use
a backup route to the fiber connection using OSPF routing. The administrator notices all
traffic is going over the DSL connection and both links are working. Which of the following
should the administrator do to adjust the routing settings for the fiber connection to be used
by the router?
A. Add the DSL connection to the neighbor table for OSPF protocol
B. Change the routing protocol to EIGRP for the fiber connection
C. Increase the administrative distance of the DSL connection
D. Create a separate VLAN for the DSL connection

QUESTION NO: 589
A company is being acquired by a large corporation. As part of the acquisition process, the
company's address should now redirect clients to the corporate organization page. Which of
the following DNS records needs to be created?
A. SOA
B. NS
C. CNAME
D. TXT

QUESTION NO: 590
A company's web server is hosted at a local ISP. This is an example of:
A. colocation.
B. an on-premises data center.
C. a branch office.
D. a cloud provider.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 581
Answer: B. Reservation
Explanation: To ensure that a device with a specific MAC address is always assigned the same IP address from DHCP, the network administrator needs to configure a DHCP reservation. With a reservation, the DHCP server assigns a specific IP address to a device based on its MAC address.

QUESTION NO: 582
Answer: A. NTP
Explanation: Network Time Protocol (NTP) must be functioning properly in order for a network administrator to create an accurate timeline during a troubleshooting process. NTP ensures that the clocks on network devices are synchronized, allowing events to be accurately timestamped.

QUESTION NO: 583
Answer: A. Anti-tampering
             F. Video surveillance
Explanation: The BEST detective physical security devices for securing a network closet and detecting changes are:
- Anti-tampering devices: These can include seals, locks, or sensors that indicate if the closet has been tampered with.
- Video surveillance: Cameras can provide visual monitoring of the network closet, allowing for the detection of any unauthorized access or changes.

QUESTION NO: 584
Answer: D. Document the findings and actions
Explanation: After determining the cause of a network disruption, the NEXT step for the technician is to document the findings and actions taken. Proper documentation ensures that the troubleshooting process is recorded for future reference and helps in maintaining an accurate record of network issues and resolutions.

QUESTION NO: 585
Answer: D. LACP
Explanation: Link Aggregation Control Protocol (LACP) can be used to increase bandwidth to a server without replacing hardware. LACP allows multiple network ports to be combined into a single logical link, increasing bandwidth and providing redundancy.

QUESTION NO: 586
Answer: C. Change to a directional antenna
Explanation: To limit wireless access outside the building, the network administrator should change to a directional antenna. Directional antennas focus the wireless signal in a specific direction, reducing signal leakage outside the building and limiting access to unauthorized users.

QUESTION NO: 587
Answer: B. Peer-to-peer network
Explanation: A peer-to-peer network is composed of computers that can all communicate with one another with equal permissions and allows users to directly share what is on or attached to their computers. In a peer-to-peer network, each computer can act as both a client and a server.

QUESTION NO: 588
Answer: C. Increase the administrative distance of the DSL connection
Explanation: To adjust the routing settings for the fiber connection to be used by the router, the network administrator should increase the administrative distance of the DSL connection. This will make the router prefer the fiber connection over the DSL connection for routing traffic.

QUESTION NO: 589
Answer: C. CNAME
Explanation: To redirect clients to the corporate organization page, the network administrator needs to create a CNAME (Canonical Name) DNS record. The CNAME record is used to alias one domain name to another, allowing clients to access the corporate organization page using the company's domain name.

QUESTION NO: 590
Answer: A. Colocation
Explanation: Hosting the company's web server at a local ISP is an example of colocation. Colocation refers to the practice of housing privately-owned servers and networking equipment in a third-party data center facility, such as that of an ISP, where businesses can rent space for their equipment while still maintaining ownership and control over it.
''')
