print('''
QUESTION NO: 741
An IDS was installed behind the edge firewall after a network was breached. The network
was then breached again even though the IDS logged the attack. Which of the following
should be used in place of these devices to prevent future attacks?
A. A network tap
B. A proxy server
C. A UTM appliance
D. A content filter

QUESTION NO: 742
Which of the following TCP ports is used by the Windows OS for file sharing?
A. 53
B. 389
C. 445
D. 1433

QUESTION NO: 743
A network administrator notices that load balancing is not working properly on the web cluster
as previously configured. In speaking with management, a change to the IP addressing
scheme was made yesterday which possibly affected one member of the cluster. Due to the
timing of the events, the administrator theorizes that this change caused the problem. Which
of the following should the administrator do NEXT?
A. Escalate to the management team
B. Change the IP address back to its previous state
C. Test the theory by analyzing logs
D. Create a plan of action to present to management

QUESTION NO: 744
A network device needs to discover a server that can provide it with an IPv4 address. Which
of the following does the device need to send the request to?
A. Default gateway
B. Broadcast address
C. Unicast address
D. Link local address

QUESTION NO: 745
An attacker is using an unknown vulnerability that allows malicious actors to utilize the print
spooler to gain system privileges on a computer. Which of the following is this scenario an
example of?
A. Honeypot
B. Zero-day attack
C. Internal threat
D. External threat

QUESTION NO: 746
The following DHCP scope was configured for a new VLAN dedicated to a large deployment
of
325 loT sensors:
      DHCP network scope:      10.10.0.0/24
      Exclusion range:         10.10.10.1-10.10.10.10
      Gateway:                 10.10.0.1
      DNS:                     10.10.0.2
      DHCP option 66 (TFTP):   10.10.10.4
      DHCP option 4 (NTP):     10.10.10.5
The first 244 loT sensors were able to connect to the TFTP server, download the
configuration file, and register to an loT management system. The other sensors are being
shown as offline.
Which of the following should be performed to determine the MOST likely cause of the partial
deployment of the sensors?
A. Check the gateway connectivity to the TFTP server.
B. Check the DHCP network scope.
C. Check whether the NTP server is online.
D. Check the loT devices for a hardware failure.

QUESTION NO: 747
A network administrator implements a group of access points, only changing the SSID,
credentials, and IP address. Shortly after, users begin reporting poor quality and video loss
while on video calls in the conference room. Which of the following should the administrator
do to MOST effectively troubleshoot during business hours?
A. Remove the current antennas and replace them with directional antennas on each AP.
B. Disconnect the AP and move it closer to the conference room.
C. Configure separate channels on APs that are not supporting the conference room.
D. Reboot the switch and each AP at the same time.

QUESTION NO: 748
Which of the following is considered a physical security detection device?
A. Cameras
B. Biometric readers
C. Access control vestibules
D. Locking racks

QUESTION NO: 749
Which of the following protocols can be routed?
A. NetBEUI
B. Fibre Channel
C. iSCSI
D. FCoE

QUESTION NO: 750
A network analyst is providing access to an FTP server that stores files that are needed by
external contractors who are working on a project. In which of the following network locations
should the FTP server be placed to achieve the MOST secure environment?
A. DMZ network
B. Server network
C. External network
D. Internal network
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Here are the answers with explanations:

QUESTION NO: 741
Answer: C. A UTM appliance
Explanation: A UTM (Unified Threat Management) appliance combines various security features such as firewall, intrusion detection and prevention (IDS/IPS), antivirus, content filtering, and more into a single device. It provides comprehensive protection against various threats and would be more effective in preventing future attacks compared to just an IDS.

QUESTION NO: 742
Answer: C. 445
Explanation: TCP port 445 is used by the Windows OS for file sharing. It is commonly associated with the Server Message Block (SMB) protocol used for sharing files, printers, and other resources on a network.

QUESTION NO: 743
Answer: C. Test the theory by analyzing logs
Explanation: The administrator should test the theory by analyzing logs to confirm whether the change in the IP addressing scheme caused the load balancing issue on the web cluster. This step will provide concrete evidence before taking further actions or presenting a plan of action to management.

QUESTION NO: 744
Answer: B. Broadcast address
Explanation: When a network device needs to discover a server for obtaining an IPv4 address, it sends a DHCP (Dynamic Host Configuration Protocol) request to the broadcast address, which is typically 255.255.255.255. This allows the device to broadcast its request to all devices on the local network.

QUESTION NO: 745
Answer: B. Zero-day attack
Explanation: A zero-day attack refers to an attack that exploits a previously unknown vulnerability in software or hardware. In this scenario, the attacker is exploiting an unknown vulnerability in the print spooler to gain system privileges, making it a zero-day attack.

QUESTION NO: 746
Answer: A. Check the gateway connectivity to the TFTP server.
Explanation: The partial deployment of loT sensors suggests a connectivity issue between the sensors and the TFTP server. Since the first 244 sensors were able to connect successfully, checking the gateway's connectivity to the TFTP server would be the next step in troubleshooting the issue.

QUESTION NO: 747
Answer: A. Remove the current antennas and replace them with directional antennas on each AP.
Explanation: Poor quality and video loss during video calls in the conference room suggest issues with wireless signal strength or interference. Replacing the current antennas with directional antennas can help improve signal strength and coverage specifically in the conference room, thereby addressing the reported issues.

QUESTION NO: 748
Answer: A. Cameras
Explanation: Cameras are physical security detection devices commonly used for surveillance and monitoring. They capture visual information to detect and deter unauthorized access or activities.

QUESTION NO: 749
Answer: C. iSCSI
Explanation: iSCSI (Internet Small Computer System Interface) is a protocol used for routing storage data over IP networks. Unlike NetBEUI (NetBIOS Extended User Interface) and Fibre Channel, iSCSI can be routed over IP networks.

QUESTION NO: 750
Answer: A. DMZ network
Explanation: Placing the FTP server in the DMZ (Demilitarized Zone) network provides the most secure environment for external access. The DMZ network is a separate network segment between the internal network and the internet, allowing external contractors to access the FTP server without directly connecting to the internal network, thereby reducing the risk of unauthorized access to sensitive internal resources.
''')
