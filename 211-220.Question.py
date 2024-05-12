print('''
Question NO:211
Which of the following is the MOST secure connection used to inspect and provide controlled
internet access when remote employees are connected to the corporate network?
 A. Site-to-site VPN
 B. Full-tunnel VPN
 C. Split-tunnel VPN
 D. SSH''')
print('''
Question NO:212
A network administrator requires redundant routers on the network, but only one default
gateway is configurable on a workstation. Which of the following will allow for redundant
routers with a single IP address?
 A. EIGRP
 B. VRRP
 C. MPLS
 D. STP ''')
print('''
Question NO:213
A network requirement calls for segmenting departments into different networks. The campus
network is set up with users of each department in multiple buildings. Which of the following
should be configured to keep the design simple and efficient?
 A. MDIX
 B. Jumbo frames
 C. Port tagging
 D. Flow control''')
print('''
Question NO:214
A network technician is installing new software on a Windows-based server in a different
geographical location. Which of the following would be BEST for the technician to use to
perform this task?
 A. RDP
 B. SSH
 C. FTP
 D. DNS

Question NO:215
A network engineer developed a plan of action to resolve an ongoing issue. Which of the
following steps should the engineer take NEXT?
 A. Verify full system functionality and implement preventative measures.
 B. Implement the solution to resolve the problem.
 C. Document findings, actions, outcomes, and lessons learned.
 D. Establish a theory of probable cause.

Question NO:216
A user cannot connect to the network, although others in the office are unaffected. The
network technician sees that the link lights on the NIC are not on. The technician needs to
check which switchport the user is connected to, but the cabling is not labeled. Which of the
following is the best way for the technician to find where the computer is connected?
 A. Look up the computer's IP address in the switch ARP table.
 B. Use a cable tester to trace the cable.
 C. Look up the computer's MAC address in the switch CAM table.
 D. Use a tone generator to trace the cable.

Question NO:217
A network technician was troubleshooting an issue for a user who was being directed to
cloned websites that were stealing credentials. The URLs were correct for the websites but
an incorrect IP address was revealed when the technician used ping on the user's PC. After
checking the is setting, the technician found the DNS server address was incorrect.
Which of the following describes the issue?
 A. Rogue DHCP server
 B. Misconfigured HSRP
 C. DNS poisoning
 D. Exhausted IP scope

Question NO:218
Which of the following security devices would be BEST to use to provide mechanical access
control to the MDF/IDF?
 A. A smart card
 B. A key fob
 C. An employee badge
 D. A door lock

Question NO:219
Which of the following attacks is typically used to guess a password?
 A. Brute-force
 B. DDoS
 C. DNS poisoning
 D. Rogue DHCP
 E. Ransomware

Question NO:220
A newly installed VoIP phone is not getting the DHCP IP address it needs to connect to the
phone system. Which of the following tasks needs to be completed to allow the phone to
operate correctly?
 A. Assign the phone's switchport to the correct VLAN
 B. Statically assign the phone's gateway address.
 C. Configure a route on the VoIP network router.
 D. Implement a VoIP gateway''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Question NO: 211 = B
Explanation: The MOST secure connection used to inspect and provide controlled internet access when remote employees are connected to the corporate network is a "Full-tunnel VPN." In a full-tunnel VPN setup, all traffic from the remote employee's device is routed through the VPN tunnel to the corporate network, where it can be inspected and controlled.

Question NO: 212 = B
Explanation: To achieve redundant routers with a single IP address, the network administrator should use "VRRP" (Virtual Router Redundancy Protocol). VRRP allows multiple routers to work together in a group, presenting a virtual IP address that can be used as the default gateway. If one router fails, another router in the group takes over seamlessly.

Question NO: 213 = C
Explanation: To segment departments into different networks efficiently in a campus network setup with users in multiple buildings, "Port tagging" should be configured. Port tagging, also known as VLAN tagging, allows network administrators to assign VLAN IDs to switch ports, segregating network traffic based on departmental requirements while maintaining simplicity and efficiency in network design.

Question NO: 214 = A
Explanation: The BEST option for a network technician to use to install new software on a Windows-based server in a different geographical location is "RDP" (Remote Desktop Protocol). RDP allows remote access to the server's desktop environment, enabling the technician to install software and perform other administrative tasks as if physically present at the server.

Question NO: 215 = D
Explanation: After developing a plan of action to resolve an ongoing issue, the NEXT step for the network engineer should be to "Establish a theory of probable cause." This involves analyzing the available information to determine the most likely cause of the problem before proceeding with the implementation of the solution.

Question NO: 216 = C
Explanation: The best way for the technician to find where the computer is connected when the cabling is not labeled is to "Look up the computer's MAC address in the switch CAM table." The CAM table (Content Addressable Memory table) in the switch contains information about MAC addresses and their associated switch ports, allowing the technician to identify the switchport to which the computer is connected.

Question NO: 217 = C
Explanation: The issue described, where a user is directed to cloned websites that steal credentials and the incorrect IP address is revealed when using ping due to a misconfigured DNS server, is known as "DNS poisoning." In DNS poisoning attacks, incorrect DNS entries are added to DNS caches, redirecting users to malicious websites.

Question NO: 218 = A
Explanation: The BEST security device to provide mechanical access control to the MDF/IDF (Main Distribution Frame/Intermediate Distribution Frame) is "A smart card." Smart cards can be used to authenticate users and provide access to restricted areas based on their access permissions.

Question NO: 219 = A
Explanation: The attack typically used to guess a password is "Brute-force." In a brute-force attack, an attacker systematically tries all possible combinations of characters until the correct password is discovered.

Question NO: 220 = A
Explanation: To allow the newly installed VoIP phone to operate correctly by getting the DHCP IP address it needs to connect to the phone system, the task that needs to be completed is to "Assign the phone's switchport to the correct VLAN." VoIP phones often require specific VLAN assignments to ensure proper network connectivity and communication with the VoIP system.
''')
