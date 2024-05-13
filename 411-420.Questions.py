print('''
QUESTION NO: 411
A network administrator is configuring a database server and would like to ensure the
database engine is listening on a certain port. Which of the following commands should the
administrator use to accomplish this goal?
A.nslookup
B.netstat -a
C.ipconfig /a
D.arp -a

QUESTION NO: 412
A company wants an administrator to perform a vulnerability test. The administrator finds the
company has a POTS phone system. Which of the following can the administrator use to
point out the phone system vulnerability?
A. Honeypot
B. Butt set
C. Spyware
D. Blue jacking

QUESTION NO: 413
A network engineer needs to create a subnet that has the capacity for five VLANs, with the
following number of clients lo be allowed on each:
Which of the following is the SMALLEST subnet capable of this setup that also has the
capacity to double the number of clients in the future?
A. 10.0.0.0/21
B. 10.0.0.0/22
C. 10.0.0.0/23
D. 10.0.0.0/24

QUESTION NO: 414
Users in a branch can access an in-house database server, but it is taking too long to fetch
records. The analyst does not know whether the issue is being caused by network latency.
Which of the following will the analyst MOST likely use to retrieve the metrics that are needed
to resolve this issue?
A. SNMP
B. Link state
C. Syslog
D. QoS
E. Traffic shaping

QUESTION NO: 415
A network administrator installed an additional IDF during a building expansion project.
Which of the following documents need to be updated to reflect the change? (Choose two.)
A. Data loss prevention policy
B. BYOD policy
C. Acceptable use policy
D. Non-disclosure agreement
E. Disaster recovery plan
F. Physical network diagram

QUESTION NO: 416
During a client audit, a network analyst is tasked with recommending changes to upgrade the
client network and readiness. A field technician has submitted the following report:
Based on this report, which of the following metrics or sensors would be the BEST
recommendation to the client?
A. Electrical
B. Humidity
C. Flooding
D. Temperature

QUESTION NO: 417
A network technician is responding to an issue with a local company. To which of the
following documents should the network technician refer to determine the scope of the issue?
A. MTTR
B. MOU
C. NDA
D. SLA

QUESTION NO: 418
A company is utilizing multifactor authentication for data center access. Which of the
following is the MOST effective security mechanism against physical intrusions due to stolen
credentials?
A. Biometrics security hardware
B. Access card readers
C. Access control vestibule
D. Motion detection cameras

QUESTION NO: 419
A junior network engineer is trying to change the native network ID to a non-default value that
can then be applied consistently throughout the network environment. Which of the following
issues is the engineer attempting to prevent?
A. DDoS
B. ARP spoofing
C. VLAN hopping
D. Rogue DHCP

QUESTION NO: 420
A network engineer is troubleshooting application connectivity issues between a server and a
client. The network engineer needs to view the certificate exchange between the two hosts.
Which of the following tools should the network engineer use?
A. dig
B. tcpdump
C. nmap
D. traceroute
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 411
Answer: B
Explanation: To determine which port the database engine is listening on, the network administrator should use the "netstat -a" command. This command displays all active connections and listening ports on the system.

NO: 412
Answer: B
Explanation: To point out vulnerabilities in the POTS phone system, the administrator can use a butt set. A butt set is a lineman's handset that allows technicians to test and troubleshoot phone lines, identify line conditions, and monitor conversations. By using a butt set, the administrator can detect vulnerabilities and assess the security of the phone system.

NO: 413
Answer: C
Explanation: The SMALLEST subnet capable of accommodating five VLANs with 30 hosts each (allowing for future growth to double the number of clients) is a /23 subnet. A /23 subnet provides 510 usable IP addresses, which is sufficient for the current requirement and allows for future expansion.

NO: 414
Answer: A
Explanation: To retrieve metrics needed to determine if network latency is causing the slow database access, the analyst would most likely use SNMP (Simple Network Management Protocol). SNMP allows for the monitoring and collection of network performance data, including latency metrics, from network devices such as routers and switches.

NO: 415
Answer: F, E
Explanation: The documents that need to be updated to reflect the change of installing an additional IDF (Intermediate Distribution Frame) during a building expansion project are:
F. Physical network diagram: This diagram should be updated to include the new IDF and its connections.
E. Disaster recovery plan: The disaster recovery plan should be updated to reflect changes in network infrastructure to ensure effective recovery procedures.

NO: 416
Answer: D
Explanation: Based on the report provided by the field technician, the BEST recommendation to the client would be to implement temperature sensors. Temperature sensors can help monitor and maintain optimal conditions in server rooms and data centers to prevent overheating and potential equipment damage.

NO: 417
Answer: D
Explanation: To determine the scope of the issue with the local company, the network technician should refer to the SLA (Service Level Agreement). The SLA outlines the agreed-upon levels of service, including response times, resolution times, and responsibilities of both the company and the service provider.

NO: 418
Answer: A
Explanation: The MOST effective security mechanism against physical intrusions due to stolen credentials is biometrics security hardware. Biometrics, such as fingerprint or iris scanners, provide strong authentication based on unique physical characteristics, significantly reducing the risk of unauthorized access even with stolen credentials.

NO: 419
Answer: C
Explanation: The junior network engineer is attempting to prevent VLAN hopping by changing the native network ID to a non-default value consistent throughout the network environment. VLAN hopping is a security exploit that occurs when an attacker sends packets to a switch with a VLAN ID that does not exist on the trunk port, potentially allowing the attacker to gain unauthorized access to network resources in other VLANs.

NO: 420
Answer: B
Explanation: To view the certificate exchange between the server and client, the network engineer should use "tcpdump." Tcpdump is a command-line packet analyzer that captures and displays network packets, including SSL/TLS handshake messages, which contain certificate information exchanged during the connection establishment process.
''')
