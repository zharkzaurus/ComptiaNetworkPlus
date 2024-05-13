print('''
QUESTION NO: 501
A user recently made changes to a PC that caused it to be unable to access websites by
both FQDN and IP Local resources, such as the file server remain accessible. Which of the
following settings did the user MOST likely misconfigure?
A. Static IP
B. Default gateway
C. DNS entries
D. Local host file

QUESTION NO: 502
A network administrator redesigned the positioning of the APs to create adjacent areas of
their devices maintain an association to a distanced AP. Which of the following should the
network administrator check FIRST?
A. Validate the roaming settings on the APs and WLAN clients
B. Verify that the AP antenna type is correct for the new layout
C. Check to see if MU-MIMO was properly activated on the APs
D. Deactivate the 2.4GHz band on the APS

QUESTION NO: 503
A security engineer is trying to determine whether an internal server was accessed by hosts
on the internet. The internal server was shut down during the investigation.
Which of the following will the engineer review to determine whether the internal server had
an unauthorized access attempt?
A. The ARP table
B. The NetFlow statistics
C. The firewall logs
D. The audit logs on the core switch

QUESTION NO: 504
An organization requires the ability to send encrypted email messages to a partner from an
email server that is hosted on premises. The organization prefers to use the standard default
ports when creating firewall rules. Which of the following ports should be open to satisfy the
requirements?
A. 110
B. 143
C. 587
D. 636

QUESTION NO: 505
A disaster recovery team needs a solution that would best meet the following requirements:
- The server infrastructure has been pre-installed
- The fail-over location offers basic life support.
- The fail-over location provides basic network connectivity.
- Minimizing cost is preferred over quicker business recovery times
- The expected time for services to be fully operational is days.
Which of the following sites would meet the requirements?
A. Cold site
B. Cloud site
C. Warm site
D. Hot site

QUESTION NO: 506
Which of the following is the LARGEST MTU for a standard Ethernet frame?
A. 1452
B. 1492
C. 1500
D. 2304

QUESTION NO: 507
Which of the following WAN technologies utilizes an optical SONET carrier and has a
maximum bandwidth of 155.54Mbps?
A. DS3
B. E3
C. OC3
D. T3

QUESTION NO: 508
A network technician is troubleshooting a specific port on a switch. Which of the following
commands should the technician use to see the port configuration?
A. show route
B. show interface
C. show arp
D. show port

QUESTION NO: 509
Which of the following cables supports 10Gbps throughput and 100 meters as the maximum
distance?
A. T1 crossover
B. Singlemode fiber
C. CAT6a
D. Coaxial

QUESTION NO: 510
A company wants to add a local redundant data center to its network in case of failure at its
primary location. Which of the following would give the LEAST amount of redundancy for the
company's network?
A. Cold site
B. Hot site
C. Cloud site
D. Warm site
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 501
Answer: C
Explanation: The correct answer is C. DNS entries. If the user is unable to access websites by both FQDN (Fully Qualified Domain Name) and IP address, it suggests a DNS (Domain Name System) misconfiguration. DNS is responsible for translating domain names to IP addresses. If DNS entries are incorrect, the system won't be able to resolve domain names to their corresponding IP addresses, resulting in the inability to access websites.

QUESTION NO: 502
Answer: A
Explanation: The correct answer is A. Validate the roaming settings on the APs and WLAN clients. When redesigning the positioning of APs to create adjacent areas, ensuring seamless roaming is crucial for devices to maintain an association with the closest AP as they move between areas. Checking and validating the roaming settings on both the APs and WLAN clients would be the first step to troubleshoot any issues related to roaming.

QUESTION NO: 503
Answer: C
Explanation: The correct answer is C. The firewall logs. Reviewing the firewall logs would provide insight into whether the internal server had unauthorized access attempts from hosts on the internet. Firewall logs typically record incoming and outgoing traffic, including attempts to access specific services or ports on internal servers. Analyzing these logs can help identify any suspicious or unauthorized activity.

QUESTION NO: 504
Answer: C
Explanation: The correct answer is C. 587. Port 587 is the standard port for email message submission, typically used for sending encrypted email messages from email clients to an email server. It's commonly used for secure SMTP (Simple Mail Transfer Protocol) communication with STARTTLS encryption. Opening port 587 on the firewall would allow the organization to send encrypted email messages to its partner from the on-premises email server.

QUESTION NO: 505
Answer: A
Explanation: The correct answer is A. Cold site. A cold site is a disaster recovery site that offers minimal infrastructure and resources. It typically provides only basic life support facilities, such as power and cooling, along with basic network connectivity. A cold site requires the organization to install and configure its own server infrastructure and recover data from backups, which can take days or even weeks to become fully operational.

QUESTION NO: 506
Answer: C
Explanation: The correct answer is C. 1500. The largest MTU (Maximum Transmission Unit) for a standard Ethernet frame is 1500 bytes. This MTU size is commonly used in Ethernet networks and is often referred to as the Ethernet MTU. It represents the maximum payload size that can be transmitted in a single Ethernet frame without fragmentation.

QUESTION NO: 507
Answer: C
Explanation: The correct answer is C. OC3. OC3 (Optical Carrier 3) is a WAN (Wide Area Network) technology that utilizes an optical SONET (Synchronous Optical Networking) carrier. It has a maximum bandwidth of 155.52 Mbps (megabits per second). OC3 is commonly used for high-speed data transmission over long-distance fiber optic links.

QUESTION NO: 508
Answer: B
Explanation: The correct answer is B. show interface. To troubleshoot a specific port on a switch and see its configuration, the network technician should use the "show interface" command. This command provides detailed information about the status and configuration of switch interfaces, including the port in question.

QUESTION NO: 509
Answer: C
Explanation: The correct answer is C. CAT6a. CAT6a (Category 6a) cable supports 10 Gbps (Gigabits per second) throughput and has a maximum distance of 100 meters when used for 10GBASE-T Ethernet connections. It offers higher performance and better bandwidth compared to earlier Ethernet cable categories like CAT5e.

QUESTION NO: 510
Answer: A
Explanation: The correct answer is A. Cold site. A cold site offers the least amount of redundancy for a company's network. In a cold site, infrastructure and resources are minimal, typically providing only basic life support facilities and basic network connectivity. Unlike hot sites or warm sites, which have pre-installed server infrastructure and may offer quicker recovery times, cold sites require the organization to set up and configure its own equipment in the event of a disaster.
''')
