print('''
QUESTION NO: 641
A trusted vendor emailed a security advisory to an engineer. The advisory listed publicly
disclosed security issues and resolutions for the vendor's installed network devices. Which of
the following describes this security concept?
A. CVE
B. Exploits
C. Zero day
D. SSO

QUESTION NO: 642
A new cabling certification is being requested every time a network technician rebuilds one
end of a Cat 6 (vendor-certified) cable to create a crossover connection that is used to
connect switches.
Which of the following would address this issue by allowing the use of the original cable?
A. CSMA/CD
B. LACP
C. PoE+
D. MDIX

QUESTION NO: 643
A network technician is working to upgrade an existing wireless system in order to improve
the coverage of APs throughout the building. Which of the following should the technician
perform to determine the optimal placement of APs for the new wireless system?
A. Cable testing
B. Network assessment
C. Site survey
D. Packet capture

QUESTION NO: 644
An administrator is investigating reports of network slowness in a building. While looking at
the uplink interface statistics in the switch's CLI, the administrator discovers the uplink is at
100% utilization. However, the administrator is unsure how to identify what traffic is causing
the saturation. Which of the following tools should the administrator utilize to identify the
source and destination addresses of the traffic?
A. SNMP
B. Traps
C. Syslog
D. NetFlow

QUESTION NO: 645
In which of the following locations is a VPN headend found?
A. Distribution
B. Access
C. Core
D. WAN edge

QUESTION NO: 646
A network technician added a new workstation to the network and needs to make a custom,
shielded cable that is 492ft (150m) with both ends wired to TIA/EIA-568A standards. The
workstation is not establishing a link to the switchport. Which of the following is the cause of
the issue?
A. Cable shielding
B. Attenuation
C. Incorrect pinout
D. Near-end crosstalk

QUESTION NO: 647
A company needs a redundant link to provide a channel to the management network in an
incident response scenario. Which of the following remote access methods provides the
BEST solution?
A. Out-of-band access
B. Split-tunnel connections
C. Virtual network computing
D. Remote desktop gateways

QUESTION NO: 648
A network technician is troubleshooting an application issue. The technician is able to
recreate the issue in a virtual environment. According to the troubleshooting methodology,
which of the following actions will the technician most likely perform NEXT?
A. Gather information from the initial report.
B. Escalate the issue to a supervisor.
C. Implement a solution to resolve the issue.
D. Establish a theory of probable cause.

QUESTION NO: 649
Which of the following devices would be used to extend the range of a wireless network?
A. A repeater
B. A media converter
C. A router
D. A switch

QUESTION NO: 650
Which of the following policies should be referenced when a user wants to access work email
on a personal cell phone?
A. Offboarding policy
B. Acceptable use policy
C. BYOD policy
D. Remote access policy
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 641
Answer: A. CVE
Explanation: The security concept described in the scenario is related to a Common Vulnerabilities and Exposures (CVE) advisory. CVEs are standardized identifiers for publicly known cybersecurity vulnerabilities, allowing organizations to reference and address specific security issues affecting their network devices or software.

QUESTION NO: 642
Answer: D. MDIX
Explanation: To address the issue of needing a new cabling certification every time a crossover connection is created using a Cat 6 cable, the technician should utilize MDIX (Medium Dependent Interface Crossover). MDIX is a feature found in many modern network devices, including switches, which automatically detects the cable type (straight-through or crossover) and configures the port accordingly, eliminating the need for manually creating crossover connections.

QUESTION NO: 643
Answer: C. Site survey
Explanation: To determine the optimal placement of APs (Access Points) for the new wireless system and improve coverage throughout the building, the technician should perform a site survey. A site survey involves physically walking through the building to assess signal strength, interference, and other factors that may affect wireless coverage, helping to identify the best locations for installing APs.

QUESTION NO: 644
Answer: D. NetFlow
Explanation: To identify the source and destination addresses of the traffic causing network saturation, the administrator should utilize NetFlow. NetFlow is a network protocol that collects and analyzes information about IP traffic flows traversing a network device, such as a router or switch. It provides detailed visibility into traffic patterns, including source and destination IP addresses, port numbers, and protocols, helping administrators identify and troubleshoot network issues.

QUESTION NO: 645
Answer: D. WAN edge
Explanation: A VPN (Virtual Private Network) headend is typically found at the WAN (Wide Area Network) edge. The VPN headend is the termination point for VPN connections, where encrypted tunnels are established and terminated, allowing remote users or branch offices to securely connect to the corporate network over the internet.

QUESTION NO: 646
Answer: B. Attenuation
Explanation: The cause of the workstation not establishing a link to the switchport in this scenario is likely attenuation. Attenuation refers to the loss of signal strength as it travels through a medium, such as a copper cable. In this case, the length of the cable (492ft/150m) may exceed the maximum allowable length for Ethernet communication without signal degradation, resulting in attenuation and the inability to establish a link.

QUESTION NO: 647
Answer: A. Out-of-band access
Explanation: Out-of-band access provides a redundant link to the management network in an incident response scenario. It allows administrators to remotely access and manage network devices using a separate, dedicated network path that is independent of the primary data network. Out-of-band access ensures continued connectivity and management capabilities, even if the primary network is compromised or unavailable.

QUESTION NO: 648
Answer: D. Establish a theory of probable cause.
Explanation: According to the troubleshooting methodology, the technician, after recreating the issue in a virtual environment, would likely establish a theory of probable cause next. This involves analyzing the gathered information, test results, and symptoms to formulate a hypothesis about the root cause of the issue before proceeding with further troubleshooting steps.

QUESTION NO: 649
Answer: A. A repeater
Explanation: A repeater is used to extend the range of a wireless network by receiving and retransmitting wireless signals, effectively amplifying the signal and extending coverage. Repeaters are commonly used in environments where the wireless signal strength is weakened over long distances or due to obstacles such as walls or interference.

QUESTION NO: 650
Answer: C. BYOD policy
Explanation: When a user wants to access work email on a personal cell phone, the policy that should be referenced is the BYOD (Bring Your Own Device) policy. BYOD policies define the rules, procedures, and security requirements for employees who use their personal devices, such as smartphones or tablets, to access corporate resources and data.
''')
