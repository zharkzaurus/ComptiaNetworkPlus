print('''
QUESTION NO: 491
An attacker is attempting to find the password to a network by inputting common words and
phrases in plaintext to the password prompt. Which of the following attack types BEST
describes this action?
A. Pass-the-hash attack
B. Rainbow table attack
C. Brute-force attack
D. Dictionary attack

QUESTION NO: 492
A company is opening a new building on the other side of its campus. The distance from the
closest building to the new building is 1,804ft (550m). The company needs to connect the
networking equipment in the new building to the other buildings on the campus without using
a repeater. Which of the following transceivers should the company use?
A. 10GBASE-SW
B. 10GBASE-LR
C. 10GBASE-LX4 over multimode fiber
D. 10GBASE-SR

QUESTION NO: 493
When internal users attempt to access the company website, they are redirected to an
inappropriate website. Which of the following is this scenario an example of?
A. DNS poisoning
B. On-path attack
C. VLAN hopping
D. ARP spoofing

QUESTION NO: 494
Which of the following are the most likely reasons voltage calculations are made before
installing equipment? (Choose two.)
A. To ensure equipment is not damaged
B. To send reports for compliance regulations
C. To speed up the installation process
D. To ensure compatibility
E. To meet legal requirements
F. To ensure the grounding is being maintained

QUESTION NO: 495
A network administrator wants to install new VoIP switches in small network closet but is
concerned about the current heat level of the room. Which of the following should the
administrator take into consideration before installing the new equipment?
A. The power load of the switches
B. The humidity in the room
C. The fire suppression system
D. The direction of airflow within the switches

QUESTION NO: 496
A technician needs to install a new wireless encryption system. They are evaluating the
feasibility of implementing WPA. WPA increases protection over WEP by implementing which
of the following?
A. Strong RC4 encryption
B. Shared secret keys
C. AES encryption
D. Key rotation

QUESTION NO: 497
Which of the following would a network administrator configure to set NTP settings for a
specific subnet within DHCP?
A. Reservation
B. Lease time
C. Scope options
D. Exclusion range

QUESTION NO: 498
A company has a geographically remote office. In order to connect to the internet, the
company has decided to use a satellite WAN link. Which of the following is the GREATEST
concern for this type of connection?
A. Duplex
B. Collisions
C. Jitter
D. Encapsulation

QUESTION NO: 499
A company that replicated the production environment in a cloud environment is starting to
use a load balancer to evenly distribute requests between both environments. Which of the
following does this scenario best describe?
A. High availability
B. NIC teaming
C. FHRP
D. Configuration backup

QUESTION NO: 500
A PC and a network connectivity, and a help desk technician is attempting to resolve the
issue.
The technician plans to run a constant ping command from a Windows workstation while
testing various possible reasons for the connectivity issue.
Which of the following should the technician use?
A. ping -w
B. ping -i
C. ping -s
D. ping -t
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 491
Answer: D
Explanation: The correct answer is D. Dictionary attack. In a dictionary attack, the attacker tries to gain unauthorized access to a system by systematically entering common words and phrases from a predefined list, known as a dictionary, into the password prompt. This method is more efficient than a brute-force attack because it uses a list of likely passwords rather than attempting all possible combinations.

QUESTION NO: 492
Answer: B
Explanation: The correct answer is B. 10GBASE-LR. 10GBASE-LR (Long Range) transceivers are designed for long-distance fiber optic connections, typically spanning up to 10 kilometers. Given the distance of 1,804ft (approximately 550m) between the closest building and the new building on the campus, 10GBASE-LR transceivers would be suitable for establishing connectivity without the need for a repeater.

QUESTION NO: 493
Answer: A
Explanation: The correct answer is A. DNS poisoning. DNS poisoning, also known as DNS cache poisoning, is a type of cyber attack where the attacker manipulates the entries in a DNS server's cache to redirect users to malicious or unintended websites. In the scenario described, when internal users attempt to access the company website, they are redirected to an inappropriate website, indicating a possible DNS poisoning attack.

QUESTION NO: 494
Answer: A, D
Explanation: The correct answers are A and D. To ensure equipment is not damaged and to ensure compatibility. Voltage calculations are made before installing equipment primarily to ensure that the equipment is not damaged by electrical surges or fluctuations. Additionally, voltage calculations help ensure compatibility between the electrical infrastructure and the equipment being installed.

QUESTION NO: 495
Answer: D
Explanation: The correct answer is D. The direction of airflow within the switches. When installing new networking equipment, particularly switches, in a small network closet, it's important to consider the direction of airflow within the switches. Proper airflow management helps prevent overheating and ensures optimal performance and reliability of the equipment.

QUESTION NO: 496
Answer: D
Explanation: The correct answer is D. Key rotation. WPA (Wi-Fi Protected Access) increases protection over WEP (Wired Equivalent Privacy) by implementing key rotation. Key rotation involves changing encryption keys at regular intervals, enhancing the security of the wireless network by making it more difficult for attackers to intercept and decrypt wireless traffic.

QUESTION NO: 497
Answer: C
Explanation: The correct answer is C. Scope options. In DHCP (Dynamic Host Configuration Protocol), scope options are used to configure additional parameters for DHCP clients within a specific subnet. NTP (Network Time Protocol) settings can be configured as scope options to ensure that DHCP clients receive NTP server information and synchronize their clocks accordingly.

QUESTION NO: 498
Answer: C
Explanation: The correct answer is C. Jitter. Jitter refers to the variation in packet arrival times in a network connection. In satellite WAN links, the distance that signals must travel introduces latency and can cause variations in packet arrival times, leading to jitter. High levels of jitter can degrade the quality of voice and video communications and affect the overall performance of network applications.

QUESTION NO: 499
Answer: A
Explanation: The correct answer is A. High availability. The scenario described best fits the concept of high availability. By using a load balancer to evenly distribute requests between the production environment and its cloud replication, the company aims to ensure high availability of its services. Load balancing helps distribute traffic efficiently, improves fault tolerance, and minimizes downtime by redirecting requests to healthy servers.

QUESTION NO: 500
Answer: D
Explanation: The correct answer is D. ping -t. The `-t` option in the ping command in Windows allows the technician to continuously ping the target device until manually stopped. This is useful for monitoring network connectivity over an extended period of time while troubleshooting various issues.
''')
