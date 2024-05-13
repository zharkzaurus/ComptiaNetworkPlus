print('''
QUESTION NO: 441
A network technician is reviewing the interface counters on a router interface. The technician
is attempting to confirm a cable issue. Given the following information:
Which of the following metrics confirms there is a cabling issue?
A. Last cleared
B. Number of packets output
C. CRCs
D. Giants
E. Multicasts

QUESTION NO: 442
A network administrator wants to reduce overhead and increase efficiency on a SAN. Which
of the following can be configured to achieve these goals?
A. Port aggregation
B. Traffic shaping
C. Jumbo frames
D. Flow control

QUESTION NO: 443
A homeowner frequently has guests visit and would like to install a wireless router for their
personal devices. The homeowner wants to ensure that the wireless router is compatible with
the widest range of devices possible. Which of the following standards should a technician
suggest?
A. 802 11ac
B. 802.11b
C. 802.11g
D. 802.11n

QUESTION NO: 444
A security engineer wants to provide a secure, dedicated, alternate access method into an IT
network infrastructure to administer connected devices and IT assets. Which of the following
is the engineer most likely to implement?
A. Remote desktop gateway
B. Authentication and authorization controls
C. Out-of-band management
D. Secure Shell

QUESTION NO: 445
Which of the following describes a situation in which an employee knowingly allows someone
access to a restricted area without verifying authentication?
A. Piggybacking
B. Tailgating
C. Shoulder surfing
D. Phishing

QUESTION NO: 446
An engineer is gathering data to determine the effectiveness of UPSs in use at remote retail
locations. Which of the following statistics can the engineer use to determine the availability
of the remote network equipment?
A. Uptime
B. NetFlow baseline
C. Review TTL stats
D. Interface statistics

QUESTION NO: 447
A network technician is configuring a wireless network that consists of multiple APs for better
coverage and allows roaming between the APs. Which of the following types of SSIDs should
the technician configure?
A. Basic Service Set
B. Independent Basic Service Set
C. Extended Service Set
D. Distribution System Service

QUESTION NO: 448
Which of the following would MOST likely utilize PoE?
A. A camera
B. A printer
C. A hub
D. A modem

QUESTION NO: 449
Which of the following cable types is employed to protect against interference in the physical
environment or when security is a concern?
A. STP
B. RG-6
C. Fiber
D. RG-59

QUESTION NO: 450
A user is connecting a smartwatch to a smartphone for internet access. Which of the
following network types is the user employing?
A. MAN
B. PAN
C. LAN
D. WLAN
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
NO: 441
Answer: C
Explanation: The metric that confirms there is a cabling issue is CRCs (Cyclic Redundancy Checks). CRC errors indicate that there are errors in the data transmission, often caused by issues such as signal interference or faulty cabling. A high number of CRC errors on an interface suggests a potential cabling problem that needs to be addressed.

NO: 442
Answer: C
Explanation: Jumbo frames can be configured to reduce overhead and increase efficiency on a Storage Area Network (SAN). Jumbo frames allow larger Ethernet frames to be transmitted, which can reduce the number of frames processed by the network devices and decrease the overhead associated with processing smaller frames.

NO: 443
Answer: A
Explanation: To ensure compatibility with the widest range of devices possible, the technician should suggest using the 802.11n standard for the wireless router. While 802.11ac offers faster speeds and improved performance, 802.11n provides better compatibility with older devices that may not support the newer standards.

NO: 444
Answer: C
Explanation: Out-of-band management is the most likely solution to provide a secure, dedicated, alternate access method into an IT network infrastructure for administering connected devices and IT assets. Out-of-band management involves managing network devices through a separate, dedicated network or communication channel, ensuring secure access even if the primary network is compromised.

NO: 445
Answer: B
Explanation: Tailgating describes a situation in which an employee knowingly allows someone access to a restricted area without verifying authentication. This typically involves an unauthorized person following closely behind an authorized person to gain access to a secure area without proper authentication.

NO: 446
Answer: A
Explanation: The statistic that the engineer can use to determine the availability of the remote network equipment is uptime. Uptime represents the amount of time that the equipment has been operational and available for use. By analyzing uptime data, the engineer can assess the reliability and availability of the UPSs (Uninterruptible Power Supplies) in use at remote retail locations.

NO: 447
Answer: C
Explanation: The technician should configure an Extended Service Set (ESS) SSID for the wireless network that consists of multiple Access Points (APs) for better coverage and allows roaming between the APs. An ESS allows seamless roaming for wireless clients across multiple APs while maintaining connectivity to the same network.

NO: 448
Answer: A
Explanation: A camera would most likely utilize Power over Ethernet (PoE). PoE allows electrical power to be transmitted over the same Ethernet cable used for data communication. This eliminates the need for separate power cables and simplifies installation, making it a common choice for powering devices such as security cameras, VoIP phones, and wireless access points.

NO: 449
Answer: A
Explanation: STP (Shielded Twisted Pair) cable type is employed to protect against interference in the physical environment or when security is a concern. STP cables have an extra layer of shielding, typically made of metal foil or braided wire, surrounding the twisted pairs of copper wires. This shielding helps to reduce electromagnetic interference (EMI) and radio frequency interference (RFI), making STP cables suitable for environments where interference is a concern.

NO: 450
Answer: B
Explanation: The user is employing a PAN (Personal Area Network) when connecting a smartwatch to a smartphone for internet access. A PAN is a network that interconnects devices in the immediate vicinity of an individual, typically within a range of about 10 meters. Smartwatches, smartphones, and other personal devices often communicate with each other over PANs using wireless technologies such as Bluetooth or Wi-Fi Direct.
''')
