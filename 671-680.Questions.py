print('''
QUESTION NO: 671
A newly installed multifunction copier needs to be set up so scanned documents can be
emailed to recipients. Which of the following ports from the copier's IP address should be
allowed?
A. 22
B. 25
C. 53
D. 80


QUESTION NO: 672
A technician is trying to install a VoIP phone, but the phone is not turning on. The technician
checks the cable going from the phone to the switch, and the cable is good. Which of the
following actions is needed for this phone to work?
A. Add a POE injector
B. Enable MDIX.
C. Use a crossover cable.
D. Reconfigure the port.

QUESTION NO: 673
Which of the following transceiver types can support up to 40Gbps?
A. SFP+
B. QSFP+
C. QSFP
D. SFP

QUESTION NO: 674
A network technician needs to ensure the company's external mail server can pass reverse
lookup checks. Which of the following records would the technician MOST likely configure?
A. PTR
B. AAAA
C. SPF
D. CNAME

QUESTION NO: 675
Which of the following is used to explain guidelines for users while using network resources?
A. Network cut sheet
B. Baselines
C. Acceptable use policy
D. Regulations

QUESTION NO: 676
A network is experiencing extreme latency when accessing a particular website. Which of the
following commands will BEST help identify the issue?
A. ipconfig
B. netstat
C. tracert
D. ping

QUESTION NO: 677
A security engineer is installing a new IOS on the network. The engineer has asked a
network administrator to ensure all traffic entering and leaving the router interface is available
for the IDS.
Which of the following should the network administrator do?
A. Install a network tap for the IDS
B. Configure ACLs to route traffic to the IDS.
C. Install an additional NIC into the IDS
D. Install a loopback adapter for the IDS.
E. Add an additional route on the router for the IDS.

QUESTION NO: 678
Which of the following can be used to limit the ability of devices to perform only HTTPS
connections to an internet update server without exposing the devices to the public internet?
A. Allow connections only to an internal proxy server.
B. Deploy an IDS system and place it in line with the traffic.
C. Create a screened network and move the devices to it.
D. Use a host-based network firewall on each device.

QUESTION NO: 679
A customer runs a DNS lookup service and needs a network technician to reconfigure the
network to improve performance. The customer wants to ensure that servers are accessed
based on whichever one is topographically closest to the destination. If the server does not
respond, then the next topographically closest server should respond. Which of the following
does the technician need to configure to meet the requirements?
A. Multicast addressing
B. Anycast addressing
C. Broadcast addressing
D. Unicast addressing

QUESTION NO: 680
A network administrator for a small office is adding a passive IDS to its network switch for the
purpose of inspecting network traffic. Which of the following should the administrator use?
A. SNMP trap
B. Port mirroring
C. Syslog collection
D. API integration
''')
answer = input(print('Do you have your answers? yes/no'))
if answer == 'yes':
	print('''
QUESTION NO: 671
To allow scanned documents to be emailed from the multifunction copier, the SMTP (Simple Mail Transfer Protocol) port should be allowed. The SMTP port is port number:
B. 25

QUESTION NO: 672
If the VoIP phone is not turning on despite the cable being good, the likely issue is the lack of power over Ethernet (PoE). To resolve this, the technician should:
A. Add a POE injector

QUESTION NO: 673
The transceiver type that can support up to 40Gbps is:
B. QSFP+

QUESTION NO: 674
To ensure the company's external mail server can pass reverse lookup checks, the technician would MOST likely configure a:
A. PTR record

QUESTION NO: 675
To explain guidelines for users while using network resources, the organization would typically have:
C. Acceptable use policy

QUESTION NO: 676
To identify the source of extreme latency when accessing a particular website, the BEST command to use is:
C. tracert

QUESTION NO: 677
To ensure all traffic entering and leaving the router interface is available for the IDS, the network administrator should:
B. Configure ACLs to route traffic to the IDS.

QUESTION NO: 678
To limit the ability of devices to perform only HTTPS connections to an internet update server without exposing the devices to the public internet, the organization can:
A. Allow connections only to an internal proxy server.

QUESTION NO: 679
To configure the network so that servers are accessed based on whichever one is topographically closest to the destination, the technician needs to configure:
B. Anycast addressing

QUESTION NO: 680
To add a passive IDS to its network switch for inspecting network traffic, the administrator should use:
B. Port mirroring
''')
