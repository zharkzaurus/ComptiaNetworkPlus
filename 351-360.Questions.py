print('''
QUESTION NO: 351
A network technician reviews an entry on the syslog server and discovers the following
message from a switch:
SPANNING-TREE Port 1/1 BLOCKED
Which of the following describes the issue?
A. A loop was discovered, and the impact was mitigated.
B. An incorrectly pinned cable was disconnected.
C. The link-local address on the port is incorrect.
D. The port was shut down, and it needs to be reactivated.

QUESTION NO: 352
A technician thinks one of the router ports is flapping. Which of the following available
resources should the technician use in order to determine if the router is flapping?
A. Audit logs
B. NetFlow
C. Syslog
D. Traffic logs

QUESTION NO: 353
Several employees have expressed concerns about the company monitoring their internet
activity when they are working from home. The company wants to mitigate this issue and
reassure employees that their private internet activity is not being monitored. Which of the
following would satisfy company and employee needs?
A. Split tunnel
B. Full tunnel
C. Site-to-site tunnel
D. Virtual desktop

QUESTION NO: 354
Which of the following protocol types describes secure communication on port 443?
A. ICMP
B. UDP
C. TCP
D. IP

QUESTION NO: 355
Which of the following would be the BEST choice to connect branch sites to a main office
securely?
A. VPN headend
B. Proxy server
C. Bridge
D. Load balancer

QUESTION NO: 356
A technician was cleaning a storage closet and found a box of transceivers labeled 8Gbps.
Which of the following protocols uses those transceivers?
A. Coaxial over Ethernet
B. Internet Small Computer Systems Interface
C. Fibre Channel
D. Gigabit interface converter

QUESTION NO: 357
A technician is troubleshooting a report about network connectivity issues on a workstation.
Upon investigation, the technician notes the workstation is showing an APIPA address on the
network interface. The technician verifies that the VLAN assignment is correct and that the
network interface has connectivity. Which of the following is MOST likely the issue the
workstation is experiencing?
A. DHCP exhaustion
B. A rogue DHCP server
C. A DNS server outage
D. An incorrect subnet mask

QUESTION NO: 358
Which of the following describes traffic going in and out of a data center from the internet?
A. Demarcation point
B. North-South
C. Fibre Channel
D. Spine and leaf

QUESTION NO: 359
A network technician is reviewing an upcoming project's requirements to implement laaS.
Which of the following should the technician consider?
A. Software installation processes
B. Type of database to be installed
C. Operating system maintenance
D. Server hardware requirements

QUESTION NO: 360
Which of the following is a security flaw in an application or network?
A. A threat
B. A vulnerability
C. An exploit
D. A risk
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 351
Answer: A. A loop was discovered, and the impact was mitigated.
Explanation: The message indicates that spanning-tree protocol has blocked port 1/1 to prevent a loop in the network, mitigating any potential impact.

QUESTION NO: 352
Answer: C. Syslog
Explanation: Syslog can provide information about router port status and any flapping occurrences, helping the technician determine if the router port is indeed flapping.

QUESTION NO: 353
Answer: A. Split tunnel
Explanation: Implementing split tunnel VPN allows the company to route only work-related traffic through the corporate network, reassuring employees that their private internet activity is not being monitored while maintaining security for work-related traffic.

QUESTION NO: 354
Answer: C. TCP
Explanation: Secure communication on port 443 is typically associated with TCP (Transmission Control Protocol), commonly used for HTTPS (HTTP over SSL/TLS) connections.

QUESTION NO: 355
Answer: A. VPN headend
Explanation: VPN headend provides a secure way to connect branch sites to a main office over the internet, establishing encrypted tunnels for secure communication.

QUESTION NO: 356
Answer: C. Fibre Channel
Explanation: Transceivers labeled as 8Gbps are typically used in Fibre Channel networks, which provide high-speed, reliable communication for storage area networks (SANs).

QUESTION NO: 357
Answer: B. A rogue DHCP server
Explanation: The presence of an APIPA address on the workstation suggests that it has not received a valid IP address from a DHCP server. A rogue DHCP server may be issuing incorrect IP addresses, causing connectivity issues.

QUESTION NO: 358
Answer: B. North-South
Explanation: Traffic going in and out of a data center from the internet is often referred to as North-South traffic.

QUESTION NO: 359
Answer: D. Server hardware requirements
Explanation: When implementing IaaS (Infrastructure as a Service), considerations such as server hardware requirements are essential for provisioning virtual machines and allocating resources.

QUESTION NO: 360
Answer: B. A vulnerability
Explanation: A vulnerability refers to a security flaw in an application or network that can potentially be exploited by attackers to compromise security.
''')
