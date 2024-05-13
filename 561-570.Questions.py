print('''
QUESTION NO: 561
A network manager wants to set up a remote access system for the engineering staff. Access
to this system will be over a public IP and secured with an ACL. Which of the following best
describes this system?
A. VPN
B. Secure Shell
C. Jump server
D. API

QUESTION NO: 562
A fiber link connecting two campus networks is broken. Which of the following tools should an
engineer use to detect the exact break point of the fiber link?
A. OTDR
B. Tone generator
C. Fusion splicer
D. Cable tester
E. PoE injector

QUESTION NO: 563
An IP camera has a failed PoE NIC. This is the third time in months that a PoE NIC has failed
on this device. The technician suspects a possible power issue. Which of the following should
be used to test the theory?
A. Toner probe
B. Loopback plug
C. Protocol analyzer
D. Multimeter

QUESTION NO: 564
Which of the following is the IEEE link cost for a Fast Ethernet interface in STP calculations?
A. 2
B. 4
C. 19
D. 100

QUESTION NO: 565
A company just migrated its email service to a cloud solution. After the migration, two-thirds
of the internal users were able to connect to their mailboxes, but the connection fails for the
other one- third of internal users. Users working externally are not reporting any issues. The
network administrator identifies the following output collected from an internal host:
c:\user> nslookup newmail.company.com
Non-Authoritative answer:
Name: newmail.company.com
IPs: 3.219.13.186, 64.58.225.184, 184.168.131.243
Which of the following verification tasks should the network administrator perform NEXT?
A. Check the firewall ACL to verify all required IP addresses are included.
B. Verify the required router PAT rules are properly configured.
C. Confirm the internal DNS server is replying to requests for the cloud solution.
D. Validate the cloud console to determine whether there are unlicensed requests.

QUESTION NO: 566
An organization with one core and five distribution switches is transitioning from a star to a
full- mesh topology.
Which of the following is the number of additional network connections needed?
A. 5
B. 7
C. 10
D. 15

QUESTION NO: 567
Which of the following would be used to expedite MX record updates to authoritative NSs?
A. UDP forwarding
B. DNS caching
C. Recursive lookup
D. Time to live

QUESTION NO: 568
A network administrator needs to back up the configurations of all network devices and store
the configurations off-line until they are needed. Which of the following should the
administrator use to back up the configurations securely?
A. SFTP
B. Syslog
C. Telnet
D. SNMP

QUESTION NO: 569
Due to an increase in wireless demand, 50 additional access points were installed as part of
an expansion project. Each device was configured and managed separately, working with its
own configuration. Which of the following network devices would assist the network team with
reducing complexity and enforcing policies on the WLAN?
A. Wireless controller
B. Wireless range extender
C. Wireless load balancer
D. Wireless analyzer

QUESTION NO: 570
A technician is troubleshooting a previously encountered issue. Which of the following should
the technician reference to find what solution was implemented to resolve the issue?
A. Standard operating procedures
B. Configuration baseline documents
C. Work instructions
D. Change management documentation
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 561
Answer: C. Jump server
Explanation: A jump server is a system on a network used to access and manage devices in a separate security zone. It allows remote access over a public IP while being secured with an Access Control List (ACL). Engineering staff can connect to the jump server, which then facilitates access to the secured devices.

QUESTION NO: 562
Answer: A. OTDR
Explanation: An Optical Time Domain Reflectometer (OTDR) is used to detect the exact break point of a fiber link. It sends optical pulses into the fiber and measures the backscattered light to determine the location and severity of any breaks or bends in the fiber optic cable.

QUESTION NO: 563
Answer: D. Multimeter
Explanation: To test the theory of a possible power issue causing the PoE NIC failures, a technician should use a multimeter. A multimeter can measure electrical parameters such as voltage, current, and resistance, allowing the technician to diagnose and verify the power supply to the IP camera.

QUESTION NO: 564
Answer: A. 2
Explanation: The IEEE link cost for a Fast Ethernet interface in Spanning Tree Protocol (STP) calculations is 19. This value is used to determine the path cost or distance to the root bridge in the network topology.

QUESTION NO: 565
Answer: C. Confirm the internal DNS server is replying to requests for the cloud solution.
Explanation: Since internal users are having trouble connecting to the cloud email service, the network administrator should verify that the internal DNS server is correctly resolving requests for the cloud solution. If the DNS server is not responding with the appropriate IP addresses for the cloud service, internal users will be unable to connect.

QUESTION NO: 566
Answer: C. 10
Explanation: In a full-mesh topology, each device is directly connected to every other device in the network. With one core switch and five distribution switches, there are a total of six devices. To transition from a star topology to a full-mesh topology, additional connections are needed between each device, resulting in a total of 10 additional network connections.

QUESTION NO: 567
Answer: D. Time to live
Explanation: Time to live (TTL) is a value in a DNS record that specifies the amount of time for which the record can be cached before it expires. Lowering the TTL value would expedite MX (Mail Exchange) record updates to authoritative Name Servers (NSs) by instructing DNS resolvers to refresh the cached records more frequently.

QUESTION NO: 568
Answer: A. SFTP
Explanation: Secure File Transfer Protocol (SFTP) should be used to securely back up the configurations of all network devices and store them offline. SFTP provides encrypted file transfer over a secure channel, ensuring the confidentiality and integrity of the backup configurations.

QUESTION NO: 569
Answer: A. Wireless controller
Explanation: A wireless controller would assist the network team with reducing complexity and enforcing policies on the WLAN. It centralizes the management of multiple access points, allowing for easier configuration, monitoring, and enforcement of wireless policies across the network.

QUESTION NO: 570
Answer: D. Change management documentation
Explanation: To find what solution was implemented to resolve the previously encountered issue, the technician should reference the change management documentation. This documentation records all changes made to the network infrastructure, including the implementation of solutions to resolve issues or address changes in the network environment.
''')
