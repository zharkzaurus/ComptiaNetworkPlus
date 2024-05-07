print("Question NO:101\nA company is moving to a new building designed with a guest waiting area that has existing network ports. Which of the following practices would BEST secure the network?\n A.Ensure all guests sign an NDA\n B.Disable unneeded switchports in the area\n C.Lower the radio strength to reduce Wi-Fi coverage in the waiting area\n D.Enable MAC filering to block unknown hardware addresses")
print("\nQuestion NO:102\nA network technician needs to correlate security events to analyze a suspected intrusion.\nWhich of the following should the technician use?\n A.SNMP\n B.Log review\n C.Vulnerability scanning\n D.SIEM")
print("\nQuestion NO:103\nA network technician teceives a support ticket about an employee who has misplaced a company-owned cell phone that containns private company information.\nWhich of the following actions should the network technician take to prevent data loss?\n A.Disable the user account\n B.Lock the phone\n C.Turn off the service\n D.Execute remote wipe")
print("\nQuestion NO:104\nWhich of the following is MOST appropiate for enforcing bandwith limits when the performance of an application is not affected by the use of buffering but is heavily impacted by packet drops?\n A.Traffic shaping\n B.Traffic policing\n C.Traffic marking\n D.Traffic classification")
print("\nQuestion NO:105\nA customer lost the connection to the telephone system. The administration console is configured with multiple interface and is connected to multiple switches. The network administrator troubleshoots and verifies the following:\n-The support team is able to connect remotely to the administration console\n-Rebooting the switch shows solid link and activity lights even on unused ports\n-Rebooting the telephone system does not bring the system back online\n-The console is able to connect directly to individual modules successfully\nWhich of the following is most likely reason the costumer lost the connection?\n A.A switch failed\n B.The console software needs to be reinstalled\n C.The cables to the modules need to be replaced\n D.A module failed")
print("\nQuestion NO:106\nA technician is deploying a new SSID for an industrial control system. The control devices require the network to use encryption that employs TKIP and a symmetrical password to connect. Which of the following should the technician configure to ensure compatibility with the control devices?\n A.WPA2-Enterprise\n B.WPA-Enterprise\n C.WPA-PSK\n D.WPA2-PSK")
print("\nQuestion NO:107\nA network administrator is adding a new switch to the network. Which of the following network hardening techniques would be BEST to use once the switch is in producation?\n A.Disable unneeded ports\n B.Disable SSH service\n C.Disable MAC filtering\n D.Disable port security")
print("\nQuestion NO:108\nA technician is troubleshooting intermittent connectivity between devices and viewing the following syslog entries from a switch:\n 21 Feb 2022 16:02:0231 NOTIFICATION %LINK-I-DOWN: G1/10\n 21 Feb 2022 16:02:0262 NOTIFICATION %LINK-I-UP: G1/10\n 21 Feb 2022 16:03:5321 NOTIFICATION %LINK-I-DOWN: G1/10\n 21 Feb 2022 16:03:7873 NOTIFICATION %LINK-I-UP: G1/10\n Which of the following are these entries indicative of?\n A.DDoS attack\n B.Jitter\n C.Latency\n D.Link flapping\n")
print("\nQuestion NO:109\nWhich of the following is a hybrid routing protocol?\n A.BGP\n B.RIPv2\n C.OSPF\n D.EIGRP")
print("\nQuestion NO:110\nA Chief Information Office (CIO) wants to improve the availability of a company's SQL database Which of the following technologies should be utilized to achieve maximum availability?\n A.Clustering\n B.Port aggregation\n C.NIC teaming\n D.Snapshots")
answer = input(print("do you have your answer? yes/no"))
if answer == "yes":
    print("NO:101 = B.Disable unneded switchports in the area\n Explanations: Disabling the unneeded switchports in the area would prevent unauthorized access to the network. This can help ensure that only authorized personnel have access to the network and improve overall network security.")
    print("NO:102 = D.SIEM\n Explanation: SIEM(Security Information and Event Management)is a security solution that helps organizations recognize and address potential security threats and vulnerabilities before they have a chance to disrupt business operations.")
    print("NO:103 = D.Execute remote wipe\n Explanation: Remote wiping allows the network technician to remotely erase all data from the misplaced phone, ensuring that sensitive company information does not fall into unauthorized hands")
    print("NO:104 = B.Traffic policing\n Explanation: Traffic policing involves controlling the rate of traffic sent or received on a network")
    print("NO:105 = A.A switch failed\n Explanation: If the switch is configured to send out network traffic such as broadcast or multicast packets, the activity lights on the switch might light up even if no device is connected to the port.")
    print("NO:106 = C.WPA-PSK\n Explanation: WPA-PSK (Wi-Fi Protected Access Pre-Shared Key) utilizes TKIP encryption and a pre-shared key (symmetrical password) for authentication")
    print("NO:107 = A.Disable unneeded ports\n Explanation: By disabling unneeded ports on the switch, you can reduce the potential attack surface and limit unauthorized access to the network.")
    print("NO:108 = D.Link flapping\n Explanation: The syslog entries indicate that the link on interface G1/10 is going down and then coming back up intermittently. This behavior is typically referred to as 'link flapping.'")
    print("NO:109 = D.EIGRP\n Explanation EIGRP(Enhanced Interior Gateway Routing Protocol)is considered a hybrid routing protocol because it combines characteristics of both distance-vector and link-state routing protocols.")
    print("NO:110 = A.Clustering\n Explanation: Clustering involves grouping multiple servers together to act as a single system, thereby increasing availability and fault tolerance")
