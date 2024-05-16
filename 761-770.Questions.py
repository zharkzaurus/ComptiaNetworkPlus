print('''
QUESTION NO: 761
A systems operator is granted access to a monitoring application, configuration application,
and timekeeping application. The operator is denied access to the financial and project
management applications by the system's security configuration. Which of the following
BEST describes the security principle in use?
A. Network access control
B. Least privilege
C. Multifactor authentication
D. Separation of duties

QUESTION NO: 762
Which of the following architectures is used for FTP?
A. Client-server
B. Service-oriented
C. Connection-oriented
D. Data-centric

QUESTION NO: 763
Which of the following describes a manually entered route?
A. Static
B. Dynamic
C. Multicast
D. Unicast

QUESTION NO: 764
Two new network switches located in different buildings are connected together with single-
mode fiber. However, no link exists between the two switches. Which of the following steps
should the technician perform FIRST to troubleshoot the issue?
A. Reverse TX/RX on the fiber patch cord at one building.
B. Replace the fiber patch cords in both buildings.
C. Clean the fiber patch cord connectors in both buildings.
D. Connect the fiber patch cord to an OTDR at one building.

QUESTION NO: 765
Which of the following network topologies contains a direct connection between every node
in the network?
A. Mesh
B. Hub-and-spoke
C. Star
D. Point-to-point

QUESTION NO: 766
A company has experienced a major security breach. Which of the following should the
network administrator reference to determine the next steps?
A. Non-disclosure policy
B. Data loss prevention policy
C. Acceptable use policy
D. Incident response policy

QUESTION NO: 767
Which of the following is conducted frequently to maintain an updated list of a system's
weaknesses?
A. Penetration test
B. Posture assessment
C. Risk assessment
D. Vulnerability scan

QUESTION NO: 768
Which of the following is most likely to have the HIGHEST latency while being the most
accessible?
A. Satellite
B. DSL
C. Cable
D. 4G

QUESTION NO: 769
A network technician visits a site that needs voice connectivity to the corporate office and
installs four IP phones. The phone exchange resides at the telephone company. Which of the
following technologies is being used?
A. Virtual switch
B. Virtual server
C. Virtual desktop
D. Virtual PBX

QUESTION NO: 770
At which of the following OSI model layers does a MAC filter list for a wireless infrastructure
operate?
A. Physical
B. Network
C. Session
D. Data link
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Here are the answers with explanations:

QUESTION NO: 761
Answer: B. Least privilege
Explanation: The principle of least privilege grants users only the permissions they need to perform their tasks and restricts access to other resources. In this scenario, the systems operator is granted access only to specific applications necessary for their role while being denied access to other applications, aligning with the principle of least privilege.

QUESTION NO: 762
Answer: A. Client-server
Explanation: FTP (File Transfer Protocol) uses a client-server architecture, where one device (the client) requests files from another device (the server) over a network connection.

QUESTION NO: 763
Answer: A. Static
Explanation: A manually entered route is referred to as a static route. Static routes are configured by a network administrator and remain unchanged until manually modified or removed.

QUESTION NO: 764
Answer: A. Reverse TX/RX on the fiber patch cord at one building.
Explanation: When troubleshooting a situation where two network switches connected by single-mode fiber have no link, reversing the transmit (TX) and receive (RX) connections on one end of the fiber patch cord is the first step. This action corrects any misalignment between the transmit and receive fibers.

QUESTION NO: 765
Answer: A. Mesh
Explanation: A mesh network topology contains a direct connection between every node in the network, providing redundancy and multiple paths for data to travel.

QUESTION NO: 766
Answer: D. Incident response policy
Explanation: In the event of a major security breach, the network administrator should reference the incident response policy to determine the next steps for containing, mitigating, and recovering from the breach.

QUESTION NO: 767
Answer: D. Vulnerability scan
Explanation: Vulnerability scans are conducted frequently to maintain an updated list of a system's weaknesses by identifying security vulnerabilities, misconfigurations, and potential threats within the network infrastructure.

QUESTION NO: 768
Answer: A. Satellite
Explanation: Satellite connections typically have the highest latency among the options listed due to the long distance data must travel to reach the satellite and back.

QUESTION NO: 769
Answer: D. Virtual PBX
Explanation: A Virtual PBX (Private Branch Exchange) is a telephone switching system hosted by a telephone company that provides voice connectivity to corporate offices and allows for features like call routing, voicemail, and auto-attendant services.

QUESTION NO: 770
Answer: D. Data link
Explanation: A MAC (Media Access Control) filter list for a wireless infrastructure operates at the Data Link layer (Layer 2) of the OSI model. MAC filtering allows or denies network access based on the MAC addresses of devices trying to connect to the wireless network.
''')
