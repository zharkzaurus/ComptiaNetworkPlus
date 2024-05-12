print('''
QUESTION NO: 231
A network administrator walks into a datacenter and notices an unknown person is following
closely. The administrator stops and directs the person to the security desk. Which of the
following attacks did the network administrator prevent?
A. Evil twin
B. Tailgating
C. Piggybacking
D. Shoulder surfing

QUESTION NO: 232
An on-call network technician receives an automated email alert stating that a power supply
on a firewall has just powered down. Which of the following protocols would BEST allow for
this level of detailed device monitoring?
A. TFTP
B. TLS
C. SSL
D. SNMP

QUESTION NO: 233
A user calls the IT department to report being unable to log in after locking the computer. The
user resets the password, but later in the day the user is again unable to log in after locking
the computer. Which of the following attacks against the user is MOST likely taking place?
A. Brute-force
B. On-path
C. Deauthentication
D. Phishing

QUESTION NO: 234
A company is hosting a secure server that requires all connections to the server to be
encrypted.
A junior administrator needs to harden the web server. The following ports on the web server
are open:
|443|
|80|
|22|
|587|
Which of the following ports should be disabled?
A. 22
B. 80
C. 443
D. 587

QUESTION NO: 235
Which of the following would be the MOST cost-effective recovery solution for a company's
lower- priority applications?
A. Warm site
B. Cloud site
C. Hot site
D. Cold site

QUESTION NO: 236
Which of the following OSI model layers contains IP headers?
A. Presentation
B. Application
C. Data link
D. Network
E. Transport

QUESTION NO: 237
Network users reported that a recent firmware upgrade to a firewall did not resolve the issue
that prompted the upgrade. Which of the following should be performed NEXT?
A. Reopen the service ticket, request a new maintenance window, and roll back to the
anterior firmware version.
B. Gather additional information to ensure users' concerns are not been caused by a different
issue with similar symptoms.
C. Employ a divide-and-conquer troubleshooting methodology by engaging the firewall
vendor's support.
D. Escalate the issue to the IT management team in order to negotiate a new SLA with the
user's manager.

QUESTION NO: 238
A company has multiple offices around the world. The computer rooms in some office
locations are too warm. Dedicated sensors are in each room, but the process of checking
each sensor takes a long time. Which of the following options can the company put in place
to automate temperature readings with internal resources?
A. Implement NetFlow.
B. Hire a programmer to write a script to perform the checks.
C. Utilize ping to measure the response.
D. Use SNMP with an existing collector server.

QUESTION NO: 239
A user is trying to reach an internet destination. A systems administrator thinks that packets
are being dropped in transit. Which of the following command-line tools would confirm if the
packets are being dropped?
A. nslookup
B. traceroute
C. arp
D. telnet

QUESTION NO: 240
Which of the following routing protocols uses attributes to select the best path?
A. EIGRP
B. BGP
C. OSPF
D. RIP''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
Here are the answers to the questions:

QUESTION NO: 231 = B
Explanation: The network administrator prevented a "Tailgating" attack by stopping the unknown person from following closely into the datacenter. Tailgating refers to unauthorized individuals following closely behind authorized personnel to gain entry into a secured area.

QUESTION NO: 232 = D
Explanation: SNMP (Simple Network Management Protocol) would BEST allow for detailed device monitoring, including receiving alerts about specific events such as a power supply powering down. SNMP enables network devices to be monitored and managed remotely.

QUESTION NO: 233 = C
Explanation: The most likely attack taking place against the user is "Deauthentication." If the user is unable to log in after locking the computer, it could indicate that someone is deauthenticating the user's sessions, forcing them to log in again.

QUESTION NO: 234 = B
Explanation: Port 80 should be disabled. Port 80 is used for unencrypted HTTP traffic, and since the company's secure server requires all connections to be encrypted, it's best to disable non-secure ports.

QUESTION NO: 235 = D
Explanation: The MOST cost-effective recovery solution for a company's lower-priority applications would be a "Cold site." A cold site provides basic infrastructure but requires time to set up and activate in the event of a disaster, making it suitable for lower-priority applications.

QUESTION NO: 236 = D
Explanation: The OSI model layer that contains IP headers is the "Network" layer. This layer is responsible for addressing, routing, and packaging data packets.

QUESTION NO: 237 = B
Explanation: The next step should be to gather additional information to ensure that users' concerns are not caused by a different issue with similar symptoms. It's important to investigate further before deciding on the next course of action.

QUESTION NO: 238 = D
Explanation: The company can use SNMP (Simple Network Management Protocol) with an existing collector server to automate temperature readings. SNMP can gather data from dedicated sensors in each room and provide centralized monitoring and management of environmental conditions.

QUESTION NO: 239 = B
Explanation: The command-line tool that would confirm if packets are being dropped in transit is "traceroute." Traceroute traces the route that packets take from the source to the destination, showing each hop along the way and identifying where packet loss may occur.

QUESTION NO: 240 = B
Explanation: BGP (Border Gateway Protocol) uses attributes to select the best path. BGP is an exterior gateway protocol used to exchange routing information between autonomous systems on the Internet, and it evaluates various attributes to determine the best path for routing.
''')
