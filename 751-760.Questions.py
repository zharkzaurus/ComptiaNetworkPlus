print('''
QUESTION NO: 751
Which of the following is required when connecting an endpoint device with an RJ45 port to a
network device with an ST port?
A. A media converter
B. A bridge
C. An MDIX
D. A load balancer

QUESTION NO: 752
In the past, users brought personal laptops to the office to bypass some of the security
protocols on their desktops. Due to new security initiatives, management has asked that
users not be allowed to attach personal devices to the network. Which of the following should
a technician use to BEST meet this goal?
A. Shut down unused ports on switches
B. Upgrade firmware on network devices
C. Allow only secure protocols on the network
D. Disable unnecessary services

QUESTION NO: 753
Which of the following fiber connector types is the most likely to be used on a network
interface card?
A. LC
B. SC
C. ST
D. MPO

QUESTION NO: 754
A network attack caused a network outage by wiping the configuration and logs of the border
firewall. Which of the following sources, in an investigation to determine how the firewall was
compromised, can provide the MOST detailed data?
A. Syslog server messages
B. MIB of the attacked firewall
C. Network baseline reports
D. NetFlow aggregate data

QUESTION NO: 755
The Chief Executive Officer of a company wants to ensure business operations are not
disrupted in the event of a disaster. The solution must have fully redundant equipment, real-
time synchronization, and zero data loss. Which of the following should be prepared?
A. Cloud site
B. Warm site
C. Hot site
D. Cold site

QUESTION NO: 756
A network contains 25 access points. Which of the following devices would be best to change
configurations on all the devices remotely?
A. WLAN controller
B. Load balancer
C. Bridge
D. Layer 3 switch

QUESTION NO: 757
Which of the following is an advanced distance vector routing protocol that automates routing
tables and also uses some features of link-state routing protocols?
A. OSPF
B. RIP
C. EIGRP
D. BGP

QUESTION NO: 758
Which of the following uses the destination IP address to forward packets?
A. A bridge
B. A Layer 2 switch
C. A router
D. A repeater

QUESTION NO: 759
A network technician needs to ensure outside users are unable to telnet into any of the
servers at the datacenter. Which of the following ports should be blocked when checking
firewall configuration?
A. 22
B. 23
C. 80
D. 3389
E. 8080

QUESTION NO: 760
A company wants to invest in new hardware for the core network infrastructure. The
management team requires that the infrastructure be capable of being repaired in less than
60 minutes if any major part fails. Which of the following metrics is MOST likely associated
with this requirement?
A. RPO
B. MTTR
C. FHRP
D. MTBF
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Here are the answers with explanations:

QUESTION NO: 751
Answer: A. A media converter
Explanation: When connecting an endpoint device with an RJ45 port to a network device with an ST port (a fiber optic port), a media converter is required to convert between the electrical signals of the RJ45 port and the optical signals of the ST port.

QUESTION NO: 752
Answer: A. Shut down unused ports on switches
Explanation: To prevent users from attaching personal devices to the network, a technician can shut down unused ports on switches. This prevents unauthorized access through physical network connections.

QUESTION NO: 753
Answer: A. LC
Explanation: The LC (Lucent Connector) is the most common fiber connector type used on network interface cards (NICs) and other network equipment due to its small size and popularity in data center environments.

QUESTION NO: 754
Answer: A. Syslog server messages
Explanation: Syslog server messages can provide detailed data about network events, including information about the network attack that caused the firewall outage. Syslog messages often contain valuable information for forensic analysis and troubleshooting.

QUESTION NO: 755
Answer: C. Hot site
Explanation: A hot site is a fully redundant facility equipped with real-time synchronization and zero data loss capabilities. It is designed to ensure business continuity in the event of a disaster by providing immediate failover and minimal downtime.

QUESTION NO: 756
Answer: A. WLAN controller
Explanation: A WLAN (Wireless Local Area Network) controller would be the best device to change configurations on all the access points remotely. WLAN controllers centralize management and configuration of multiple access points, allowing for efficient management of the entire wireless network.

QUESTION NO: 757
Answer: C. EIGRP
Explanation: EIGRP (Enhanced Interior Gateway Routing Protocol) is an advanced distance vector routing protocol that automates routing tables and incorporates some features of link-state routing protocols, such as rapid convergence and partial updates.

QUESTION NO: 758
Answer: C. A router
Explanation: A router uses the destination IP address in packet headers to forward packets between different networks or subnets. Routers operate at the network layer (Layer 3) of the OSI model.

QUESTION NO: 759
Answer: B. 23
Explanation: Telnet typically uses port 23 for communication. To prevent outside users from telnetting into any of the servers at the datacenter, port 23 should be blocked when checking firewall configuration.

QUESTION NO: 760
Answer: B. MTTR (Mean Time to Repair)
Explanation: MTTR (Mean Time to Repair) is the metric associated with the time it takes to repair a failed component or system and restore it to full functionality. In this scenario, the requirement of being capable of being repaired in less than 60 minutes aligns with the concept of MTTR.
''')
