print('''
QUESTION NO: 381
Which of the following describes when an active exploit is used to gain access to a network?
A. Penetration testing
B. Vulnerability testing
C. Risk assessment
D. Posture assessment
E. Baseline testing

QUESTION NO: 382
Which of the following policies would be best to refer to when trying to prevent a disgruntled
employee from copying sensitive materials off company servers after termination?
A. Incident response plan
B. Offboarding
C. Change management
D. Acceptable use

QUESTION NO: 383
A small office has a wireless network with several access points that are used by mobile
devices.
Users occasionally report that the wireless connection drops or becomes very slow. Reports
confirm that this only happens when the devices are connected to the office wireless network
.
Which of the following is MOST likely the cause?
A. The configuration of the encryption protocol
B. Interference from other devices
C. Insufficient bandwidth capacity
D. Duplicate SSIDs

QUESTION NO: 384
Users are reporting intermittent WiFi connectivity in specific parts of a building. Which of the
following should the network administrator check FIRST when troubleshooting this issue?
(Choose two.)
A. Site survey
B. EIRP
C. AP placement
D. Captive portal
E. SSID assignment
F. AP association time

QUESTION NO: 385
A desktop support department has observed slow wireless speeds for a new line of laptops
using the organization's standard image. No other devices have experienced the same issue.
Which of the following should the network administrator recommend troubleshooting FIRST
to resolve this issue?
A. Increasing wireless signal power
B. Installing a new WAP
C. Changing the protocol associated to the SSID
D. Updating the device wireless drivers

QUESTION NO: 386
Which of the following is used to provide networking capability for VMs at Layer 2 of the OSI
model?
A. VPN
B. VRRP
C. vSwitch
D. VIP

QUESTION NO: 387
A network administrator is configuring Neighbor Discovery Protocol in an IPv6 network to
ensure an attacker cannot spoof link-layer addresses of network devices. Which of the
following should the administrator implement?
A. MAC filtering
B. Router Advertisement Guard
C. Port security
D. DNSSEC

QUESTION NO: 388
Ann, a technician, installs a wireless router in a network closet in a large office. She then
configures all workstations in various offices on that floor to use the wireless connection.
Maximum connection speed at each workstation is 54 Mbps. Some users complain that their
network connection is very slow. Which of the following is MOST likely the problem?
A. Workstations were configured with the wrong connection speed on the wireless adapter.
B. Users with a slow connection are too far away from the wireless router.
C. Users that cannot connect are configured on the wrong channel.
D. Wireless network SSID is incorrect.

QUESTION NO: 389
A Chief Information Officer wants to monitor network breaching in a passive, controlled
manner.
Which of the following would be BEST to implement?
A. Honeypot
B. Perimeter network
C. Intrusion prevention system
D. Port security

QUESTION NO: 390
A user returns to the office after working remotely for an extended period. The user is
reporting limited access to the office wireless network and the inability to reach company
resources on the network. The user connected to the guest network, ensured all patches
were applied, and checked to make sure software was up to date. Which of the following is
most likely the cause of the issue?
A. The laptop drivers need to be updated to support a new wireless infrastructure.
B. The wireless passphrase has been cycled and needs to be updated.
C. The NAC appliance has labeled the laptop as non-complaint.
D. The WAP transmit power is too low and cannot complete user authentication.
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 381
Answer: A. Penetration testing
Explanation: Penetration testing involves actively exploiting vulnerabilities to gain access to a network. It is a controlled and authorized attempt to evaluate the security of the network by simulating real-world attack scenarios.

QUESTION NO: 382
Answer: B. Offboarding
Explanation: Offboarding policies typically include procedures for terminating access to company resources, such as revoking access to sensitive materials on company servers, when an employee leaves the organization.

QUESTION NO: 383
Answer: B. Interference from other devices
Explanation: Interference from other devices, such as neighboring wireless networks or electronic appliances operating on the same frequency, is a common cause of dropped or slow wireless connections.

QUESTION NO: 384
Answer: A. Site survey
          C. AP placement
Explanation: When troubleshooting intermittent WiFi connectivity issues, the network administrator should first conduct a site survey to assess the wireless coverage and placement of access points (APs) to ensure optimal signal strength and coverage throughout the building.

QUESTION NO: 385
Answer: D. Updating the device wireless drivers
Explanation: Slow wireless speeds on new laptops could be caused by outdated or incompatible wireless drivers. Updating the device's wireless drivers should be the first troubleshooting step to resolve this issue.

QUESTION NO: 386
Answer: C. vSwitch
Explanation: A vSwitch (virtual switch) is used to provide networking capability for virtual machines (VMs) at Layer 2 of the OSI model within a virtualized environment.

QUESTION NO: 387
Answer: B. Router Advertisement Guard
Explanation: Router Advertisement Guard is used in IPv6 networks to prevent an attacker from spoofing link-layer addresses of network devices, thus ensuring the integrity of Neighbor Discovery Protocol messages.

QUESTION NO: 388
Answer: B. Users with a slow connection are too far away from the wireless router.
Explanation: Slow network connection for users could be due to being too far away from the wireless router, resulting in weak signal strength and reduced data transmission rates.

QUESTION NO: 389
Answer: A. Honeypot
Explanation: A honeypot is a passive security mechanism used to monitor network breaching attempts in a controlled manner by luring attackers into a trap system designed to gather information about their tactics and techniques.

QUESTION NO: 390
Answer: C. The NAC appliance has labeled the laptop as non-compliant.
Explanation: The Network Access Control (NAC) appliance may have labeled the laptop as non-compliant, possibly due to outdated security settings or software configurations, restricting its access to the network resources.
''')
