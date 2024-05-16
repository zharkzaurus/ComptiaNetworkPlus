print('''
QUESTION NO: 781
A technician must install and configure a network device in a building with 20 classrooms.
Each room must be on a separate subnet and should not be able to see traffic from other
subnets.
Which of the following is the MOST cost-effective solution?
A. A switch with VLANs created for each segment
B. A router with interfaces connected to a switch in each room
C. A VoIP endpoint connected to a hub for each network
D. A firewall with DHCP pools for each subnet

QUESTION NO: 782
Which of the following are standard fiber cable connector types? (Select TWO).
A. RJ-11
B. F-connector
C. MTRJ
D. DB-9
E. ST

QUESTION NO: 783
An administrator is able to list the interfaces on a switch after providing the community string
"public". Which of the protocols is the administrator MOST likely using?
A. Telnet
B. RADIUS
C. SSH
D. SNMP

QUESTION NO: 784
Which of the following is required for hosts to receive DHCP addresses from a server that is
located on a different subnet?
A. DHCP scope
B. DHCP snooping
C. DHCP reservations
D. DHCP relay

QUESTION NO: 785
A technician wants to monitor and provide traffic segmentation across the network.
The technician would like to assign each department a specific identifier.
Which of the following will the technician MOST likely use?
A. Flow control
B. Traffic shaping
C. VLAN tagging
D. Network performance baselines

QUESTION NO: 786
A network technician notices the site-to-site VPN and Internet connection have not come
back up at a branch office after a recent power outage. Which of the following is an out-of-
band method the technician would MOST likely utilize to check the branch office's router
status?
A. Use a modem to console into the router
B. Walk a user through troubleshooting the connection
C. Travel to the branch office
D. Hire a contractor to go on-site

QUESTION NO: 787
Which of the following documents would be used to define uptime commitments from a
provider, along with details on measurement and enforcement?
A. NDA
B. SLA
C. MOU
D. AUP

QUESTION NO: 788
A cafeteria is facing lawsuits related to criminal internet access that was made over its guest
network. The marketing team, however, insists on keeping the cafeteria's phone number as
the wireless passphrase. Which of the following actions would improve wireless security
while accommodating the marketing team and accepting the terms of use?
A. Setting WLAN security to use EAP-TLS
B. Deploying a captive portal for user authentication
C. Using geofencing to limit the area covered by the WLAN
D. Configuring guest network isolation

QUESTION NO: 789
A network administrator is testing performance improvements by configuring channel bonding
on an 802.11ac AP. Although a site survey detected the majority of the 5GHz frequency
spectrum was idle, being used only by the company's WLAN and a nearby government radio
system, the AP is not allowing the administrator to manually configure a large portion of the
5GHz frequency range. Which of the following would be BEST to configure for the WLAN
being tested?
A. Upgrade the equipment to an AP that supports manual configuration of the ElRP power
settings.
B. Switch to 802.11n, disable channel auto-selection, and enforce channel bonding on the
configuration.
C. Set up the AP to perform a dynamic selection of the frequency according to regulatory
requirements.
D. Deactivate the band 5GHz to avoid Interference with the government radio

QUESTION NO: 790
A network administrator decides to secure their small network by allowing only specific MAC
addresses to gain access to the network from specific switches. Which of the following is
described by this example?
A. Packet filtering
B. Hardware firewalls
C. Port security
D. Stateful inspection
''')
Answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 781
Answer: A. A switch with VLANs created for each segment
Explanation: Using a switch with VLANs created for each segment is the most cost-effective solution to achieve network segmentation in this scenario. VLANs allow the network to be divided into separate broadcast domains, ensuring that traffic from one classroom subnet does not interfere with traffic from other subnets.

QUESTION NO: 782
Answers: C. MTRJ
             E. ST
Explanation: MTRJ and ST are standard fiber cable connector types. MTRJ is a small form factor connector commonly used for duplex communication, while ST (Straight Tip) is a bayonet-style connector used in older networking equipment.

QUESTION NO: 783
Answer: D. SNMP
Explanation: SNMP (Simple Network Management Protocol) is commonly used for network monitoring and management. Providing the community string "public" suggests that SNMP is being used to access management information on the switch.

QUESTION NO: 784
Answer: D. DHCP relay
Explanation: DHCP relay is required for hosts to receive DHCP addresses from a server located on a different subnet. DHCP relay agents forward DHCP messages between clients and servers across different network segments.

QUESTION NO: 785
Answer: C. VLAN tagging
Explanation: VLAN tagging allows for traffic segmentation across the network by assigning each department or group a specific VLAN identifier. This ensures that traffic from different departments remains separate, even though they may be transmitted over the same physical network infrastructure.

QUESTION NO: 786
Answer: A. Use a modem to console into the router
Explanation: Using a modem to console into the router provides an out-of-band method for accessing the device's console interface. This allows the technician to check the router's status and troubleshoot connectivity issues remotely, even if the main network connections are down.

QUESTION NO: 787
Answer: B. SLA
Explanation: An SLA (Service Level Agreement) document defines uptime commitments from a provider, along with details on measurement and enforcement. It outlines the expected level of service and the consequences if the service levels are not met.

QUESTION NO: 788
Answer: D. Configuring guest network isolation
Explanation: Configuring guest network isolation would improve wireless security by ensuring that devices connected to the guest network cannot communicate with each other. This prevents potential criminal internet access from one guest device to another, while still accommodating the marketing team's preference for using the cafeteria's phone number as the wireless passphrase.

QUESTION NO: 789
Answer: C. Set up the AP to perform dynamic selection of the frequency according to regulatory requirements.
Explanation: Setting up the AP to perform dynamic selection of the frequency ensures compliance with regulatory requirements while optimizing WLAN performance. It allows the AP to automatically select the best available frequency channels within the 5GHz spectrum, considering interference and regulatory restrictions.

QUESTION NO: 790
Answer: C. Port security
Explanation: Port security involves securing a network by allowing only specific MAC addresses to gain access to the network from specific switches. This helps prevent unauthorized devices from connecting to the network and enhances network security.
''')
