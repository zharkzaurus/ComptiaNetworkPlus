print('''
QUESTION NO: 471
Which of the following attack vectors represents a large number of devices sending access
requests to a website, making it unavailable to respond?
A. Virus
B. Botnet
C. ARP spooling
D. DDoS

QUESTION NO: 472
Which of the following layers of the OSI model has new protocols activated when a user
moves from a wireless to a wired connection?
A. Data link
B. Network
C. Transport
D. Session

QUESTION NO: 473
A technician finds that the network card is no longer functioning. At which of the following OSI
layers is the problem occurring?
A. Layer 1
B. Layer 3
C. Layer 5
D. Layer 7

QUESTION NO: 474
A network technician is designing a SOHO environment where cost is a consideration. The
requirements include access to the Internet and access to the guest house which is 100 feet
away. The location of the Internet modem is located in the main house. Which of the
following is the BEST option to accomplish these requirements?
A. Use two combined Internet/router/wireless devices, one in each house.
B. Use a Layer 3 switch in the main house and a combined Internet/router/wireless device in
the guest house.
C. Use a combined Internet/router/wireless device in the main house and a wireless access
point in the guest house.
D. Use a single combined Internet/router/wireless device at the guest house.

QUESTION NO: 475
Which of the following routing protocols is generally used by major ISPs for handling large-
scale internet traffic?
A. RIP
B. EIGRP
C. OSPF
D. BGP

QUESTION NO: 476
A Wi-Fi network was recently deployed in a new, multilevel building. Several issues are now
being reported related to latency and drops in coverage. Which of the following is the FIRST
step to troubleshoot the issues?
A. Perform a site survey.
B. Review the AP placement
C. Monitor channel utilization.
D. Test cable attenuation.

QUESTION NO: 477
A company is contracting a new third-party organization that will handle storage of the
company's critical data. Which of the following policies would ensure the data remains
confidential?
A. SLA
B. NDA
C. MOU
D. BYOD

QUESTION NO: 478
An IT technician installs five old switches in a network. In addition to the low port rates on
these switches, they also have improper network configurations. After three hours, the
network becomes overwhelmed by continuous traffic and eventually shuts down. Which of
the following is causing the issue?
A. Broadcast storm
B. Collisions
C. IP settings
D. Routing loops

QUESTION NO: 479
An engineer recently decided to upgrade the firmware on a router. During the upgrade, the
help desk received calls about a network outage, and a critical ticket was opened. The
network manager would like to create a policy to prevent this from happening in the future.
Which of the following documents should the manager create?
A. Change management
B. incident response
C. Standard operating procedure
D. System life cycle

QUESTION NO: 480
A small office is looking to deploy wireless to cover one half of the work area only. The
technician is restricted to suspending the WAP in the middle of the office due to network jack
limitations.
Which of the following antenna types would BEST meet these requirements?
A. Dipole
B. Parabolic
C. Directional
D. Omni-directional
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 471
Answer: D
Explanation: The correct answer is D. DDoS (Distributed Denial of Service) attack involves a large number of devices, often part of a botnet, sending access requests to a website or online service simultaneously, overwhelming its capacity to respond. This flood of traffic makes the service unavailable to legitimate users.

QUESTION NO: 472
Answer: A
Explanation: The correct answer is A. Data link. The Data Link layer of the OSI model is responsible for addressing physical devices on the network. When a user moves from a wireless to a wired connection, new protocols are activated at the Data Link layer to establish communication over the new physical medium.

QUESTION NO: 473
Answer: A
Explanation: The correct answer is A. Layer 1. The OSI model Layer 1, the Physical layer, deals with the physical connection between devices. A malfunctioning network card indicates a problem at Layer 1, as it relates to the physical hardware.

QUESTION NO: 474
Answer: C
Explanation: The correct answer is C. Use a combined Internet/router/wireless device in the main house and a wireless access point in the guest house. This option provides a cost-effective solution for providing Internet access to both the main house and the guest house. The combined Internet/router/wireless device in the main house can serve as the primary access point, while a wireless access point in the guest house can extend the wireless network coverage to reach that area.

QUESTION NO: 475
Answer: D
Explanation: The correct answer is D. BGP (Border Gateway Protocol). BGP is generally used by major ISPs (Internet Service Providers) for handling large-scale internet traffic and routing between autonomous systems on the internet.

QUESTION NO: 476
Answer: A
Explanation: The correct answer is A. Perform a site survey. Performing a site survey is the first step to troubleshoot Wi-Fi issues in a multilevel building. A site survey helps identify areas with coverage gaps, interference, or other issues affecting Wi-Fi performance. By conducting a thorough site survey, network administrators can gather data to optimize AP placement, channel selection, and other configuration settings to improve Wi-Fi performance and address latency and coverage drop issues.

QUESTION NO: 477
Answer: B
Explanation: The correct answer is B. NDA (Non-Disclosure Agreement). A Non-Disclosure Agreement (NDA) is a legal document that ensures the confidentiality of sensitive information shared between parties. In the context of the scenario, the NDA would ensure that the third-party organization handling storage of the company's critical data maintains confidentiality and does not disclose the data to unauthorized parties.

QUESTION NO: 478
Answer: A
Explanation: The correct answer is A. Broadcast storm. A broadcast storm occurs when network devices continuously broadcast excessive traffic, overwhelming the network and causing performance degradation or network outages. In this scenario, the installation of old switches with improper network configurations likely led to a broadcast storm, causing the network to become overwhelmed by continuous traffic and eventually shutting down.

QUESTION NO: 479
Answer: A
Explanation: The correct answer is A. Change management. Change management is the process of managing changes to the network infrastructure in a controlled and systematic manner. Creating a change management policy would help prevent network outages during firmware upgrades by establishing procedures for testing, scheduling, and implementing changes in a way that minimizes disruptions to network operations.

QUESTION NO: 480
Answer: C
Explanation: The correct answer is C. Directional. A directional antenna focuses its signal in one direction, making it ideal for covering specific areas with targeted wireless coverage. In this scenario, where the technician is restricted to suspending the WAP in the middle of the office due to network jack limitations, a directional antenna would be the best choice for providing wireless coverage to only one half of the work area.
''')
