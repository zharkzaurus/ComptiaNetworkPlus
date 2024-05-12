print('''
QUESTION NO: 271
Which of the following layers of the OSI model lies between the transport layer and the
network layer?
A. Application
B. Data link
C. Session
D. Presentation

QUESTION NO: 272
A website administrator is concerned the company's static website could be defaced by
hacktivists or used as a pivot point to attack internal systems.
Which of the following should a network security administrator recommend to assist with
detecting these activities?
A. Implement file integrity monitoring.
B. Change the default credentials.
C. Use SSL encryption.
D. Update the web-server software.

QUESTION NO: 273
In which of the following scenarios should a technician use a cross-over cable to provide
connectivity?
A. PC to switch
B. Switch to AP
C. Router to switch
D. Router to modem
E. PC to PC

QUESTION NO: 274
A home user states during a basement remodel, one of the workers cut the network cable
that goes from the modem to the WAP and nothing else has changed. According to the
network troubleshooting methodology, which of the following is the NEXT step?
A. Identify the problem
B. Question the user
C. Establish a plan of action
D. Establish a theory of probable cause

QUESTION NO: 275
An IT administrator received an assignment with the following objectives:
- Conduct a total scan within the company's network for all connected hosts.
- Detect all the types of operating systems running on all devices.
- Discover all services offered by hosts on the network.
- Find open ports and detect security risks.
Which of the following command-line tools can be used to achieve these objectives?
A. nmap
B. arp
C. netstat
D. tcpdump

QUESTION NO: 276
A network administrator connects two unmanaged switches together with a straight-through
Ethernet cable. The administrator reviews the connection and notices that the uplinks are not
on.
Which of the following options offers the best solution for the issue?
A. A rollover cable needs to be used.
B. The switches needs to be rebooted after connecting.
C. The ports need to be enabled.
D. The ports need the IP address configured.
E. A crossover cable needs to be used.

QUESTION NO: 277
While using a secure conference call connection over a corporate VPN, a user moves from a
cellular connection to a hotel wireless network. Although the wireless connection and the
VPN show a connected status, no network connectivity is present. Which of the following is
the MOST likely cause of this issue?
A. MAC filtering is configured on the wireless connection.
B. The VPN and the WLAN connection have an encryption protocol mismatch.
C. The WLAN is using a captive portal that requires further authentication.
D. Wireless client isolation is enforced on the WLAN settings.

QUESTION NO: 278
A technician is assisting a user who cannot access network resources when the workstation
is connected to a VoIP phone. The technician identifies the phone as faulty and replaces it.
According to troubleshooting methodology, which of the following should the technician do
NEXT?
A. Implement the solution.
B. Test the theory.
C. Duplicate the issue.
D. Document the findings.
E. Verify functionality.

QUESTION NO: 279
Due to concerns around single points of failure, a company decided to add an additional
WAN to the network. The company added a second MPLS vendor to the current MPLS WAN
and deployed an additional WAN router at each site. Both MPLS providers use OSPF on the
WAN network, and EIGRP is run internally. The first site to go live with the new WAN is
successful, but when the second site is activated significant network issues occur. Which of
the following is the MOST likely cause for the WAN instability?
A. A routing loop
B. Asymmetrical routing
C. A switching loop
D. An incorrect IP address

QUESTION NO: 280
During a recent security audit, a contracted penetration tester discovered the organization
uses a number of insecure protocols. Which of the following ports should be disallowed so
only encrypted protocols are allowed? (Choose two.)
A. 22
B. 23
C. 69
D. 443
E. 587
F. 8080''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO:271 = C
Explanation: The Session layer lies between the Transport layer and the Network layer in the OSI model.

NO:272 = A
Explanation: Implementing file integrity monitoring would assist in detecting unauthorized changes to the static website, helping to identify defacement or potential attacks.

NO:273 = E
Explanation: A crossover cable should be used for direct PC-to-PC connections, allowing for the exchange of data between two computers without the need for a switch or hub.

NO:274 = B
Explanation: Questioning the user is the next step in the troubleshooting methodology, allowing the technician to gather more information about the problem and its potential causes.

NO:275 = A
Explanation: The nmap command-line tool can be used to conduct network scans, detect operating systems, discover services, and find open ports, making it suitable for achieving the stated objectives.

NO:276 = C
Explanation: Enabling the ports on the unmanaged switches would allow the uplinks to become active and establish connectivity between the switches.

NO:277 = C
Explanation: The lack of network connectivity after moving to the hotel wireless network suggests that the WLAN may be using a captive portal that requires further authentication before allowing access to the network.

NO:278 = E
Explanation: After replacing the faulty VoIP phone, the technician should verify functionality to ensure that the issue has been resolved.

NO:279 = B
Explanation: Asymmetrical routing, where traffic takes different paths between sites, can occur when using multiple WAN connections with different routing protocols, leading to network instability.

NO:280 = D, F
Explanation: Disallowing ports 69 (TFTP) and 8080 (HTTP alternate) would ensure that only encrypted protocols are allowed, enhancing security by preventing the use of insecure protocols.
''')
