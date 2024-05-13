print('''
QUESTION NO: 521
To access production applications and data, developers must first connect remotely to a
different server.
From there, the developers are able to access production data. Which of the following does
this BEST represent?
A. A management plane
B. A proxy server
C. An out-of-band management device
D. A site-to-site VPN
E. A jump box

QUESTION NO: 522
A disgruntled employee executes a man-in-the-middle attack on the company network. Layer
2 traffic destined for the gateway is redirected to the employee's computer. This type of
attack is an example of:
A. ARP cache poisoning
B. IP spoofing
C. amplified DNS attack
D. evil twin

QUESTION NO: 523
Which of the following characteristics allows an 802.11g WAP to have transfer speeds up to
108Mbps?
A. MIMO technology
B. Channel bonding
C. Encryption type
D. Frequency

QUESTION NO: 524
Which of the following are environmental factors that should be considered when installing
equipment in a building? (Choose two.)
A. Fire suppression system
B. UPS location
C. Humidity control
D. Power load
E. Floor construction type
F. Proximity to nearest MDF

QUESTION NO: 525
A security team would like to use a system in an isolated network to record the actions of
potential attackers. Which of the following solutions is the security team implementing?
A. Perimeter network
B. Honeypot
C. Zero trust infrastructure
D. Network segmentation

QUESTION NO: 526
A technician is trying to configure a previously owned WAP. The technician successfully logs
into the administrative console and attempts to input the IP address on the WAP. However,
the WAP is not accepting the command. Which of the following is causing the problem?
A. The WAP antenna is damaged
B. The WAP transmitter light is dim
C. The terminal emulation software is misconfigured
D. The LWAPP image is installed on the WAP

QUESTION NO: 527
A technician replaces a failed router with a spare that has been in inventory for some time.
After attempting to enable HTTPS on the spare router, the technician discovers the feature is
unavailable. The support office was able to connect to the previous router. Which of the
following actions should the technician perform to enable HTTPS access for the support
team?
A. Reboot the router
B. Enable HTTP on the router
C. Update the firmware of the spare router
D. Perform a factory reset on the router

QUESTION NO: 528
Which of the following would be used to filter web traffic based on content?
A. Proxy server
B. Load balancer
C. Media converter
D. Access point

QUESTION NO: 529
To comply with industry requirements, a security assessment on the cloud server should
identify which protocols and weaknesses are being exposed to attackers on the Internet.
Which of the following tools is the MOST appropriate to complete the assessment?
A. Use tcpdumpand parse the output file in a protocol analyzer.
B. Use an IP scanner and target the cloud WAN network addressing.
C. Run netstat in each cloud server and retrieve the running processes.
D. Use nmapand set the servers' public IPs as the targets.

QUESTION NO: 530
Lisa, a technician, is tasked to monitor various analog POTS lines for voice activity. Which of
the following hardware tools would be used?
A. Butt set
B. Toner probe
C. Wire mapper
D. Cable certifier
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 521
Answer: E
Explanation: A jump box.
This scenario BEST represents the use of a jump box. A jump box (also known as a jump host or a bastion host) is a secure computer that serves as an intermediary connection point for accessing production servers and data from remote locations. Developers connect remotely to the jump box, and from there, they can access production applications and data. The jump box adds an additional layer of security by controlling and monitoring access to sensitive resources.

QUESTION NO: 522
Answer: A
Explanation: ARP cache poisoning.
This type of attack is an example of ARP cache poisoning. ARP (Address Resolution Protocol) cache poisoning, also known as ARP spoofing, involves manipulating the ARP cache of a network device to associate a different MAC address with the IP address of another device, redirecting traffic intended for that device to the attacker's computer. In this scenario, the attacker redirects Layer 2 traffic destined for the gateway to their own computer, allowing them to intercept and potentially manipulate the traffic.

QUESTION NO: 523
Answer: B
Explanation: Channel bonding.
Channel bonding is the characteristic that allows an 802.11g Wireless Access Point (WAP) to have transfer speeds up to 108Mbps. Channel bonding involves combining multiple adjacent channels to increase the overall bandwidth available for data transmission. In the case of 802.11g, channel bonding allows the WAP to use two channels simultaneously, effectively doubling the data transfer rate compared to using a single channel.

QUESTION NO: 524
Answer: C, D
Explanation:
- Humidity control: Humidity levels in the environment can affect the performance and reliability of network equipment. High humidity can lead to corrosion and electrical shorts, while low humidity can increase the risk of static electricity buildup.
- Power load: The power load refers to the amount of electrical power consumed by the equipment in a building. It's important to consider the power load to ensure that the electrical infrastructure can support the equipment without overloading circuits or causing power disruptions.

QUESTION NO: 525
Answer: B
Explanation: Honeypot.
The security team is implementing a honeypot, which is a system designed to lure potential attackers and gather information about their tactics, techniques, and procedures. By deploying a honeypot in an isolated network, the security team can monitor and analyze the actions of potential attackers without putting production systems at risk. Honeypots are valuable tools for threat intelligence gathering and can help organizations improve their cybersecurity defenses.

QUESTION NO: 526
Answer: D
Explanation: The LWAPP image is installed on the WAP.
The problem is likely caused by the Lightweight Access Point Protocol (LWAPP) image installed on the WAP. LWAPP is a protocol used by Cisco wireless LAN controllers (WLCs) to manage lightweight access points (APs). If the WAP has an LWAPP image installed, it may be controlled by a WLC and configured centrally rather than through its own administrative console. To configure the WAP, the technician may need to connect it to the appropriate WLC and manage it through the controller interface.

QUESTION NO: 527
Answer: C
Explanation: Update the firmware of the spare router.
The technician should update the firmware of the spare router to enable HTTPS access for the support team. Firmware updates often include bug fixes, security patches, and feature enhancements, so updating the firmware may enable missing features or resolve compatibility issues. By updating the firmware, the technician can ensure that the spare router has the latest software version with all the necessary features enabled.

QUESTION NO: 528
Answer: A
Explanation: Proxy server.
A proxy server is used to filter web traffic based on content. It acts as an intermediary between clients and servers, intercepting requests from clients and forwarding them to the appropriate servers. By configuring the proxy server to inspect and filter web traffic, administrators can enforce content filtering policies to block or allow specific websites or content categories based on predefined rules.

QUESTION NO: 529
Answer: D
Explanation: Use nmap and set the servers' public IPs as the targets.
The most appropriate tool to complete the assessment is to use nmap and set the servers' public IPs as the targets. nmap (Network Mapper) is a powerful open-source tool used for network discovery and security auditing. By scanning the servers' public IPs, the security team can identify open ports, running services, and potential vulnerabilities exposed to attackers on the Internet.

QUESTION NO: 530
Answer: A
Explanation: Butt set.
To monitor various analog Plain Old Telephone Service (POTS) lines for voice activity, Lisa would use a butt set. A butt set, also known as a lineman's handset or test set, is a handheld device used by technicians to test and monitor telephone lines. It allows technicians to listen to and monitor voice transmissions on analog telephone lines, making it suitable for tasks such as testing for voice activity on POTS lines.
''')
