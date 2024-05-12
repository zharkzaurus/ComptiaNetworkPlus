print('''
QUESTION NO: 311
An organization would like to implement a disaster recovery strategy that does not require a
facility agreement or idle hardware. Which of the following strategies MOST likely meets the
organization's requirements?
A. Cloud site
B. Cold site
C. Warm site
D. Hot site

QUESTION NO: 312
The network administrator is informed that a user's email password is frequently hacked by
brute- force programs. Which of the following policies should the network administrator
implements to BEST mitigate this issue? (Choose two.)
A. Captive portal
B. Two-factor authentication
C. Complex passwords
D. Geofencing
E. Role-based access
F. Explicit deny

QUESTION NO: 313
During a risk assessment, which of the following should be considered when planning to
mitigate high CPU utilization of a firewall?
A. Recovery time objective
B. Uninterruptible power supply
C. NIC teaming
D. Load balancing

QUESTION NO: 314
An online gaming company needs a cloud solution that will allow for more virtual resources to
be deployed when tournaments are held. The number of users who access the service
increases during tournaments. The company also needs the resources to return to baseline
levels once the resources are not needed in order to reduce cost. Which of the following
cloud concepts would provide the best solution?
A. Scalability
B. Hybrid
C. Multitenancy
D. Elasticity

QUESTION NO: 315
Which of the following use cases would justify the deployment of an mGRE hub-and-spoke
topology?
A. An Increase In network security using encryption and packet encapsulation
B. A network expansion caused by an increase in the number of branch locations to the
headquarters
C. A mandatory requirement to increase the deployment of an SOWAN network
D. An Improvement In network efficiency by increasing the useful packet payload

QUESTION NO: 316
A help desk supervisor reviews the following excerpt of a call transcript:

Agent: Thanks for calling the help desk. What can I help you with today?
Customer: I have been trying to connect to www.awesome-website.com all morning, but I can't get to it.
Customer: Sure. Thanks for helping.
Agent: It's my pleasure. And indeed, it seems like I can't reach that webiste either.
Customer: I guess that means that it isn't just me, then.

Which of the following was the agent trying to accomplish with this exchange?
A. The agent was questioning the obvious.
B. The agent was verifying full system functionality.
C. The agent was identifying potential effects.
D. The agent was trying to duplicate the problem.

QUESTION NO: 317
A small, family-run business uses a single SOHO router to provide Internet and WiFi to its
employees. At the start of a new week, employees come in and find their usual WiFi network
is no longer available, and there is a new wireless network to which they cannot connect.
Given that information, which of the following should have been done to avoid this situation'
A. The device firmware should have been kept current.
B. Unsecure protocols should have been disabled.
C. Parental controls should have been enabled
D. The default credentials should have been changed

QUESTION NO: 318
Which of the following is the physical topology for an Ethernet LAN?
A. Bus
B. Ring
C. Mesh
D. Star

QUESTION NO: 319
A technician is investigating packet loss to a device that has varying data bursts throughout
the day. Which of the following will the technician MOST likely configure to resolve the issue?
A. Flow control
B. Jumbo frames
C. Duplex
D. Port mirroring

QUESTION NO: 320
A network administrator received reports that a 40Gb connection is saturated. The only
server the administrator can use for data collection in that location has a 10GB connection to
the network.
Which of the following is the best method to use on the server to determine the source of the
saturation?
A. Port mirroring
B. Log aggregation
C. Flow data
D. Packet capture
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 311
Answer: A. Cloud site
Explanation: A cloud site offers disaster recovery capabilities without the need for dedicated facilities or idle hardware. It allows for data replication and failover to virtualized resources in the cloud.

QUESTION NO: 312
Answers: B. Two-factor authentication, C. Complex passwords
Explanation: Implementing two-factor authentication and enforcing complex passwords can significantly enhance security and mitigate the risk of email password hacking through brute-force attacks.

QUESTION NO: 313
Answer: D. Load balancing
Explanation: Load balancing can help mitigate high CPU utilization of a firewall by distributing incoming traffic across multiple firewall instances, thereby reducing the load on individual devices.

QUESTION NO: 314
Answer: D. Elasticity
Explanation: Elasticity in cloud computing allows for scaling resources up or down dynamically based on demand. This would enable the online gaming company to deploy more virtual resources during tournaments and scale back to baseline levels afterward, optimizing cost.

QUESTION NO: 315
Answer: D. An Improvement In network efficiency by increasing the useful packet payload
Explanation: mGRE (Multipoint Generic Routing Encapsulation) hub-and-spoke topology improves network efficiency by reducing overhead and increasing the useful packet payload through packet encapsulation.

QUESTION NO: 316
Answer: D. The agent was trying to duplicate the problem.
Explanation: By confirming that the agent also cannot reach the website, they are attempting to duplicate the problem experienced by the customer, which is an important step in troubleshooting.

QUESTION NO: 317
Answer: A. The device firmware should have been kept current.
Explanation: Keeping the device firmware up to date helps to ensure stability, security, and compatibility, potentially avoiding issues such as the sudden disappearance of the WiFi network.

QUESTION NO: 318
Answer: D. Star
Explanation: In an Ethernet LAN, the physical topology commonly used is the star topology, where each device is connected to a central hub or switch.

QUESTION NO: 319
Answer: A. Flow control
Explanation: Configuring flow control helps manage packet transmission between devices, which can mitigate packet loss caused by varying data bursts.

QUESTION NO: 320
Answer: C. Flow data
Explanation: Flow data, collected using NetFlow or similar technologies, provides insights into network traffic patterns, including identifying the source of saturation on a 40Gb connection from a server with a 10Gb connection.
''')
