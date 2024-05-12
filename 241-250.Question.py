print('''
QUESTION NO: 241
All packets arriving at an interface need to be fully analyzed. Which of the following features
should be used to enable monitoring of the packets?
A. LACP
B. Flow control
C. Port mirroring
D. NetFlow exporter

QUESTION NO: 242
A network engineer needs to change an entire subnet of SLAAC-configured workstation
addresses. Which of the following methods would be the best for the engineer to use?
A. Change the address prefix in ARP in order for the workstations to retrieve their new
addresses.
B. Change the address prefix in a router in order for the router to advertise the new prefix
with an ND.
C. Change the address prefix scope in a DHCP server in order for the workstations to retrieve
their new addresses.
D. Change the workstations' address prefix manually because an automated method does
not exist.

QUESTION NO: 243
The process of grouping network interfaces together to increase throughput is called:
A. VLAN tagging
B. load balancing
C. port aggregation
D. fault tolerance

QUESTION NO: 244
An email server, which is called "Frederick," has an IPv6 address of 2001:5689:23:ABCD:6A,
but most users call it "Fred" for short. Which of the following DNS entries is needed so the
alias
"Fred" can also be used?
A. MX
B. AAAA
C. SRV
D. CNAME
E. TXT
F. NS

QUESTION NO: 245
A Fortune 500 company would like to move its on-premises corporate email systems to a
multitenant product hosted in the cloud where no maintenance of the underlying server OS or
platform is required. Which of the following BEST represents the model the company should
choose?
A. Public
B. Private
C. Hybrid
D. Community

QUESTION NO: 246
A network technician is having issues connecting an IoT sensor to the internet. The WLAN
settings were entered via a custom command line, and a proper IP address assignment was
received on the wireless interface. However, when trying to connect to the internet, only
HTTP redirections are being received when data is requested. Which of the following will
point to the root cause of the issue?
A. Verifying if an encryption protocol mismatch exists.
B. Verifying if a captive portal is active for the WLAN.
C. Verifying the minimum RSSI for operation in the device's documentation.
D. Verifying EIRP power settings on the access point.

QUESTION NO: 247
A network technician is deploying multiple switches for a new office. The switches are
separately managed and need to be cabled in to support dual firewalls in a HA setup. Which
of the following should the technician enable to support proper stability of the network
switches?
A. NTP
B. CDMA
C. STP
D. LACP
E. 802.1Q

QUESTION NO: 248
A network administrator has received calls every day for the past few weeks from three users
who cannot access the network. The administrator asks all the users to reboot their PCs, but
the same users still cannot access the system. The following day, three different users report
the same issue, and the administrator asks them all to reboot their PCs; however, this does
not fix the issue. Which of the following is MOST likely occurring?
A. Incorrect firewall settings
B. Inappropriate VLAN assignment
C. Hardware failure
D. Overloaded CAM table in switch
E. DHCP scope exhaustion

QUESTION NO: 249
Which of the following compromises Internet-connected devices and makes them vulnerable
to becoming part of a botnet? (Choose two.)
A. Deauthentication attack
B. Malware infection
C. IP spoofing
D. Firmware corruption
E. Use of default credentials
F. Dictionary attack

QUESTION NO: 250
A network administrator is checking to see if anything has changed. Which of the following
steps of the troubleshooting methodology is involved?
A. Identify the problem.
B. Test the theory.
C. Establish a theory.
D. Document findings.''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO:241 = C
Explanation: Port mirroring should be used to enable monitoring of all packets arriving at an interface by duplicating them to another port where monitoring can take place.

NO:242 = B
Explanation: The network engineer should change the address prefix in a router so that the router can advertise the new prefix with Neighbor Discovery (ND) messages, allowing the SLAAC-configured workstations to retrieve their new addresses.

NO:243 = C
Explanation: The process of grouping network interfaces together to increase throughput is called port aggregation, also known as link aggregation or Ethernet bonding.

NO:244 = D
Explanation: To create an alias "Fred" for the email server "Frederick," a CNAME (Canonical Name) DNS entry should be used.

NO:245 = A
Explanation: The company should choose the Public cloud model for moving its on-premises corporate email systems to a multitenant product hosted in the cloud, where no maintenance of the underlying server OS or platform is required.

NO:246 = B
Explanation: The root cause of the issue is likely a captive portal active for the WLAN, which redirects HTTP requests for authentication before allowing internet access.

NO:247 = C
Explanation: The network technician should enable STP (Spanning Tree Protocol) to support proper stability of the network switches and prevent loops in the network topology.

NO:248 = D
Explanation: The most likely issue occurring is an overloaded CAM (Content Addressable Memory) table in the switch, which is causing connectivity issues for users.

NO:249 = B, E
Explanation: Malware infection and the use of default credentials compromise Internet-connected devices and make them vulnerable to becoming part of a botnet.

NO:250 = C
Explanation: The step of checking to see if anything has changed falls under establishing a theory in the troubleshooting methodology.
''')
