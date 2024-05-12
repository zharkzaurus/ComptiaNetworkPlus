print('''
QUESTION NO: 321
Which of the following should a junior security administrator recommend implementing to
mitigate malicious network activity?
A. Intrusion prevention system
B. Load balancer
C. Access logging
D. Endpoint encryption

QUESTION NO: 322
Which of the following bandwidth management techniques uses buffers al the client side to
prevent TCP retransmissions from occurring when the ISP starts to drop packets of specific
types that exceed the agreed traffic rate?
A. Traffic shaping
B. Traffic policing
C. Traffic marking
D. Traffic prioritization

QUESTION NO: 323
Which of the following ports are associated with IMAP? (Choose two.)
A. 25
B. 110
C. 143
D. 587
E. 993
F. 995

QUESTION NO: 324
A network administrator is configuring DCHP and wants to explicitly set an IP address based
on a MAC address. Which of the following should the administrator use?
A. Dynamic assignment
B. Static IP on the server
C. IP helper
D. Exclusion range
E. Reservation

QUESTION NO: 325
A network administrator is investigating a network connectivity issue. The administrator runs
a command to view the status of the network cards. The administrator receives the following
output:
RX packets:45332 errors: 45332 dropped:0 overruns 0 frame:0
Which of the following should the administrator troubleshoot based on the output?
A. Physical layer components
B. VLAN tagging configuration
C. Buffers on the card filling up
D. TCP/IP address settings

QUESTION NO: 326
Which of the following describes a network in which users and devices need to mutually
authenticate before any network resource can be accessed?
A. Least privilege
B. Local authentication
C. Zero trust
D. Need to know

QUESTION NO: 327
Network traffic is being compromised by DNS poisoning every time a company's router is
connected to the internet. The network team detects a non-authorized DNS server being
assigned to the network clients and remediates the incident by setting a trusted DNS server,
but the issue occurs again after internet exposure. Which of the following best practices
should be implemented on the router?
A. Change the device's default password.
B. Disable router advertisement guard.
C. Activate control plane policing.
D. Disable unneeded network services.

QUESTION NO: 328
Which of the following would most likely affect design considerations when building out an
IDF?
A. The source panel amperage
B. The fire suppression system
C. The humidity levels
D. The cable transmission speeds

QUESTION NO: 329
Which of the following is a valid and cost-effective solution to connect a fiber cable into a
network switch without available SFP ports?
A. Use a media converter and a UTP cable
B. Install an additional transceiver module and use GBICs
C. Change the type of connector from SC to F-type
D. Use a loopback adapter to make the connection

QUESTION NO: 330
A user is required to log in to a main web application, which then grants the user access to all
other programs needed to complete job-related tasks. Which of the following authentication
methods does this setup describe?
A. SSO
B. RADIUS
C. TACACS+
D. Multifactor authentication
E. 802.1X
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 321
Answer: A. Intrusion prevention system
Explanation: An intrusion prevention system (IPS) can help mitigate malicious network activity by actively monitoring and analyzing network traffic for signs of malicious behavior and taking action to block or prevent such activity.

QUESTION NO: 322
Answer: A. Traffic shaping
Explanation: Traffic shaping techniques use buffers at the client side to manage the flow of traffic and prevent TCP retransmissions when the ISP starts dropping packets of specific types that exceed the agreed traffic rate.

QUESTION NO: 323
Answers: C. 143, E. 993
Explanation: IMAP (Internet Message Access Protocol) commonly uses port 143 for non-secure connections and port 993 for secure connections.

QUESTION NO: 324
Answer: E. Reservation
Explanation: To explicitly set an IP address based on a MAC address in DHCP, the administrator should use a reservation, which assigns a specific IP address to a specific MAC address.

QUESTION NO: 325
Answer: A. Physical layer components
Explanation: The output indicates errors in received packets, suggesting issues at the physical layer such as cabling or network interface card (NIC) problems.

QUESTION NO: 326
Answer: C. Zero trust
Explanation: Zero trust network architecture requires mutual authentication between users/devices and network resources before access is granted, ensuring a higher level of security by not inherently trusting any user or device.

QUESTION NO: 327
Answer: A. Change the device's default password.
Explanation: Changing the default password on the router can prevent unauthorized access and help mitigate DNS poisoning attacks.

QUESTION NO: 328
Answer: D. The cable transmission speeds
Explanation: Cable transmission speeds affect design considerations for an IDF (Intermediate Distribution Frame) as they dictate the type of cabling infrastructure required to support network connectivity.

QUESTION NO: 329
Answer: A. Use a media converter and a UTP cable
Explanation: Using a media converter allows connecting a fiber cable to a network switch without SFP ports by converting the fiber signal to a form compatible with UTP cables.

QUESTION NO: 330
Answer: A. SSO (Single Sign-On)
Explanation: SSO allows users to log in once to access multiple applications or systems without needing to log in again for each one.
''')
