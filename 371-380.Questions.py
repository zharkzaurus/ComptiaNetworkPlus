print('''
QUESTION NO: 371
A network administrator is setting up several loT devices on a new VLAN and wants to
accomplish the following:
1. Reduce manual configuration on each system
2. Assign a specific IP address to each system
3. Allow devices to move to different switchports on the same VLAN
Which of the following should the network administrator do to accomplish these
requirements?
A. Set up a reservation for each device
B. Configure a static IP on each device
C. Implement private VLANs for each device
D. Use DHCP exclusions to address each device

QUESTION NO: 372
Which of the following tools can the technician use to analyze TCP/IP packets when trying to
determine a connection problem within a subnet?
A. Wire mapper
B. Protocol analyzer
C. Cable tester
D. SYSLOG server

QUESTION NO: 373
A user is unable to reach any resources on the internet. A technician goes to the site and
obtains the following output from the workstation:
 Network
 Destination        Netmask            Gateway   Interface       Metric
 10.10.51.0         255.255.255.0      On-link   10.10.51.147    291
 10.10.51.147       255.255.255.255    On-link   10.10.51.147    291
 10.10.51.255       255.255.255.255    On-link   10.10.51.147    297
 127.0.0.0          255.0.0.0          On-link   127.0.0.1       331
 127.0.0.1          255.255.255.255    On-link   127.0.0.1       331
 127.255.255.255    255.255.255.255    On-link   127.0.0.1       331
 224.0.0.0          240.0.0.0          On-link   127.0.0.1       331
 224.0.0.0          240.0.0.0          On-link   10.10.51.147    291
 255.255.255.255    255.255.255.255    On-link   127.0.0.1       331
 255.255.255.255    255.255.255.255    On-link   10.10.51.147    291
Which of the following commands should the technician use to correct the issue?
A. route ADD 0.0.0.0 MASK 0.0.0.0 10.10.51.10 metric 35
B. route CHANGE 10.10.51.0 MASK 255.255.255.255 10.10.52.1 metric 5
C. route CHANGE 10.10.51.255 MASK 255.0.0.0 On-Link metric 1
D. route DELETE 127.255.255.255

QUESTION NO: 374
A technician needs to configure a Linux computer for network monitoring. The technician has
the following information:
Linux computer details:
| Interface | IP address | MAC address       |
| eth0      | 10.1.2.24  | A1:B2:C3:F4:E5:D6 |
Switch mirror port details:
| Interface | IP address | MAC address       |
| eth1      | 10.1.2.3   | A1:B2:C3:D4:E5:F6 |
After connecting the Linux computer to the mirror port on the switch, which of the following
commands should the technician run on the Linux computer?
A. ifconfig ecth0 promisc
B. ifconfig eth1 up
C. ifconfig eth0 10.1.2.3
D. ifconfig eth1 hw ether A1:B2:C3:D4:E5:F6

QUESTION NO: 375
After running a Cat 8 cable using passthrough plugs, an electrician notices that connected
cables are experiencing a lot of cross talk. Which of the following troubleshooting steps
should the electrician take first?
A. Inspect the connectors for any wires that are touching or exposed.
B. Restore default settings on the connected devices.
C. Terminate the connections again.
D. Check for radio frequency interference in the area.

QUESTION NO: 376
Users are reporting issues with connecting to the wireless router. The technician discovers
neighboring wireless APs that are not part of the network are on the same 5GHz frequency.
Which of the following best describes the issue?
A. Distance limitation
B. Absorption
C. Signal-to-noise ratio
D. Interference

QUESTION NO: 377
A user stores large graphic files. The time required to transfer the files to the server is
excessive due to network congestion. The user's budget does not allow for the current
switches to be replaced. Which of the following can be used to provide FASTER transfer
times?
A. Half duplex
B. Jumbo frames
C. LACP
D. 802.1Q

QUESTION NO: 378
A network administrator is given the network 80.87.78.0/26 for specific device assignments.
Which of the following describes this network?
A. 80.87.78.0 - 80.87.78.14
B. 80.87.78.0 - 80.87.78.110
C. 80.87.78.1 - 80.87.78.62
D. 80.87.78.1 - 80.87.78.158

QUESTION NO: 379
A network administrator is downloading a large patch that will be uploaded to several
enterprise switches simultaneously during the day's upgrade cycle. Which of the following
should the administrator do to help ensure the upgrade process will be less likely to cause
problems with the switches?
A. Confirm the patch's MD5 hash prior to the upgrade
B. Schedule the switches to reboot after an appropriate amount of time.
C. Download each switch's current configuration before the upgrade
D. Utilize FTP rather than TFTP to upload the patch

QUESTION NO: 380
A network technician is installing an analog desk phone for a new receptionist.
After running a new phone line, the technician now needs to crimp on a new connector.
Which of the following connectors would MOST likely be used in this case?
A. DB9
B. RJ11
C. RJ45
D. DB25
''')
answer = input(print("Do you answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 371
Answer: A. Set up a reservation for each device
Explanation: Setting up DHCP reservations for each IoT device allows the network administrator to achieve the specified requirements. DHCP reservations reduce manual configuration, assign specific IP addresses to devices, and allow devices to move within the same VLAN without requiring reconfiguration.

QUESTION NO: 372
Answer: B. Protocol analyzer
Explanation: A protocol analyzer, also known as a network analyzer or packet sniffer, is the appropriate tool for analyzing TCP/IP packets when troubleshooting connection problems within a subnet.

QUESTION NO: 373
Answer: A. route ADD 0.0.0.0 MASK 0.0.0.0 10.10.51.10 metric 35
Explanation: The command "route ADD 0.0.0.0 MASK 0.0.0.0 10.10.51.10 metric 35" adds a default route (0.0.0.0/0) to the workstation's routing table, specifying the correct gateway (10.10.51.10) for internet access.

QUESTION NO: 374
Answer: B. ifconfig eth1 up
Explanation: The command "ifconfig eth1 up" brings up the eth1 interface on the Linux computer, enabling it to receive mirrored traffic from the switch's mirror port for network monitoring.

QUESTION NO: 375
Answer: A. Inspect the connectors for any wires that are touching or exposed.
Explanation: Cross talk in a cable installation can often be caused by wires touching or exposed within the connectors. Inspecting and ensuring proper termination of the connectors should be the first troubleshooting step.

QUESTION NO: 376
Answer: D. Interference
Explanation: The presence of neighboring wireless APs on the same 5GHz frequency can cause interference, leading to connectivity issues with the wireless router.

QUESTION NO: 377
Answer: B. Jumbo frames
Explanation: Jumbo frames can be used to provide faster transfer times for large files by increasing the Maximum Transmission Unit (MTU) size, reducing the overhead associated with transferring data over the network.

QUESTION NO: 378
Answer: C. 80.87.78.1 - 80.87.78.62
Explanation: The network 80.87.78.0/26 includes IP addresses from 80.87.78.1 to 80.87.78.62, providing a total of 62 assignable host addresses within the given subnet.

QUESTION NO: 379
Answer: C. Download each switch's current configuration before the upgrade
Explanation: Downloading each switch's current configuration before the upgrade allows the network administrator to have a backup in case of any issues during the upgrade process.

QUESTION NO: 380
Answer: B. RJ11
Explanation: RJ11 connectors are commonly used for analog phone lines, making them the most likely choice for crimping on a new connector for the analog desk phone.
''')
