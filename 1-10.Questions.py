print('Question NO:1\nA company requires a disaster recovery site to have equipment ready to go in the event of a disaster at its main datacenter. The company does not have the budget to mirror all the live data to the disaster recovery site. Which of the following concepts should the company select?\n A.Cold site\n B.Hot site\n C.Warm site\n D.Cloud site')
print('\nQuestion NO:2\nAn engineer is configuring redundant network links between switches. Which of the following should the engineer enable to prevent network stability issues?\n A.802.1Q\n B.STP\n C.Flow control\n D.CSMA/CD')
print('\nQuestion NO:3\nwhich of the following protocols would enable a company to upgrade its internet connection by acquiring its own public IP prefixes and autonomous system number?\n A.EIGRP\n B.BGP\n C.IPv6\n D.MPLS')
print('\nQuestion NO:4\nWhich of the following devices Is used to configure and centrally manage access points installed at different locations?\n A.Wireless controller\n B.Load balancer\n C.Proxy server\n D.VPN concentrator')
print('\nQuestion NO:5\nAn administrator is trying to retrieve management information from the network devices on their LAN. which of the following monitoring resources provides the ability to collect this information encrypted over the network?\n A.SNMPv3\n B.VTP\n C.CDP\n D.IPSec')
print('\nQuestion NO:6\nwhich of the following is used to classify network data for the purpose of providing QoS?\n A.STP\n B.VLANs\n C.SIP\n D.DSCP')
print('\nQuestion NO:7\nA company that uses VoIP telephones is experiencing intermittent issues with one-way audio and dropped conversations. The manufacturer says the sytem will wokr if ping times are less than 50ms.\nThe company Has recorded the following ping times:\n|10ms|10ms|10ms|100ms|70ms|5ms|5ms|80ms|100ms|5ms|5ms|\nwhich of the following is MOST likely causing the issue?\n A.Attenuation\n B.Latency\n C.VLAN mismatch \n D.jitter')
print('\nQuestion NO:8\nA network engineer needs to pass both data and telephony on an access port. Which or the following features should be configured to meet this requirement?\n A.VLAN\n B.VoIP\n C.VIP\n D.VRRP\n')
print('\nQuesiton NO:9\nA network administrator is creating a subnet for a remote office that has 53 network devices. An additional requirement the appropiate number of IP addresses with the LEAST amount of unused adresses?\n A./24\n B./26\n C./28\n D./32')
print('\nQuestion NO:10\nAn engineer was asked to update an MX record for an upcoming project. Which of the following server types is MOST likely to be in scope for the project?\n A.Email\n B.Web\n C.File\n D.Database')
answer = input(print("Do you have your answers? yes/no\n"))
if answer == 'yes':
    print("NO:1 = C.Warm site\nExplanation: Warm site means that some services are up and running meaning that the recovery site dosen't have everything running just parts of it.\nNO:2 = B.STP\nExplanation: STP(Spanning Tree Protocol) is used to connect multiple switches, prevents loops and redudancy in case a switch fails.\nNO:3 = B.BGP\nExplanation: BGP(Border Gateway Protocol) is a set of rules that find the best route for data trasmission on the internet.\nNO:4 = A.Wireless controller\nExplanation: A wireless controller is a device used to manage wireless access points (APs) in different locations.\nNO:5 = A.SNMPv3\nExplanation:SNMPv3(Simple Network Management Protocol Version 3) is the version of SNMP but encrypted and more secure.\nNO:6 = D.DSCP\nExplanation:DSCP(Differentiated Services Code Point) is a way to classify and manage network traffic to provide QoS(Quality of Service in Layer 3 IP networks.\nNO:7 = Attenuation\nExplanation: Attenuation is the loss of signal strenght in networking cables or connections.\nNO:8 = A. VLAN\nExplanation: VLAN(Virtual Local Area Network) it is used to split computers into different VLANS so a broadcast can comunicate to only those in the VLAN and separating the messages to not be recieved to people in another VLAN.\nNO:9 = B./26\nExplanation: as /26 subnet is 255.255.255.192 subnet mask leaving 6 bits for hosts if you add all of the remaining bits you will end up with 63.\nNO:10 = A.Email\nExplanation an MX record is a Mail Exchange record which is used to direct emails to a mail server.")
finish = input(print("Are you done looking at the answers? yes/no"))
if finish == "yes":
    break
