print('''
QUESTION NO: 731
Which of the following is used to provide disaster recovery capabilities to spin up all critical
devices using internet resources?
A. Cloud site
B. Hot site
C. Cold site
D. Warm site

QUESTION NO: 732
A recently constructed building makes use of glass and natural light. Users in the building are
reporting poor cellular connectivity and speeds. Which of the following is MOST likely the
cause?
A. Absorption
B. Channel overlap
C. Reflection
D. Frequency mismatch

QUESTION NO: 733
An IT intern moved the location of a WAP from one conference room to another. The WAP
was unable to boot following the move. Which of the following should be used to fix the
issue?
A. Antenna
B. WLAN controller
C. Media converter
D. PoE injector

QUESTION NO: 734
After HVAC failures caused network outages, the support team decides to monitor the
temperatures of all the devices. The network administrator cannot find a command that will
display this information. Which of the following will retrieve the necessary information?
A. SNMP OID values
B. NetFlow data export
C. Network baseline configurations
D. Security information and event management

QUESTION NO: 735
A network engineer performs the following tasks to increase server bandwidth:
- Connects two network cables from the server to a switch stack
- Configure LACP on the switchports
- Verifies the correct configurations on the switch interfaces
Which of the following needs to be configured on the server?
A. Load balancing
B. Multipathing
C. NIC teaming
D. Clustering

QUESTION NO: 736
Which of the following can be used to centrally manage credentials for various types of
administrative privileges on configured network devices?
A. SSO
B. TACACS+
C. Zero Trust
D. Separation of duties
E. Multifactor authentication

QUESTION NO: 737
A network technician receives a support ticket concerning multiple users who are unable to
access the company's shared drive. The switch interface that the shared drive is connected
to is displaying the following:
 GigabitEthernet 0/9 is down, line protocol is down (notconnected)
        Hardware is Gigabit Ethernet, address is C800.84df.9847 (via c800.84bf.9847)
        MTU 1500 bytes, BW 10000 Kbit / sec, DLY 1000 usec,
        reliability 255/255, txload 1/225. rxload 1/255
        Encapsulation ARPA, loopback not set
Which of the following is MOST likely the issue?
A. The switchport is shut down.
B. The cable is not plugged in.
C. The loopback is not set.
D. The bandwidth configuration is incorrect.

QUESTION NO: 738
A user wants to avoid using a password to access a third-party website. Which of the
following does the user need in order to allow this type of access to the third-party website?
A. Multifactor
B. RADIUS
C. SSO
D. Local authentication

QUESTION NO: 739
A network engineer is investigating reports of poor network performance. Upon reviewing a
report, the engineer finds hundreds of CRC errors on an interface. Which of the following is
the MOST likely cause of these errors?
A. A bad wire on the Cat 5e cable
B. The wrong VLAN assignment to the switchport
C. A misconfigured QoS setting on the router
D. Both sides of the switch trunk set to full duplex

QUESTION NO: 740
Which of the following options represents the participating computers in a network?
A. Nodes
B. CPUs
C. Servers
D. Clients
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 731
Answer: A. Cloud site
Explanation: A cloud site refers to disaster recovery capabilities provided through internet resources, allowing critical devices and services to be spun up in the cloud in the event of a disaster.

QUESTION NO: 732
Answer: C. Reflection
Explanation: The use of glass and natural light in the building likely causes reflection of cellular signals, leading to poor connectivity and speeds for users inside the building.

QUESTION NO: 733
Answer: D. PoE injector
Explanation: If the WAP (Wireless Access Point) is unable to boot after being moved, it might not be receiving power properly. Using a PoE (Power over Ethernet) injector can provide power to the WAP, resolving the issue.

QUESTION NO: 734
Answer: A. SNMP OID values
Explanation: SNMP (Simple Network Management Protocol) OID (Object Identifier) values can be used to retrieve temperature information from network devices, allowing the network administrator to monitor temperatures and prevent network outages due to HVAC failures.

QUESTION NO: 735
Answer: C. NIC teaming
Explanation: NIC (Network Interface Card) teaming allows multiple network interfaces on a server to work together as a single, aggregated network interface, increasing server bandwidth and providing redundancy.

QUESTION NO: 736
Answer: B. TACACS+
Explanation: TACACS+ (Terminal Access Controller Access-Control System Plus) can be used to centrally manage credentials for various types of administrative privileges on configured network devices, providing authentication, authorization, and accounting (AAA) services.

QUESTION NO: 737
Answer: A. The switchport is shut down.
Explanation: The switch interface being shut down is the most likely cause of the issue where multiple users are unable to access the company's shared drive connected to that switch interface.

QUESTION NO: 738
Answer: C. SSO
Explanation: Single Sign-On (SSO) allows users to access multiple applications or websites with a single set of login credentials, avoiding the need for passwords for each individual service.

QUESTION NO: 739
Answer: A. A bad wire on the Cat 5e cable
Explanation: CRC errors often indicate data corruption during transmission, which can be caused by physical issues such as a bad wire in the Cat 5e cable.

QUESTION NO: 740
Answer: A. Nodes
Explanation: In a network, the participating computers are referred to as nodes. Nodes can include servers, clients, routers, switches, and other network devices.
''')
