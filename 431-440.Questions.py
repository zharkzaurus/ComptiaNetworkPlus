print('''
QUESTION NO: 431
Which of the following protocols would allow a secure connection to a Linux-based system?
A. SMB
B. FTP
C. RDP
D. SSH

QUESTION NO: 432
Two remote offices need to be connected securely over an untrustworthy MAN. Each office
needs to access network shares at the other site. Which of the following will BEST provide
this functionality?
A. Client-to-site VPN
B. Third-party VPN service
C. Site-to-site VPN
D. Split-tunnel VPN

QUESTION NO: 433
A packet is assigned a value to ensure it does not traverse a network indefinitely. Which of
the following BEST represents this value?
A. Zero Trust
B. Planned obsolescence
C. Time to live
D. Caching

QUESTION NO: 434
Which of the following connector types would have the MOST flexibility?
A. SFP
B. BNC
C. LC
D. RJ45

QUESTION NO: 435
Which of the following services can provide data storage, hardware options, and scalability to
a third-party company that cannot afford new devices?
A. SaaS
B. IaaS
C. PaaS
D. DaaS

QUESTION NO: 436
A technician wants to deploy a new wireless network that comprises 30 WAPs installed
throughout a three-story office building. All the APs will broadcast the same SSID for client
access. Which of the following BEST describes this deployment?
A. Extended service set
B. Basic service set
C. Unified service set
D. Independent basic service set

QUESTION NO: 437
A network administrator is trying to identify a device that is having issues connecting to a
switchport. Which of the following would BEST help identify the issue?
A. A syslog server
B. Change management records
C. A rack diagram
D. The security log

QUESTION NO: 438
A technician is connecting a Cat 6 Ethernet cable to a device that only has LC ports. Which
of the following will the technician MOST likely use to accomplish this task?
A. A bridge
B. A media converter
C. A repeater
D. A router

QUESTION NO: 439
A company's data center is hosted at its corporate office to ensure greater control over the
security of sensitive data. During times when there are increased workloads, some of the
company's non-sensitive data is shifted to an external cloud provider.
Which of the following cloud deployment models does this describe?
A. Hybrid
B. Community
C. Public
D. Private

QUESTION NO: 440
A network administrator needs to implement routing capabilities in a hypervisor. Which of the
following should the administrator most likely implement?
A. VPC
B. Firewall
C. NFV
D. laaS
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 431
Answer: D
Explanation: Secure Shell (SSH) is the protocol that would allow a secure connection to a Linux-based system. SSH provides encrypted communication over a network and allows users to securely access and manage remote systems. It provides strong authentication and secure encrypted data transmission, making it a common choice for accessing Linux servers remotely.

NO: 432
Answer: C
Explanation: To securely connect two remote offices over an untrustworthy MAN (Metropolitan Area Network) and allow each office to access network shares at the other site, the BEST solution would be to implement a Site-to-Site VPN (Virtual Private Network). A Site-to-Site VPN establishes a secure encrypted tunnel between the two office locations over the untrustworthy network, ensuring confidentiality and integrity of data transmission.

NO: 433
Answer: C
Explanation: The value assigned to a packet to ensure it does not traverse a network indefinitely is called the Time to Live (TTL). TTL is a field in the packet header that specifies the maximum number of router hops or network segments the packet can pass through before being discarded. It prevents packets from circulating endlessly in the network and helps to detect routing loops or misconfigurations.

NO: 434
Answer: A
Explanation: SFP (Small Form-factor Pluggable) connectors would have the most flexibility. SFP connectors are modular and support various types of transceivers, allowing them to be easily replaced or upgraded to accommodate different network requirements. They are commonly used in networking devices such as switches and routers to connect fiber optic or copper cables.

NO: 435
Answer: B
Explanation: Infrastructure as a Service (IaaS) can provide data storage, hardware options, and scalability to a third-party company that cannot afford new devices. With IaaS, companies can rent virtualized computing resources, including storage, networking, and servers, from a cloud provider on a pay-as-you-go basis, avoiding the need for upfront hardware investments.

NO: 436
Answer: A
Explanation: The deployment described, where multiple Wireless Access Points (WAPs) installed throughout a three-story office building broadcast the same SSID for client access, is known as an Extended Service Set (ESS). An ESS allows seamless roaming for wireless clients across multiple APs while maintaining connectivity to the same network.

NO: 437
Answer: A
Explanation: To identify a device having issues connecting to a switchport, a syslog server would be the BEST option. Syslog servers collect and store log messages generated by network devices, including information about network connectivity issues, errors, and warnings. Analyzing syslog messages can help identify the root cause of connectivity problems and troubleshoot network issues effectively.

NO: 438
Answer: B
Explanation: To connect a Cat 6 Ethernet cable to a device with only LC ports, the technician would most likely use a media converter. A media converter is a networking device that converts signals from one media type (such as copper to fiber) to another, allowing connectivity between devices with different interface types or physical media.

NO: 439
Answer: A
Explanation: The described scenario where a company hosts its sensitive data in its corporate data center while shifting non-sensitive data to an external cloud provider during times of increased workloads corresponds to a Hybrid cloud deployment model. A Hybrid cloud combines elements of both private and public clouds, allowing organizations to leverage the benefits of both environments while maintaining control over sensitive data.

NO: 440
Answer: C
Explanation: To implement routing capabilities in a hypervisor, the administrator would most likely implement Network Function Virtualization (NFV). NFV involves virtualizing network functions, such as routing, firewalling, and load balancing, and running them as software-based services on virtual machines or containers within the hypervisor environment. This enables flexible and scalable network infrastructure deployment and management within virtualized environments.
''')
