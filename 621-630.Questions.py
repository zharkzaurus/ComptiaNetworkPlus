print('''
QUESTION NO: 621
A technician restored network connectivity on a user's laptop. After validating full system
functionality, which of the following steps should the technician take NEXT?
A. Duplicate the problem, if possible
B. Determine if anything has changed
C. Test the theory to determine the cause
D. Document the findings, actions, and outcomes

QUESTION NO: 622
Which of the following is used when a workstation sends a DHCP broadcast to a server on
another LAN?
A. Reservation
B. Dynamic assignment
C. Helper address
D. DHCP offer

QUESTION NO: 623
A network technician needs to install the latest firmware on the switch to address a recently
discovered vulnerability. Which of the following should the technician do to have a rollback
plan in case of issues with the new firmware? (Choose two.)
A. Label the switch with IP address and firmware version
B. Draw the switchport diagram
C. Create a change management document
D. Draw the network rack logical diagram
E. Confirm standard operating procedures documentation
F. Create a performance baseline of the switch

QUESTION NO: 624
Which of the following is most closely associated with the management plane?
A. Routing table
B. Current configuration
C. File operations
D. Console port

QUESTION NO: 625
An engineer is troubleshooting poor performance on the network that occurs during work
hours.
Which of the following should the engineer do to improve performance?
A. Replace the patch cables.
B. Create link aggregation.
C. Create separation rules on the firewall.
D. Create subinterfaces on the existing port.

QUESTION NO: 626
A firewall administrator is implementing a rule that directs HTTP traffic to an internal server
listening on a non-standard socket.
Which of the following types of rules is the administrator implementing?
A. NAT
B. PAT
C. STP
D. SNAT
E. ARP

QUESTION NO: 627
A network technician is selecting a replacement for a damaged fiber cable that goes directly
to an SFP transceiver on a network switch. Which of the following cable connectors should
be used?
A. RJ45
B. LC
C. MT
D. F-type

QUESTION NO: 628
Which of the following VPN types provides the highest security for a user who travels often
but also has the highest bandwidth requirements to provide a satisfactory user experience?
A. Full-tunnel
B. Site-to-site
C. Clientless
D. Split-tunnel

QUESTION NO: 629
A customer cannot reach a web application on a local server. The network consultant
suspects that the server is not accepting the HTTPS connection. Which of the following
commands should the consultant run on the server to determine what is occurring?
A. route
B. arp
C. nmap
D. netstat

QUESTION NO: 630
During an annual review of policy documents, a company decided to adjust its recovery time
frames. The company agreed that critical applications can be down for no more than six
hours, and the acceptable amount of data loss is no more than two hours. Which of the
following should be documented as the RPO?
A. Two hours
B. Four hours
C. Six hours
D. Eight hours
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 621
Answer: D. Document the findings, actions, and outcomes
Explanation: After restoring network connectivity on a user's laptop and validating full system functionality, the next step for the technician should be to document the findings, actions taken, and outcomes. Proper documentation ensures that the resolution process is recorded for future reference and helps maintain an organized record of network troubleshooting activities.

QUESTION NO: 622
Answer: C. Helper address
Explanation: When a workstation sends a DHCP broadcast to a server on another LAN, a helper address is used to forward the DHCP broadcast to the DHCP server. The helper address, also known as DHCP relay agent address, allows DHCP requests to traverse between different network segments.

QUESTION NO: 623
Answers:
C. Create a change management document
E. Confirm standard operating procedures documentation
Explanation: To have a rollback plan in case of issues with the new firmware, the technician should:
- Create a change management document detailing the firmware update process, including rollback procedures.
- Confirm standard operating procedures documentation to ensure that proper procedures are followed during the firmware update and rollback process.

QUESTION NO: 624
Answer: D. Console port
Explanation: The management plane is most closely associated with the console port. The console port provides direct access to the device's management interface, allowing administrators to configure, monitor, and troubleshoot network devices.

QUESTION NO: 625
Answer: B. Create link aggregation.
Explanation: To improve performance on the network during work hours, the engineer should create link aggregation. Link aggregation, also known as port trunking or EtherChannel, combines multiple physical links between network devices into a single logical link to increase bandwidth and provide redundancy.

QUESTION NO: 626
Answer: D. SNAT
Explanation: The firewall administrator is implementing a rule that directs HTTP traffic to an internal server listening on a non-standard socket. This type of rule is associated with Source Network Address Translation (SNAT), which modifies the source IP address of outgoing packets to a different IP address.

QUESTION NO: 627
Answer: B. LC
Explanation: When selecting a replacement for a damaged fiber cable that goes directly to an SFP transceiver on a network switch, the technician should use an LC connector. LC connectors are commonly used with SFP (Small Form-factor Pluggable) transceivers and provide a secure and reliable connection for fiber optic cables.

QUESTION NO: 628
Answer: A. Full-tunnel
Explanation: The VPN type that provides the highest security for a user who travels often but also has the highest bandwidth requirements is Full-tunnel VPN. In a Full-tunnel VPN configuration, all user traffic, including internet traffic, is routed through the VPN tunnel, providing maximum security, but potentially impacting bandwidth due to the overhead of encrypting all traffic.

QUESTION NO: 629
Answer: D. netstat
Explanation: To determine if the server is not accepting the HTTPS connection, the network consultant should run the "netstat" command on the server. Netstat is a command-line network utility that displays network connections, routing tables, and network interface statistics, allowing the consultant to view the status of listening ports on the server.

QUESTION NO: 630
Answer: A. Two hours
Explanation: In the scenario described, where the acceptable amount of data loss is no more than two hours, the Recovery Point Objective (RPO) should be documented as two hours. RPO defines the maximum tolerable amount of data loss in the event of a disruption or disaster, indicating how much data the organization is willing to lose.
''')
