print("Question NO:141\nA technician is connecting DSL for a new costumer. After installing and connecting the onpremises equipment, the technician verifies DSL synchronization. When connecting to a workstation, however, the link LEDs on the workstation and modem do not light up. Which of the following should the technician perform during troubleshooting?\n A.Identify the switch loops between the modem and the workstation\n B.Check for asymmetrical routing on the modem\n C.Look for a rogue DHCP server on the modem\n D.Replace the cable connecting the modem and the workstation")
print("\nQuestion NO:142\nWhich of the following antenna types would most likely be used in a network repeater that is housed in a central point in a home office?\n A.Omnidirectional\n B.Parabolic\n C.High-gain\n D.Patch")
print("\nQuestion NO:143\nA customer called the help desk to report a network issue. The customer recently added a hub between the switch and the router in order to duplicate the traffic flow to a logging device. After adding the hub, all the other network components that were connected to the switch slowed more than expected. Which of the following is the MOST likely cause of the issue\n A.Duplex mismatch\n B.Flow control failure\n C.STP malfunction\n D.802.1Q disabled")
print("\nQuestion NO:144\nA network requirement calls for the network traffic of a specific department within a campus network to be monitored. The network has users from each department located in multiple buildings. Which of the following should be configured to meet this requirement?(Choose two)\n A.MDIX\n B.802.1Q\n C.Jumbo frames\n D.Port mirroring\n E.Flow control\n F.LACP")
print("\nQuestion NO:145\nA network engineer is configured is configuring new switches. Some of the trunks ports are in a blocking state.\nWhich of the following should the network engineer reconfigure?\n A.STP\n B.Port mirroring\n C.Flow control\n D.LACP")
print("\nQuestion NO:146\nWhich of the following mowing architectures reduces network latency by enforcing a limit on the number of switching devices on the frame's path between any internal hosts?\n A.Spine and leaf\n B.Software-defined network\n C.Three-tiered\n D.Collapsed core")
print("\nQuestion NO:147\nA Chief Excutive Officer and a network administrator came to an aggrement with a vendor to purchase new equipment for the data center. A document was drafted so all parties would be informed about the scope of the project before it started. Which of the following terms BEST describes the document used?\n A.Contract\n B.Project charter\n C.Memorandum of understanding\n D.Non-diclosure aggrement")
print("\nQuestion NO:148\nWhich of the following redundant devices creates broadcast storms when connected together on a high-availability network?\n A.Switches\n B.Routers\n C.Access points\n D.Servers")
print("\nQuestion NO:149\nWhich of the following storage connection types should be used to allow the consolidation of the physical connections for SAN and LAN in just one Layer 2 protocol?\n A.Fibre Channel\n B.SCSI\n C.T1/E1\n D.FCoE")
print("\nQuestion NO:150\nA technician is monitoring a network interface and notices the device is dropping packets. The cable and interface, however, are in working order.\nWhich of the following is MOST likely the cause?\n A.OID duplication\n B.MIB mismatch\nC.CPU usage\n D.Encapsulation errors")
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print("NO:141 = D.Replace the cable connecting the modem and the workstation\n Explanation: The absence of link LEDs lighting up on both the modem and the workstation suggests a potential issue with the physical connection between them.")
    print("NO:142 = A.Omnidirectional\n Explanation: Omnidirectional antennas radiate wireless signals in all directions, providing 360-degree coverage.")
    print("NO:143 = B.Flow control failure\n Explanation: Flow control mechanisms help regulate the flow of data between devices to prevent packet loss and congestion. If flow control fails in this scenario, it can exacerbate the congestion and slow down network performance significantly.")
    print("NO:144 = B.802.1Q, D.Port mirroring\n Explanation: Port mirroring, also known as SPAN (Switched Port Analyzer), allows the network administrator to copy traffic from one or more ports to another port, typically connected to a monitoring device such as a packet analyzer or network monitoring tool, 802.1Q is a standard for VLAN tagging, which allows the network to be logically segmented into multiple virtual LANs")
    print("NO:145 = A.STP\n Explanation: When trunk ports are in a blocking state, it usually indicates an issue with spanning tree protocol (STP).")
    print("NO:146 = A.Spine and leaf\n Explanation: Spine and Leaf Architecture The spine-leaf architecture consists of only two layers of switches spine and leaf switches.")
    print("NO:147 = B.Project charter\n Explanation: A project charter is a formal short document that states a project exists and provides project managers with written authority to begin work.")
    print("NO:148 = A.Switches\n Explanation: When redundant switches are connected together without proper loop prevention mechanisms (such as Spanning Tree Protocol), it can lead to broadcast storms in a network. This can result in excessive network traffic and degradation of network performance.")
    print("NO:149 = D.FCoE\n Explanation: Fiber Channel protocol over Ethernet(Layer 2). It encapsulates FiberChannel protocol so that it can be transmitted over Ethernet without IP address(Layer3)")
    print("NO:150 = C.CPU usage\n Explanation: High CPU usage is the most likely cause of the device dropping packets when the cable and interfaces are in working order. When the CPU becomes overloaded, the device may not be able to process network packets quickly enough, leading to dropped packets.")
