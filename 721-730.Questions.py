print('''
QUESTION NO: 721
A new engineer at a company is working to understand the network. Which of the following
diagrams should the engineer review to understand the paths traffic takes?
A. Physical
B. Logical
C. Wiring
D. Rack

QUESTION NO: 722
A technician uses a badge to enter a security checkpoint on a corporate campus. An
unknown individual quickly walks in behind the technician without speaking. Which of the
following types of attacks did the technician experience?
A. Tailgating
B. Evil twin
C. On-path
D. Piggybacking

QUESTION NO: 723
Which of the following connector types would be used to connect to the demarcation point
and provide network access to a cable modem?
A. F-type
B. RJ45
C. LC
D. RJ11

QUESTION NO: 724
An organization wants to implement a method of centrally managing logins to network
services.
Which of the following protocols should the organization use to allow for authentication,
authorization and auditing?
A. MS-CHAP
B. RADIUS
C. LDAPS
D. RSTP

QUESTION NO: 725
An infrastructure company is implementing a cabling solution to connect sites on multiple
continents. Which of the following cable types should the company use for this project?
A. Cat 7
B. Single-mode
C. Multimode
D. Cat 6

QUESTION NO: 726
Which of the following would be BEST to install to find and block any malicious users within a
network?
A. IDS
B. IPS
C. SCADA
D. ICS

QUESTION NO: 727
Which of the following are considered AAA authentication methods? (Select TWO).
A. Kerberos
B. Radius
C. MS-CHAP
D. TACACS+
E. 802.1X

QUESTION NO: 728
A false camera is installed outside a building to assist with physical security.
Which of the following is the device assisting?
A. Detection
B. Recovery
C. Identification
D. Prevention

QUESTION NO: 729
A network technician is reviewing a document that specifies how to handle access to
company resources, such as the Internet and printers, when devices are not part of the
company's assets.
Which of the following agreements would a user be required to accept before using the
company's resources?
A. BYOD
B. DLP
C. AUP
D. MOU

QUESTION NO: 730
Which of the following passwords would provide the best defense against a brute-force
attack?
A. ThisIsMyPasswordForWork
B. Qwerty!@#$
C. Password!1
D. T5!8j5
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 721
Answer: B. Logical
Explanation: A logical diagram illustrates the paths and connections of a network from a logical perspective, showing how data flows between devices and systems regardless of their physical location or arrangement.

QUESTION NO: 722
Answer: A. Tailgating
Explanation: Tailgating occurs when an unauthorized individual follows closely behind an authorized person to gain access to a secure area without proper authentication.

QUESTION NO: 723
Answer: A. F-type
Explanation: F-type connectors are commonly used for coaxial cables and are suitable for connecting cable modems to the demarcation point for network access.

QUESTION NO: 724
Answer: B. RADIUS
Explanation: RADIUS (Remote Authentication Dial-In User Service) is a protocol commonly used for centralized authentication, authorization, and accounting (AAA) for network services.

QUESTION NO: 725
Answer: B. Single-mode
Explanation: Single-mode fiber optic cables are typically used for long-distance communication between sites on different continents due to their ability to transmit data over greater distances with minimal signal loss.

QUESTION NO: 726
Answer: B. IPS
Explanation: An Intrusion Prevention System (IPS) is designed to detect and block malicious users or activities within a network in real-time, providing active defense against various threats.

QUESTION NO: 727
Answers: B. Radius
                 D. TACACS+
Explanation: RADIUS (Remote Authentication Dial-In User Service) and TACACS+ (Terminal Access Controller Access-Control System Plus) are both AAA (Authentication, Authorization, and Accounting) protocols used for authentication purposes.

QUESTION NO: 728
Answer: C. Identification
Explanation: The false camera is assisting with identification by providing visual surveillance to identify individuals or potential security threats outside the building.

QUESTION NO: 729
Answer: A. BYOD
Explanation: BYOD (Bring Your Own Device) is an agreement that specifies how personal devices are allowed to access and use company resources, such as the Internet and printers.

QUESTION NO: 730
Answer: D. T5!8j5
Explanation: This password is strong, containing a mix of uppercase letters, lowercase letters, numbers, and special characters, making it resistant to brute-force attacks compared to the other options.
''')
