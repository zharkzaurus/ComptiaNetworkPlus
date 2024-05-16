print('''
QUESTION NO: 791
A malicious user is using special software to perform an on-path attack. Which of the
following best practices should be configured to mitigate this threat?
A. Dynamic ARP inspection
B. Role-based access
C. Control plane policing
D. MAC filtering

QUESTION NO: 792
Which of the following would MOST likely be used to review previous upgrades to a system?
A. Business continuity plan
B. Change management
C. System life cycle
D. Standard operating procedures

QUESTION NO: 793
Which of the following is used to require network devices to authenticate before gaining
access to a LAN?
A. 802.1Q
B. 802.1X
C. 802.11ax
D. 802.3af

QUESTION NO: 794
A company recently added an addition to their office building. A technician runs new plenum
network cables from the switch on one side of the company's gymnasium 80 meters (262 ft.)
to the new offices on the other side, draping the wires across the light fixtures. Users working
out of the new offices in the addition complain of intermittent network connectivity. Which of
the following is MOST likely the cause of the connectivity issue?
A. dB loss
B. Distance
C. Incorrect connector type
D. EMI
E. Crosstalk

QUESTION NO: 795
A network administrator is getting reports of some internal users who cannot connect to
network resources. The users slate they were able to connect last week, but not today. No
changes have been configured on the network devices or server during the last few weeks.
Which of the following is the MOST likely cause of the issue?
A. The client DHCP scope is fully utilized
B. The wired network is experiencing electrical interference
C. The captive portal is down and needs to be restarted
D. SNMP traps are being received
E. The packet counter on the router interface is high.

QUESTION NO: 796
Which of the following is the NEXT step to perform network troubleshooting after identifying
an issue?
A. Implement a solution.
B. Establish a theory.
C. Escalate the issue.
D. Document the findings.

QUESTION NO: 797
A WAN technician reviews activity and identifies newly installed hardware that is causing
outages over an eight-hour period. Which of the following should be considered FIRST?
A. Network performance baselines
B. VLAN assignments
C. Routing table
D. Device configuration review

QUESTION NO: 798
Access to a datacenter should be individually recorded by a card reader even when multiple
employees enter the facility at the same time. Which of the following allows the enforcement
of this policy?
A. Motion detection
B. Access control vestibules
C. Smart lockers
D. Cameras

QUESTION NO: 799
SIMULATION

QUESTION NO: 800
A network resource was accessed by an outsider as a result of a successful phishing
campaign.
Which of the following strategies should be employed to mitigate the effects of phishing?
A. Multifactor authentication
B. Single sign-on
C. RADIUS
D. VPN
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Here are the answers to the questions:

QUESTION NO: 791
Answer: A. Dynamic ARP inspection
Explanation: Dynamic ARP inspection (DAI) is a security feature that validates ARP packets in a network to prevent ARP spoofing attacks, which are commonly used in on-path attacks.

QUESTION NO: 792
Answer: B. Change management
Explanation: Change management is a process used to review and manage changes to systems, including upgrades. By reviewing previous upgrades as part of change management procedures, organizations can ensure that upgrades are properly documented and evaluated for their impact on the system.

QUESTION NO: 793
Answer: B. 802.1X
Explanation: 802.1X is used to require network devices to authenticate before gaining access to a LAN. It provides port-based network access control, requiring users or devices to authenticate before being granted network access.

QUESTION NO: 794
Answer: D. EMI (Electromagnetic Interference)
Explanation: In this scenario, the network cables are draped across light fixtures in the gymnasium. This can cause electromagnetic interference (EMI), which can disrupt network connectivity, leading to intermittent issues.

QUESTION NO: 795
Answer: E. The packet counter on the router interface is high.
Explanation: A high packet counter on the router interface indicates that there may be network congestion or issues with packet transmission, which could result in some internal users being unable to connect to network resources.

QUESTION NO: 796
Answer: B. Establish a theory.
Explanation: After identifying an issue during network troubleshooting, the next step is to establish a theory or hypothesis about the root cause of the problem. This theory will guide further investigation and troubleshooting steps.

QUESTION NO: 797
Answer: D. Device configuration review
Explanation: In this scenario, where newly installed hardware is causing outages, the first step should be to review the configuration of the new hardware to ensure it is correctly configured and not causing any misconfigurations or conflicts in the network.

QUESTION NO: 798
Answer: B. Access control vestibules
Explanation: Access control vestibules are enclosed spaces with controlled entry and exit points, often used to enforce security policies such as individually recording access to a datacenter, even when multiple employees enter at the same time.

QUESTION NO: 800
Answer: A. Multifactor authentication
Explanation: Multifactor authentication adds an extra layer of security by requiring users to provide multiple forms of verification before gaining access to a network resource. This can help mitigate the effects of phishing by making it more difficult for attackers to gain unauthorized access even if they obtain a user's credentials through a phishing campaign.
''')
