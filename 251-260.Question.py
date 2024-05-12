print('''
QUESTION NO: 251
A technician is deploying a new switch model and would like to add it to the existing network
monitoring software. The technician wants to know what metrics can be gathered from a
given switch. Which of the following should the technician utilize for the switch?
A. MIB
B. Trap
C. Syslog
D. Audit log

QUESTION NO: 252
A network technician is configuring a new firewall for a company with the necessary access
requirements to be allowed through the firewall. Which of the following would normally be
applied as the LAST rule in the firewall?
A. Secure SNMP
B. Port security
C. Implicit deny
D. DHCP snooping

QUESTION NO: 253
A network technician is hired to review all the devices within a network and make
recommendations to improve network efficiency. Which of the following should the technician
do FIRST before reviewing and making any recommendations?
A. Capture a network baseline.
B. Perform an environmental review.
C. Read the network logs.
D. Run a bandwidth test.

QUESTION NO: 254
A technician would like to implement a low-latency Wi-Fi network. Which of the following
standards should the technician deploy for the network if the expected user bandwidth is
450Mbps?
A. 802.11a
B. 802.11b
C. 802.11g
D. 802.11n

QUESTION NO: 255
An ISP configured an internet connection to provide 20Mbps, but actual data rates are
occurring at 10Mbps and causing a significant delay in data transmission. Which of the
following specifications should the ISP check?
A. Throughput
B. Latency
C. Bandwidth
D. Jitter

QUESTION NO: 256
A network technician needs to install security updates on several switches on the company's
network. The management team wants this completed as quickly and efficiently as possible.
Which of the following should the technician do to perform the updates?
A. Upload the security update onto each switch using a terminal emulator and a console
cable.
B. Configure a TFTP server. SSH into each device, and perform the update.
C. Replace each old switch with new switches that have the updates already performed.
D. Connect a USB memory stick to each switch and perform the update.

QUESTION NO: 257
A network manager is configuring switches in IDFs to ensure unauthorized client computers
are not connecting to a secure wired network. Which of the following is the network manager
MOST likely performing?
A. Disabling unneeded switchports
B. Changing the default VLAN
C. Configuring DHCP snooping
D. Writing ACLs to prevent access to the switch

QUESTION NO: 258
A building was recently remodeled in order to expand the front lobby. Some mobile users
have been unable to connect to the available network jacks within the new lobby, while
others have had no issues. Which of the following is the most likely cause of the connectivity
issues?
A. LACP
B. Port security
C. 802.11 ax
D. Duplex settings

QUESTION NO: 259
A store owner would like to have secure wireless access available for both business
equipment and patron use. Which of the following features should be configured to allow
different wireless access through the same equipment?
A. MIMO
B. TKIP
C. LTE
D. SSID

QUESTION NO: 260
Which of the following OSI model layers is where conversations between applications are
established, coordinated, and terminated?
A. Session
B. Physical
C. Presentation
D. Data link''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO:251 = A
Explanation: The technician should utilize MIB (Management Information Base) to gather metrics from the switch. MIB is a database used to manage the entities in a communication network.

NO:252 = C
Explanation: The LAST rule in a firewall is usually an Implicit deny rule, which denies all traffic that doesn't match any of the preceding rules.

NO:253 = B
Explanation: Before reviewing and making recommendations to improve network efficiency, the technician should FIRST perform an environmental review to understand the network's physical layout, topology, and environmental factors.

NO:254 = D
Explanation: To implement a low-latency Wi-Fi network with an expected user bandwidth of 450Mbps, the technician should deploy the 802.11n standard, which offers higher data rates and better performance compared to 802.11a, 802.11b, or 802.11g.

NO:255 = A
Explanation: The ISP should check the Throughput specification to ensure that the actual data rates match the configured internet connection speed of 20Mbps.

NO:256 = B
Explanation: To perform security updates on several switches quickly and efficiently, the technician should configure a TFTP (Trivial File Transfer Protocol) server, SSH (Secure Shell) into each device, and perform the updates remotely.

NO:257 = C
Explanation: The network manager is most likely performing DHCP snooping to prevent unauthorized client computers from connecting to the secure wired network by monitoring DHCP messages and filtering unauthorized DHCP server replies.

NO:258 = B
Explanation: The most likely cause of the connectivity issues with the network jacks in the remodeled lobby is that the default VLAN configuration has changed, preventing some users from accessing the correct VLAN.

NO:259 = D
Explanation: To allow different wireless access through the same equipment, the SSID (Service Set Identifier) feature should be configured. Different SSIDs can be set up to segregate wireless traffic for business equipment and patron use.

NO:260 = A
Explanation: The Session layer of the OSI model is where conversations between applications are established, coordinated, and terminated. It provides services such as session establishment, maintenance, and termination.
''')
