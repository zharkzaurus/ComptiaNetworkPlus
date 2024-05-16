print('''
QUESTION NO: 771
A user in a branch office reports that access to all files has been lost after receiving a new
PC. All other users in the branch can access fileshares. The IT engineer who is
troubleshooting this incident is able to ping the workstation from the branch router, but the
machine cannot, ping the router. Which of the following is MOST likely the cause of the
incident?
A. Incorrect subnet mask
B. Incorrect DNS server
C. Incorrect IP class
D. Incorrect TCP port

QUESTION NO: 772
An administrator is troubleshooting analog telephony issues on the punch down block. Which
of the following tools would be MOST useful in this scenario?
A. T1 loopback
B. Butt set
C. Multimeter
D. Protocol analyzer

QUESTION NO: 773
A user at a hotel sees two SSIDs; both are called "HotelWireless". After the PC connects to
one of the APs, the user notices their browser homepage has been changed. Which of the
following BEST describes this AP?
A. Man-in-the-middle
B. DDoS
C. Evil twin
D. War driving

QUESTION NO: 774
The results of a recently completed site survey indicate a significant, undesired RSSI in the
parking lot and other exterior areas near the main building. The wireless technician would like
to mitigate access to the wireless network in exterior access areas. The current access point
settings are listed in the following table:
 | Name | Power  | Antenna type    | Channel | SSID   | Passphrase |
 | AP1  | High   | Omnidirectional | 1       | Corp01 | P$ssw0rd   |
 | AP2  | Medium | Omnidirectional | 6       | Corp01 | P$ssw0rd   |
 | AP1  | Medium | Directional     | 9       | Corp01 | P$ssw0rd   |

Which of the following is the BEST step for the technician to take to resolve the issue?
A. Reconfigure AP2 and AP3 for non-overlapping channels.
B. Implement directional antennas on AP1 and AP2.
C. Raise the power settings on AP2 and AP3.
D. Change the SSID on AP1 and AP2.

QUESTION NO: 775
A technician is troubleshooting a network switch that seems to stop responding to requests
intermittently whenever the logging level is set for debugging. Which of the following metrics
should the technician check to begin troubleshooting the issue?
A. Audit logs
B. CPU utilization
C. CRC errors
D. Jitter

QUESTION NO: 776
A technician is checking network devices to look for opportunities to improve security. Which
of the following tools would BEST accomplish this task?
A. Wi-Fi analyzer
B. Protocol analyzer
C. Nmap
D. IP scanner

QUESTION NO: 777
A security team would like to use a system in an isolated network to record the actions of
potential attackers. Which of the following solutions is the security team implementing?
A. Perimeter network
B. Honeypot
C. Zero trust infrastructure
D. Network segmentation

QUESTION NO: 778
Switch 3 was recently added to an existing stack to extend connectivity to various parts of the
network. After the update, new employees were not able to print to the main networked
copiers from their workstations. Following are the port configurations for the switch stack in
question:
Switch 1:
 |             | Port 1-12    | Ports 13-24 | Ports 25-36  | Ports 37-44  | Ports 45-48 |
 | Description | Workstations | Printers    | Workstations | Wireless APs | Uplink      |
 | VLAN        | 20           | 60          | 20           | 80           | 20/60/80    |
 | Duplex      | Full         | Full        | Full         | Full         | Full        |
 | Status      | Active       | Active      | Active       | Active       | Active      |
Switch 2:
 |             | Port 1-12    | Ports 13-24 | Ports 25-36  | Ports 37-44  | Ports 45-48 |
 | Description | Workstations | Printers    | Workstations | Wireless APs | Uplink      |
 | VLAN        | 20           | 60          | 20           | 80           | 20/60/80    |
 | Duplex      | Full         | Full        | Full         | Full         | Full        |
 | Status      | Active       | Active      | Shut down    | Active       | Active      |

Switch 3:
 |             | Port 1-12    | Ports 13-24 | Ports 25-36  | Ports 37-44  | Ports 45-48 |
 | Description | Workstations | Printers    | Workstations | Wireless APs | Uplink      |
 | VLAN        | 20           | 60          | 20           | 80           | 20/60/80    |
 | Duplex      | Full         | Full        | Full         | Full         | Full        |
 | Status      | Active       | Shut down   | Shut down    | Shut down    | Active      |
Which of the following should be configured to resolve the issue? (Choose two.)
A. Enable the printer ports on Switch 3.
B. Reconfigure the duplex settings on the printer ports on Switch 3.
C. Reconfigure the VLAN on an printer ports to VLAN 20.
D. Enable all ports that are shut down on the stack.
E. Reconfigure the VLAN on the printer ports on Switch 3.
F. Enable wireless APs on Switch 3.

QUESTION NO: 779
In a small office environment, one computer is set up to provide Internet access to three
other computers that are not interconnected. This is an example of which of the following
topology types?
A. Peer-to-peer
B. Point-to-multipoint
C. Hybrid
D. Point-to-point

QUESTION NO: 780
A workstation is configured with the following network details:
 | IP address | Subnet mask | Defalut gateway |
 |10.1.2.23   | 10.1.2.0/27 | 10.1.2.1        |
Software on the workstation needs to send a query to the local subnet broadcast address. To
which of the following addresses should the software be configured to send the query?
A. 10.1.2.0
B. 10.1.2.1
C. 10.1.2.23
D. 10.1.2.255
E. 10.1.2.31
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 771
Answer: A. Incorrect subnet mask
Explanation: The user's inability to ping the router from the workstation, despite being able to ping the workstation from the router, suggests a network configuration issue. The most likely cause is an incorrect subnet mask on the workstation, which prevents it from communicating properly within the network.

QUESTION NO: 772
Answer: B. Butt set
Explanation: A butt set is a telecommunications tool used by technicians to troubleshoot analog telephone lines, including issues related to punch-down blocks.

QUESTION NO: 773
Answer: C. Evil twin
Explanation: An Evil Twin AP is a rogue wireless access point that mimics a legitimate access point, often to conduct man-in-the-middle attacks or gather sensitive information from unsuspecting users who connect to it.

QUESTION NO: 774
Answer: B. Implement directional antennas on AP1 and AP2.
Explanation: To mitigate access to the wireless network in exterior access areas, the technician should implement directional antennas on AP1 and AP2 to focus the Wi-Fi signal towards the intended coverage area and reduce signal leakage into undesired areas.

QUESTION NO: 775
Answer: B. CPU utilization
Explanation: Intermittent unresponsiveness of a network switch when the logging level is set for debugging suggests that the switch's CPU might be overwhelmed by the increased processing required for logging. Checking the CPU utilization metric can confirm if this is the case.

QUESTION NO: 776
Answer: C. Nmap
Explanation: Nmap is a network scanning tool that can be used to discover network devices and identify potential security vulnerabilities. It can help identify open ports, services running on devices, and potential security risks.

QUESTION NO: 777
Answer: B. Honeypot
Explanation: A honeypot is a security mechanism designed to lure potential attackers into interacting with a simulated system or network, allowing security teams to monitor and analyze their activities for defensive purposes.

QUESTION NO: 778
Answers: A. Enable the printer ports on Switch 3.
             E. Reconfigure the VLAN on the printer ports on Switch 3.
Explanation: To resolve the issue, the technician should enable the printer ports on Switch 3 (which are currently shut down) and ensure that the VLAN configuration on the printer ports matches the VLAN configuration on Switches 1 and 2.

QUESTION NO: 779
Answer: A. Peer-to-peer
Explanation: In a peer-to-peer network topology, devices communicate directly with each other without the need for a central server. In this scenario, one computer provides Internet access to three other computers without them being interconnected, making it a peer-to-peer setup.

QUESTION NO: 780
Answer: D. 10.1.2.255
Explanation: The broadcast address for the subnet 10.1.2.0/27 is 10.1.2.255. Broadcasting a query to this address will reach all devices within the subnet.
''')
