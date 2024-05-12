print('''
QUESTION NO: 341
Users are reporting poor wireless performance in some areas of an industrial plant. The
wireless controller is measuring a low EIRP value compared to the recommendations noted
on the most recent site survey. Which of the following should be verified or replaced for the
EIRP value to meet the site survey's specifications? (Choose two.)
A. AP transmit power
B. Channel utilization
C. Signal loss
D. Update ARP tables
E. Antenna gain
F. AP association time

QUESTION NO: 342
A technician is installing a SOHO router. Which of the following should be performed on
every installation and periodically maintained to prevent unauthorized access? (Choose two.)
A. Disable remote management
B. Update the router firmware
C. Disable port forwarding
D. Use complex passwords
E. Disable the SSID broadcast

QUESTION NO: 343
An IT administrator needs to connect older smart-plug devices to the network. The
administrator wants to prevent future issues from occurring by using an 802.11 standard that
only operates on the 2.4GHz frequency. Which of the following standards should the
administrator choose?
A. 802.11a
B. 802.11ac
C. 802.11ax
D. 802.11b

QUESTION NO: 344
An employee working in a warehouse facility is experiencing interruptions in mobile
applications while walking around the facility. According to a recent site survey, the WLAN
comprises autonomous APs that are directly connected to the internet, providing adequate
signal coverage.
Which of the following is the BEST solution to improve network stability?
A. Implement client roaming using an extended service deployment employing a wireless
controller.
B. Remove omnidirectional antennas and adopt a directional bridge.
C. Ensure all APs of the warehouse support MIMO and Wi-Fi 4.
D. Verify that the level of EIRP power settings is set to the maximum permitted by

QUESTION NO: 345
A network administrator needs to set up a file server to allow user access. The organization
uses DHCP to assign IP addresses. Which of the following is the best solution for the
administrator to set up?
A. A separate scope for the file server using a /32 subnet
B. A reservation for the server based on the MAC address
C. A static IP address within the DHCP IP range
D. A SLAAC for the server

QUESTION NO: 346
A network technician has multimode fiber optic cable available in an existing IDF. Which of
the following Ethernet standards should the technician use to connect the network switch to
the existing fiber?
A. 10GBaseT
B. 1000BaseT
C. 1000BaseSX
D. 1000BaseLX

QUESTION NO:347
Go to question number 347 for the simulation

QUESTION NO: 348
A company rents out a large event space and includes wireless internet access for each
tenant.
Tenants reserve a two-hour window from the company each week, which includes a tenant-
specific SSID. However, all users share the company's network hardware.
The network support team is receiving complaints from tenants that some users are unable to
connect to the wireless network. Upon investigation, the support team discovers a pattern
indicating that after a tenant with a particularly large attendance ends its sessions, tenants
throughout the day are unable to connect.
The following settings are common to all network configurations:
| Wireless encryption | WPA2          |
| Captive portal      | Disabled      |
| AP isolation        | Enabled       |
| Subnet mask         | 255.255.255.0 |
| DNS server          | 10.0.0.1      |
| Default gateway     | 10.1.10.1     |
| DHCP scope begin    | 10.1.10.10    |
| DHCP scope end      | 10.1.10.150   |
| DHCP lease time     | 24 hours      |
Which of the following actions would MOST likely reduce this issue? (Choose two.)
A. Change to WPA encryption
B. Change the DNS server to 10.1.10.1.
C. Change the default gateway to 10.0.0.1.
D. Change the DHCP scope end to 10.1.10.250
E. Disable AP isolation
F. Change the subnet mask lo 255.255.255.192.
G. Reduce the DHCP lease time to four hours.

QUESTION NO: 349
A company cell phone was stolen from a technician's vehicle. The cell phone has a
passcode, but it contains sensitive information about clients and vendors. Which of the
following should also be enabled?
A. Factory reset
B. Autolock
C. Encryption
D. Two-factor authentication

QUESTION NO: 350
Which of the following topologies is designed to fully support applications hosted in on-
premises data centers, public or private clouds, and SaaS services?
A. SDWAN
B. MAN
C. PAN
D. MPLS
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 341
Answers: A. AP transmit power, E. Antenna gain
Explanation: To ensure that the EIRP (Effective Isotropic Radiated Power) value meets the site survey's specifications, the AP transmit power and antenna gain should be verified or replaced accordingly.

QUESTION NO: 342
Answers: A. Disable remote management, D. Use complex passwords
Explanation: Disabling remote management and using complex passwords are essential security measures to prevent unauthorized access to SOHO routers.

QUESTION NO: 343
Answer: D. 802.11b
Explanation: 802.11b operates exclusively on the 2.4GHz frequency band, making it suitable for older smart-plug devices that only support this frequency.

QUESTION NO: 344
Answer: A. Implement client roaming using an extended service deployment employing a wireless controller.
Explanation: Implementing client roaming using a wireless controller and deploying extended services can improve network stability by ensuring seamless handover between access points as the employee moves around the facility.

QUESTION NO: 345
Answer: B. A reservation for the server based on the MAC address
Explanation: Setting up a reservation for the file server based on its MAC address within the DHCP server configuration ensures that the server always receives the same IP address.

QUESTION NO: 346
Answer: C. 1000BaseSX
Explanation: Multimode fiber optic cable typically supports Ethernet standards such as 1000BaseSX for Gigabit Ethernet connections over short distances.

QUESTION NO: 347
*Simulation Question*

QUESTION NO: 348
Answers: E. Disable AP isolation, G. Reduce the DHCP lease time to four hours.
Explanation: Disabling AP isolation allows devices to communicate directly with each other, potentially resolving connectivity issues. Reducing the DHCP lease time to four hours ensures that IP addresses are released back to the pool more frequently, preventing exhaustion during busy periods.

QUESTION NO: 349
Answer: C. Encryption
Explanation: Enabling encryption on the stolen cell phone ensures that the sensitive information stored on it remains protected even if the device is compromised.

QUESTION NO: 350
Answer: A. SDWAN
Explanation: SDWAN (Software-Defined Wide Area Network) is designed to fully support applications hosted in various environments, including on-premises data centers, public or private clouds, and SaaS services, by dynamically routing traffic based on application requirements and network conditions.
''')
