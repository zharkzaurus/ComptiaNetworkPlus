print("Question NO:171\nA network technician recently replaced a managed switch in an enterprise network with a new managed switch. Users on the switch can communicate with each other but now cannot access other network segments. Which of the following is the MOST likely reason that the users are unable to access any network segments?\n A.The newly installed swtich is defective and must be returned\n B.The newly installed is using a different MAC address than the previous switch\n C.The technician forgot to change the VTP mode on the new switch to the new server\n D.The technician did not use the correct cable when trunking the new switch")
print("\nQuestion NO:172\nA branch of a company recently switched to a new ISP. The network engineer was given a new IP range to assign. The ISP assigned 196.26.4.0/26, and the branch gateway router now has the following configurations on the interface that peers to the ISP\n IP address:  196.26.4.30\n Subnet mask:  255.255.255.224\n Gateway: 196.24.4.1\nThe network engineer observes that all users have lost internet connectivity. Which of the following describes the issue?\n A.The incorrect subnet mask was configured\n B.The incorrect gateway was configured\n C.The incorrect IP address was configures\n D.The incorrect interface was configured")
print("\nQuestion NO:173\nWhich of the following can be used to identify users after an action has occurred?\n A.Access control vestibule\n B.Cameras\n C.Asset tag\n D.Motion detectors")
print("\nQuestion NO:174\nA city has hired a new employee who needs to be able to work when traveling at home and at the municipal sourcing of a neighboring city that snares services. The employee is issued a laptop, and a technician needs to train the employee on the appropiate solutions for secure access to the network from all the possible locations On which of the following solutions would the technician MOST likely train the employee?\n A.Site-to-site VPNs between the two city locations and client-to-site software on the employee's laptop for all other remote access\n B.Client-to-site VPNs between the travel locations and site-to-site software on the employee's laptop for all other remote access\n C.Client-to-site VPNs between the two city locations and site-to-site software on the employee's laptop for all other remote access\n D.Site-to-site VPNs between the home and city locations and site-to-site software on the employee's laptop for all other remote access")
print("\nQuestion NO:175\nA network team is getting reports that air conditioning is out in an IDF. The team would like to determine whether additional network issues are occuring. Which of the following should the network team do?\n A.Confirm that memory usage on the network devices in the IDF is normal\nB.Access network baseline data for references to an air conditioning issue\n C.Verify serverity levels on the corporate syslog server\n D.Check for SNMP traps from a network device in the IDF\n E.Review interface statistics looking for cyclic redundancy errors")
print("\nQuestion NO:176\nDHCP uses which of the following ports by default?\n A.21\n B.23\n C.68\n D.443")
print("\nQuestion NO:177\nWhich of the following routing technologies uses a succesor and a feasible successor?\n A.IS-IS\n B.OSPF\n C.BGP\n D.EIGRP")
print("\nQuestion NO:178\nWhich of the following should be used to manage outside cables that need to be routed to various multimode uplinks?\n A.Fiber distribution panel\n B.110 punchdown block\n C.PDU\n D.TIA/EIA-568A patch bay\n E.Cat 6 patch panel")
print("\nQuestion NO:179\nA network administrator is implementing OSPF on all of a company's network devices. Which of the following will MOST likely replace all the company's hubs?\n A Layer 3 switch\n B.A proxy server\n C.A NGFW\n D.A WLAN controller")
print("\nQuestion NO:180\nA network administrator needs to configure a server to use the most accurate NTP reference available. Which of the following NTP Devices should the administrator select?\n A.Stratum 1\n B.Stratum 2\n C.Stratum 3\n D.Stratum 4")
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''NO:171 = C.The technician forgot to change the VTP mode on the new switch to server\n Explanation: VTP is responsible for managing VLAN configurations across a network. If the VTP mode on the new switch is not set to "server," it will not propagate VLAN information to other switches in the network, leading to connectivity issues between different network segments.''')
    print("NO:172 = C.The incorrect IP address was configured\n Explanation: ensuring the correct configuration of the default gateway is crucial for maintaining smooth and reliable network connectivity.")
    print("NO:173 = B.Cameras\n Explanation: Cameras can capture images or footage of individuals performing actions or activities, allowing for retrospective identification of users or individuals involved in particular actions.")
    print("NO:174 = C.Client-to-site VPNs between the two city locations and site-to-site software on the employee's laptop for all other remote access\n Explanation: This setup provides flexibility and security for the employee to work remotely from various locations while ensuring secure access to the city network.")
    print("NO:175 = B.Access network baseline data for references to an air conditioned issue\n Explantion: Accessing network baseline data allows the team to compare current network conditions with historical records, helping to identify any deviations related to the reported air conditioning issue.")
    print("NO:176 = C.68\n Explanation: DHCP Server uses the UDP port 67 and DHCP client uses UDP port 68.")
    print("NO:177 = D.EIGRP\n Explanation: EIGRP(Enhanced Interior Gateway Routing Protocol) is capable of having backup routes ready to install in the routing table if the primary route fails.")
    print("NO:178 = A.Fiber distribution panel\n Explanation: Fiber distribution panels are designed to manage and organize fiber optic cables. They typically include features such as cable management, termination points for incoming and outgoing cables, and adapters for connecting various fiber optic cables.")
    print("NO:179 = A.A Layer 3 switch\n Explanation: Layer 3 switches offer routing capabilities at the network layer (Layer 3) of the OSI model, similar to routers, while also providing the high port density and switching capabilities of traditional Layer 2 switches. When implementing OSPF, which is a dynamic routing protocol, a Layer 3 switch can replace hubs to provide both switching and routing functions, allowing for more efficient and scalable network communication.")
    print("NO:180 = A.Stratum 1\n Explanation: Stratum 1 devices are directly connected to a reliable time source, such as an atomic clock or GPS receiver.")
