print("Question NO:201\nA client wants to increase overall security after a recent breach. Which of the following would be best to implement? (Choose two.)\n A. Least privilege network access\n B. Dynamic inventories\n C. Central policy management\n D. Zero-touch provisioning\n E. Configuration drift prevention\n F. Subnet range limits")
print("\nQuestion NO:202\nSeveral end users viewing a training video report seeing pixelated images while watching. A network administrator reviews the core switch and is unable to find an immediate cause.\nWhich of the following BEST explains what is occurring?\n A. Jitter\n B. Bandwidth\n C. Latency\n D. Giants")
print("\nQuestion NO:203\nUsers report that the network is slower than usual when accessing on-premises email.\nWhich of the following should a network technician do to confirm the issue?\n A. Review the logging levels of network devices.\n B. Check the audit logs to see if users are accessing email\n C. Compare the network baselines to the current network status.\n D. Verify that users who are trying to access email have LDAP accounts")
print("\nQuestion NO:204\nA customer calls the help desk to report that a Windows PC is unable to open any websites or access any server shares. The help desk technician suspects there is an issue with the configuration.\nWhich of the following commands should the technician issue FIRST to troubleshoot the issue?\n A. tracert\n B. netstat\n C. arp\n D. ipconfig\n E. nmap")
print("\nQuestion NO:205\nA technician needs to set up a wireless connection that utilizes MIMO on non-overlapping channels. Which of the following would be the best choice?\n A. 802.11a\n B. 802.11b\n C. 802.11g\n D. 802.11n")
print('''
Question NO:206
A technician is troubleshooting network connectivity from a wall jack. Readings from a multimeter indicate extremely low ohmic values instead of the rated impedance from the switchport. Which of the following is the MOST likely cause of this issue?
 A. Incorrect transceivers
 B. Faulty LED
 C. Short circuit
 D. Upgraded OS version on switch''')
print('''
Question NO:207
A network technician is troubleshooting internet connectivity issues with users in a subnet. From a host, the technician runs tcpdump and then attempts to navigate to a website using a web browser. The technician receives the following output:
 16:35:58.756583 IP (tos 0x0, ttl 64, id 56522, offset 0, flags [DF], proto UPD (17), length 57)
    192.168.1.15.44232 > 192.168.1.252.53: 50327 + A? comptia .com (29)
 16:35:58.835371 IP (tos 0x0, ttl 64, id 56522, offset 0, flags [DF], proto UPD (17), length 57)
    192.168.1.15.44232 > 192.168.1.252.53: 50327 + A? comptia .com (29)
 16:35:59.652312 IP (tos 0x0, ttl 64, id 56522, offset 0, flags [DF], proto UPD (17), length 57)
    192.168.1.15.44232 > 192.168.1.252.53: 50327 + A? comptia .com (29)
 16:35:58.765212 IP (tos 0x0, ttl 64, id 56522, offset 0, flags [DF], proto UPD (17), length 57)
    192.168.1.15.44232 > 192.168.1.252.53: 50327 + A? comptia .com (29)
Afterward, the browser displays an error. Which of the following explains this issue?
 A. A routing loop is within the network.
 B. The host is configured with incorrect DNS settings.
 C. A broadcast storm is occurring on the subnet.
 D. The host is missing a route to the website.''')
print('''
Question NO:208
A customer hired a network consultant to provide advice on the installation of new wireless access. The customer has several devices that operate in either the 5.0GHz range or the 2.4GHz range, and the best performance must be available. Which of the following standards should the technician suggest?
 A. 802.11a
 B. 802.11b
 C. 802.11g
 D. 802.11n''')
print('''
Question NO:209
A company is designing a SAN and would like to use STP as its medium for communication.
Which of the following protocols would BEST suit the company's needs?
 A. SFTP
 B. Fibre Channel
 C. iSCSI
 D. FTP''')
print('''
Question NO:210
A customer is having issues accessing local resources on the network. A technician questions the user and discovers that a small switch had been taken out of storage and installed so that additional devices could be connected in the room. The technician runs the ping command from the PC to the network server and does not find any issues. However, data transfers to the server are slow, and the transfer appears to be locked up at times.
Which of the following is the most likely cause of the issue?
 A. Duplexing mismatch
 B. Reversed TX/RX pinouts
 C. Cable crosstalk
 D. Failed transceiver''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Question NO: 201 = A, C
Explanation: To increase overall security after a recent breach, the client should implement the following:
A. Least privilege network access: This principle ensures that users are granted only the minimum level of access or permissions necessary to perform their job functions, reducing the risk of unauthorized access to sensitive data.
C. Central policy management: Centralized policy management allows for consistent enforcement of security policies across the network, making it easier to update and manage security configurations.

Question NO: 202 = A
Explanation: The issue of pixelated images while watching a training video is most likely caused by "Jitter." Jitter refers to variations in the delay of received packets, causing delays in the arrival of data packets, which can result in distorted or pixelated images during video playback.

Question NO: 203 = C
Explanation: To confirm the issue of slower-than-usual network access when accessing on-premises email, a network technician should "Compare the network baselines to the current network status." Network baselines provide a reference point for normal network performance, allowing technicians to identify deviations and potential issues.

Question NO: 204 = D
Explanation: The FIRST command a technician should issue to troubleshoot the issue of a Windows PC being unable to open any websites or access server shares is "ipconfig." This command displays the IP configuration details of the PC, including the IP address, subnet mask, and default gateway, helping the technician identify any network configuration issues.

Question NO: 205 = D
Explanation: To set up a wireless connection that utilizes MIMO (Multiple Input, Multiple Output) on non-overlapping channels, the best choice would be "802.11n." The 802.11n standard supports MIMO technology, which improves wireless performance and efficiency by using multiple antennas for transmitting and receiving data.

Question NO: 206 = C
Explanation: The MOST likely cause of the issue indicated by extremely low ohmic values instead of the rated impedance from the switchport is a "Short circuit." A short circuit occurs when there is an unintended connection between two conductive elements, resulting in a low resistance path and abnormal electrical behavior.

Question NO: 207 = B
Explanation: The issue indicated by the tcpdump output and subsequent browser error is likely due to the "Host being configured with incorrect DNS settings." The tcpdump output shows DNS requests being sent repeatedly without receiving responses, suggesting that the host is unable to resolve domain names correctly due to incorrect DNS settings.

Question NO: 208 = D
Explanation: To ensure the best performance for devices operating in either the 5.0GHz or 2.4GHz range, the technician should suggest the "802.11n" standard. 802.11n supports both frequency bands and offers improved throughput and range compared to earlier standards like 802.11a, 802.11b, and 802.11g.

Question NO: 209 = B
Explanation: For a company designing a SAN (Storage Area Network) and planning to use STP (Spanning Tree Protocol) as its medium for communication, the BEST protocol to suit its needs would be "Fibre Channel." Fibre Channel is a high-speed networking technology specifically designed for SAN environments, providing reliable and scalable communication between storage devices.

Question NO: 210 = C
Explanation: The most likely cause of the issue described, where data transfers to the server are slow and appear to be locked up at times after a small switch is installed to connect additional devices, is "Cable crosstalk." Crosstalk occurs when signals transmitted on one cable interfere with signals on adjacent cables, leading to signal degradation and performance issues
.
''')
