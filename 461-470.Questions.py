print('''
QUESTION NO: 461
A help desk technician is troubleshooting a Windows server named SQL.local and wants to
check which port a specific application is running on. Which of the following commands
should the technician run?
A. dig
B. traceroute
C. arp
D. netstat

QUESTION NO: 462
Which of the following is an IPv6 transition mechanism in which network devices utilize IPv4
and IPv6 at the same time?
A. 6to4
B. ISATAP
C. Teredo
D. Dual stack

QUESTION NO: 463
An IT organization needs to optimize speeds for global content distribution and wants to
reduce latency in high-density user locations. Which of the following technologies BEST
meets the organization's requirements?
A. Load balancing
B. Geofencing
C. Public cloud
D. Content delivery network
E. Infrastructure as a service

QUESTION NO: 464
A new office space is being designed. The network switches are up, but no services are
running yet. A network engineer plugs in a laptop configured as a DHCP client to a switch.
Which of the following IP addresses should be assigned to the laptop?
A. 10.1.1.1
B. 169.254.1.128
C. 172.16.128.128
D. 192.168.0.1

QUESTION NO: 465
Which of the following STP states indicates an inactivated port due to a loop?
A. Disabled
B. Learning
C. Blocking
D. Forwarding

QUESTION NO: 466
Users have reported an issue connecting to a server over the network. A workstation was
recently added to the network and configured with a shared USB printer. Which of the
following is most likely causing the issue?
A. The switch is oversubscribed and cannot handle the additional throughput.
B. The printer is tying up the server with DHCP discover messages.
C. The web server's back end was designed for only single-threaded applications.
D. The workstation was configured with a static IP that is the same as the server.

QUESTION NO: 467
A network administrator is implementing process changes based on recommendations
following a recent penetration test. The testers used a method to gain access to the network
that involved exploiting a publicly available and fixed remote code execution vulnerability in
the VPN appliance.
Which of the following should the administrator do to BEST prevent this from happening
again?
A. Change default passwords on internet-facing hardware.
B. Implement robust ACLs with explicit deny-all entries.
C. Create private VLANs for management plane traffic.
D. Routinely upgrade all network equipment firmware.

QUESTION NO: 468
A technician is configuring a wireless access point in a public space for guests to use. Which
of the following should the technician configure so that only approved connections are
allowed?
A. Geofencing
B. Captive portal
C. Secure SNMP
D. Private VLANs

QUESTION NO: 469
Which of the following firewall rules will block destination telnet traffic to any host with the
source IP address 1.1.1.2/24?
A. Deny any source host on source port 23 to destination any
B. Deny any source network 1.1.1.0/24 to destination any on port 23
C. Deny source host 1.1.12 on source port 23 to destination any
D. Deny any source network 1.1.1.0/24 with source port 23 to destination any

QUESTION NO: 470
A customer wants to segregate the traffic between guests on a hypervisor. Which of the
following does a technician need to configure to meet the requirement?
A. Virtual switches
B. OSPF routing
C. Load balancers
D. NIC teaming
E. Fibre Channel
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 461
Answer: D
Explanation: The command the technician should run to check which port a specific application is running on is `netstat`. The `netstat` command displays active network connections, routing tables, and a variety of network interface statistics. By using the appropriate options with `netstat`, such as `-a` (to display all connections and listening ports), the technician can identify the port on which the application associated with the server named SQL.local is running.

NO: 462
Answer: D
Explanation: The IPv6 transition mechanism in which network devices utilize IPv4 and IPv6 at the same time is called "Dual stack." With Dual stack, devices are configured to support both IPv4 and IPv6 protocols simultaneously. This allows for a gradual transition from IPv4 to IPv6 without requiring immediate abandonment of IPv4 infrastructure.

NO: 463
Answer: D
Explanation: The technology that best meets the organization's requirements for optimizing speeds for global content distribution and reducing latency in high-density user locations is a "Content Delivery Network" (CDN). A CDN consists of a network of distributed servers strategically deployed in multiple data centers across various geographical locations. These servers cache and deliver web content to users based on their geographic proximity, thereby reducing latency and optimizing content delivery speeds.

NO: 464
Answer: B
Explanation: When a DHCP server is not available, devices often assign themselves an IP address from the Automatic Private IP Addressing (APIPA) range, which is 169.254.0.0 to 169.254.255.255. Therefore, in this scenario, the laptop plugged into the switch without DHCP services running should be assigned an IP address from the APIPA range. Option B, 169.254.1.128, falls within this range and would be a valid IP address for the laptop in this situation.

NO: 465
Answer: C
Explanation: The STP (Spanning Tree Protocol) state that indicates an inactivated port due to a loop is "Blocking." In STP, ports go through several states, including Blocking, Listening, Learning, and Forwarding, to prevent loops in the network topology. When a port is in the Blocking state, it does not forward data frames but listens to BPDU (Bridge Protocol Data Unit) messages to determine the topology of the network and prevent loops.

NO: 466
Answer: D
Explanation: The most likely cause of the issue connecting to the server over the network is that the workstation was configured with a static IP address that conflicts with the IP address of the server. This conflict can cause network connectivity issues, as both devices are using the same IP address. To resolve the issue, the static IP configuration of the workstation should be modified to use a unique IP address that does not conflict with other devices on the network.

NO: 467
Answer: D
Explanation: To best prevent a reoccurrence of the penetration test scenario involving a publicly available and fixed remote code execution vulnerability in the VPN appliance, the administrator should routinely upgrade all network equipment firmware. Regular firmware updates ensure that known vulnerabilities are patched and security flaws are addressed, reducing the risk of exploitation by attackers.

NO: 468
Answer: B
Explanation: To ensure that only approved connections are allowed on a wireless access point in a public space, the technician should configure a "Captive portal." A captive portal is a web page that users must interact with before being granted access to the network. It typically requires users to authenticate or agree to terms of service before gaining network access, thereby controlling and restricting unauthorized access to the network.

NO: 469
Answer: B
Explanation: The firewall rule that will block destination telnet traffic to any host with the source IP address 1.1.1.2/24 is "Deny any source network 1.1.1.0/24 to destination any on port 23." This rule explicitly denies traffic from the specified source network (1.1.1.0/24) to any destination on port 23 (telnet). By denying telnet traffic from the specified source network, the firewall effectively blocks telnet connections originating from that network.

NO: 470
Answer: A
Explanation: To segregate traffic between guests on a hypervisor, a technician needs to configure "Virtual switches." Virtual switches allow for the creation of separate network segments within the hypervisor environment, enabling traffic isolation and segmentation. Each virtual switch can be configured with its own network policies, VLANs, and security settings to ensure guest traffic separation and network segmentation.
''')
