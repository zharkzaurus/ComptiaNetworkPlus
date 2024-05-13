print('''
QUESTION NO: 651
Which of the following is MOST commonly used to address CVEs on network equipment
and/or operating systems?
A. Vulnerability assessment
B. Factory reset
C. Firmware update
D. Screened subnet

QUESTION NO: 652
A company is considering shifting its business to the cloud. The management team is
concerned about the availability of the third-party cloud service. Which of the following should
the management team consult to determine the promised availability of the cloud provider?
A. Memorandum of understanding
B. Business continuity plan
C. Disaster recovery plan
D. Service-level agreement

QUESTION NO: 653
A network technician is manually configuring the network settings for a new device and is told
the network block is 192.168.0.0/20. Which of the following subnets should the technician
use?
A. 255.255.128.0
B. 255.255.192.0
C. 255.255.240.0
D. 255.255.248.0

QUESTION NO: 654
Which of the following documents is MOST likely to be associated with identifying and
documenting critical applications?
A. Software development life-cycle policy
B. User acceptance testing plan
C. Change management policy
D. Business continuity plan

QUESTION NO: 655
A network engineer receives the following when connecting to a switch to configure a port:
telnet 10.1.200.1
Connecting to 10.1.200.1..Could not open connection to the host, on
port 23: Connect failed.
Which of the following is the MOST likely cause for the failure?
A. The network engineer is using the wrong protocol
B. The network engineer does not have permission to configure the device
C. SNMP has been secured with an ACL
D. The switchport the engineer is trying to configure is down

QUESTION NO: 656
Which of the following is the most accurate NTP time source that is capable of being
accessed across a network connection?
A. Stratum 0 device
B. Stratum 1 device
C. Stratum 7 device
D. Stratum 16 device

QUESTION NO: 657
A network technician is selecting new network hardware, and availability is the main concern.
Which of the following availability concepts should the technician consider?
A. RTO
B. MTTR
C. MTBF
D. RPO

QUESTION NO: 658
Users report that a database server responds slowly or drops connections to other servers at
random during busy times. A technician notices the database and servers are connected to
an access switch in the office. Which of the following should the technician do to improve the
performance of the database server?
A. Use different ports on the access switch.
B. Implement LACP on the connection to the database server.
C. Move the cable connection for users to the same switch as the database server.
D. Move the server connection from the access switch to the core switch.

QUESTION NO: 659
An organization is interested in purchasing a backup solution that supports the organization's
goals. Which of the following concepts would specify the maximum duration that a given
service can be down before impacting operations?
A. MTTR
B. RTO
C. MTBF
D. RPO

QUESTION NO: 660
Which of the following addresses is a class B private address?
A. 132.216.14.184
B. 152.119.25.213
C. 162.17.43.22
D. 172.23.226.34
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 651
Answer: C. Firmware update
Explanation: The most common method used to address Common Vulnerabilities and Exposures (CVEs) on network equipment and operating systems is by applying firmware updates or patches provided by the vendor. These updates typically address known security vulnerabilities and help ensure the security of the system or device.

QUESTION NO: 652
Answer: D. Service-level agreement
Explanation: To determine the promised availability of a cloud provider, the management team should consult the Service-level agreement (SLA). An SLA is a contract between a service provider and a customer that outlines the agreed-upon levels of service, including availability, uptime guarantees, and performance metrics. It specifies the provider's commitment to maintaining the availability of their cloud services.

QUESTION NO: 653
Answer: C. 255.255.240.0
Explanation: The subnet mask /20 corresponds to the subnet mask 255.255.240.0. When configuring network settings for a device within the network block 192.168.0.0/20, the technician should use the subnet mask 255.255.240.0 to define the range of IP addresses available within that subnet.

QUESTION NO: 654
Answer: D. Business continuity plan
Explanation: Identifying and documenting critical applications is most likely associated with the Business continuity plan. A Business continuity plan (BCP) is a document that outlines procedures and protocols for maintaining essential business functions during and after a disaster or disruption. It typically includes information about critical applications, their dependencies, and strategies for ensuring their availability.

QUESTION NO: 655
Answer: A. The network engineer is using the wrong protocol
Explanation: The error message "Could not open connection to the host, on port 23: Connect failed" indicates that the network engineer is attempting to establish a Telnet connection to the switch but is unable to do so. The most likely cause for the failure is that the engineer is using the wrong protocol. Telnet typically operates on port 23, but if the switch is not configured to allow Telnet access or if another protocol is used for remote management (such as SSH), the connection will fail.

QUESTION NO: 656
Answer: B. Stratum 1 device
Explanation: The most accurate Network Time Protocol (NTP) time source that is capable of being accessed across a network connection is a Stratum 1 device. Stratum 1 devices are directly connected to an authoritative time source, such as an atomic clock or GPS receiver, and serve as primary time servers. They have the highest level of accuracy and reliability in the NTP hierarchy.

QUESTION NO: 657
Answer: C. MTBF
Explanation: When selecting new network hardware with availability as the main concern, the technician should consider Mean Time Between Failures (MTBF). MTBF is a measure of a system's reliability and represents the average time between consecutive failures of a hardware component or system. A higher MTBF value indicates greater reliability and longer intervals between failures.

QUESTION NO: 658
Answer: D. Move the server connection from the access switch to the core switch.
Explanation: To improve the performance of the database server and reduce network congestion, the technician should consider moving the server connection from the access switch to the core switch. Core switches typically have higher bandwidth and throughput capabilities, making them better suited for handling traffic between critical servers and other network devices.

QUESTION NO: 659
Answer: B. RTO
Explanation: The concept that specifies the maximum duration that a given service can be down before impacting operations is known as Recovery Time Objective (RTO). RTO defines the acceptable amount of time it takes to restore a service or system after a disruption or outage. It helps organizations determine their recovery capabilities and plan accordingly to minimize downtime.

QUESTION NO: 660
Answer: D. 172.23.226.34
Explanation: The class B private address range is 172.16.0.0 to 172.31.255.255. Among the given options, 172.23.226.34 falls within this range and is therefore a class B private address. Class B addresses have the first two octets reserved for the network portion, allowing for a larger number of networks compared to class A addresses.
''')
