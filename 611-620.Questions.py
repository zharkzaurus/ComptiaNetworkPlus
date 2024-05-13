print('''
QUESTION NO: 611
A company wants to implement a large number of WAPs throughout its building and allow
users to be able to move around the building without dropping their connections.
Which of the following pieces of equipment would be able to handle this requirement?
A. A VPN concentrator
B. A load balancer
C. A wireless controller
D. A RADIUS server

QUESTION NO: 612
Which of the following records can be used to track the number of changes on a DNS zone?
A. SOA
B. SRV
C. PTR
D. NS

QUESTION NO: 613
Which of the following is used to purposely attack a system to exploit vulnerabilities?
A. Honeypot
B. Vulnerability scan
C. Device hardening
D. Penetration testing

QUESTION NO: 614
A technician has been called about intermittent connectivity near IDF 2. Multiple cables were
recently pulled through a common conduit. Which of the following is MOST likely the cause of
the problem?
A. Crosstalk
B. Bad connectors
C. Wrong DNS
D. Duplicate IP address

QUESTION NO: 615
Which of the following protocols can be used to change device configurations via encrypted
and authenticated sessions? (Choose two.)
A. SNMPv3
B. SSH
C. Telnet
D. IPSec
E. ESP
F. Syslog

QUESTION NO: 616
A network administrator wants to improve the security of the management console on the
company's switches and ensure configuration changes made can be correlated to the
administrator who conformed them.
Which of the following should the network administrator implement?
A. Port security
B. Local authentication
C. TACACS+
D. Access control list

QUESTION NO: 617
A network engineer configured new firewalls with the correct configuration to be deployed to
each remote branch. Unneeded services were disabled, and all firewall rules were applied
successfully. Which of the following should the network engineer perform NEXT to ensure all
the firewalls are hardened successfully?
A. Ensure an implicit permit rule is enabled
B. Configure the log settings on the firewalls to the central syslog server
C. Update the firewalls with current firmware and software
D. Use the same complex passwords on all firewalls

QUESTION NO: 618
While setting up a new workstation, a technician discovers that the network connection is
only
100 full duplex (FD), although it is connected to a gigabit switch.
While reviewing the interface information in the switch CLI, the technician notes the port is
operating at IOOFD but Shows many RX and TX errors. The technician moves the computer
to another switchport and experiences the same issues.
Which of the following is MOST likely the cause of the low data rate and port errors?
A. Bad switch ports
B. Duplex issues
C. Cable length
D. Incorrect pinout

QUESTION NO: 619
A network is secured and is only accessible via TLS and IPSec VPNs. Which of the following
would need to be present to allow a user to access network resources on a laptop without
logging in to the VPN application?
A. Site-to-site
B. Secure Shell
C. In-band management
D. Remote desktop connection

QUESTION NO: 620
A technician is investigating an intermittent connectivity issue that occurs when specific
WAPs are turned on. The technician checks into the issue further and finds the WAPs that
are having issues share channel five. Which of the following is most likely causing the issue?
A. Polarization
B. Interference
C. Incorrect channel
D. Low power levels
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 611
Answer: C. A wireless controller
Explanation: A wireless controller would be able to handle the requirement of implementing a large number of Wireless Access Points (WAPs) throughout the building and allow users to move around without dropping their connections. A wireless controller centralizes the management and configuration of multiple WAPs, ensuring seamless roaming and consistent connectivity for users.

QUESTION NO: 612
Answer: A. SOA
Explanation: The Start of Authority (SOA) record in DNS can be used to track the number of changes on a DNS zone. The SOA record contains administrative information about the zone, including the serial number, which is incremented each time the zone is modified.

QUESTION NO: 613
Answer: D. Penetration testing
Explanation: Penetration testing is used to purposely attack a system to exploit vulnerabilities. It involves simulating real-world cyberattacks to identify weaknesses in systems, networks, or applications that could be exploited by malicious actors.

QUESTION NO: 614
Answer: A. Crosstalk
Explanation: Intermittent connectivity near IDF 2 after multiple cables were pulled through a common conduit is most likely caused by crosstalk. Crosstalk occurs when signals from one cable interfere with signals on adjacent cables, leading to signal degradation and intermittent connectivity issues.

QUESTION NO: 615
Answers:
B. SSH
D. IPSec
Explanation: SSH (Secure Shell) and IPSec (Internet Protocol Security) can be used to change device configurations via encrypted and authenticated sessions. SSH is commonly used for secure remote access to network devices, while IPSec provides secure communication between network devices over IP networks.

QUESTION NO: 616
Answer: C. TACACS+
Explanation: To improve the security of the management console on the company's switches and ensure configuration changes made can be correlated to the administrator who performed them, the network administrator should implement TACACS+ (Terminal Access Controller Access-Control System Plus). TACACS+ provides centralized authentication, authorization, and accounting (AAA) services for network devices.

QUESTION NO: 617
Answer: B. Configure the log settings on the firewalls to the central syslog server
Explanation: After configuring new firewalls with the correct settings, the network engineer should configure the log settings on the firewalls to the central syslog server. This ensures that firewall logs are centralized and can be monitored for security and troubleshooting purposes.

QUESTION NO: 618
Answer: B. Duplex issues
Explanation: The low data rate and port errors experienced by the technician, despite being connected to a gigabit switch, are most likely caused by duplex issues. The mismatched duplex settings between the switch and the workstation can lead to performance degradation and errors.

QUESTION NO: 619
Answer: A. Site-to-site
Explanation: To allow a user to access network resources on a laptop without logging in to the VPN application, a site-to-site VPN connection would need to be present. Site-to-site VPNs establish secure connections between different network locations, allowing users to access resources seamlessly as if they were on the same network.

QUESTION NO: 620
Answer: B. Interference
Explanation: The intermittent connectivity issue experienced when specific WAPs are turned on, which share channel five, is most likely caused by interference. Interference from other wireless devices or sources operating on the same frequency can disrupt Wi-Fi signals and cause connectivity issues.
''')
