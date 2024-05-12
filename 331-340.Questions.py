print('''
QUESTION NO: 331
ARP spoofing would normally be a part of:
A. an on-path attack.
B. DNS poisoning.
C. a DoS attack.
D. a rogue access point.

QUESTION NO: 332
A technician is assisting a user who cannot connect to a network resource. The technician
first checks for a link light. According to troubleshooting methodology, this is an example of:
A. using a bottom-to-top approach.
B. establishing a plan of action.
C. documenting a finding.
D. questioning the obvious.

QUESTION NO: 333
A medical building offers patients Wi-Fi in the waiting room. Which of the following security
features would be the BEST solution to provide secure connections and keep the medical
data protected?
A. Isolating the guest network
B. Securing SNMP
C. MAC filtering
D. Disabling unneeded switchports

QUESTION NO: 334
A network technician is planning the infrastructure for a new data center that will support a
10GBASE-T network. Traffic in the data center is expected to be high, and data integrity is
very important. Which of the following would the network technician most likely include in the
plan?
A. UTP plenum
B. Cat 6a STP
C. PoE injector
D. Riser Cat 5e

QUESTION NO: 335
A technician is installing a cable modem in a SOHO. Which of the following cable types will
the technician MOST likely use to connect a modem to the ISP?
A. Coaxial
B. Single-mode fiber
C. Cat 6e
D. Multimode fiber

QUESTION NO: 336
Which of the following can use a third party back-end LDAP user database for
authentication?
A. ISAKMP
B. TACACS+
C. PKI
D. CHAP

QUESTION NO: 337
Which of the following protocols operates at Layer 4 of the OSI model?
A. TCP
B. ARP
C. IMAP
D. POP3

QUESTION NO: 338
A network technician is attempting to increase throughput by configuring link port aggregation
between a Gigabit Ethernet distribution switch and a Fast Ethernet access switch. Which of
the following is the BEST choice concerning speed and duplex for all interfaces that are
participating in the link aggregation?
A. Half duplex and 1GB speed
B. Full duplex and 1GB speed
C. Half duplex and 100MB speed
D. Full duplex and 100MB speed

QUESTION NO: 339
A network administrator is designing a new network for a company that has frequent power
spikes. The company wants to ensure that employees can keep working and the server will
remain operational. Which of the following is the best solution for the administrator to
recommend?
A. Generator
B. Cold site
C. Redundant power supplies
D. Uninterruptible power supply

QUESTION NO: 340
Which of the following network topologies is ONLY possible between two users?
A. Star
B. Client-server
C. Hybrid
D. Peer-to-peer
''')
answer = input("Do you have your answers? yes/no"))
if answer == "yes":
    print('''
QUESTION NO: 331
Answer: A. an on-path attack.
Explanation: ARP spoofing is typically associated with on-path attacks, where an attacker intercepts or alters communication between two parties by impersonating one of them.

QUESTION NO: 332
Answer: D. questioning the obvious.
Explanation: Checking for a link light is a basic step in troubleshooting, often referred to as "questioning the obvious," as it confirms the physical layer connectivity before moving on to more complex issues.

QUESTION NO: 333
Answer: A. Isolating the guest network
Explanation: Isolating the guest network helps keep medical data protected by segregating it from the main network, reducing the risk of unauthorized access or data breaches.

QUESTION NO: 334
Answer: B. Cat 6a STP
Explanation: Cat 6a STP (Shielded Twisted Pair) provides higher bandwidth and better data integrity, making it suitable for high-traffic data centers where data integrity is crucial.

QUESTION NO: 335
Answer: A. Coaxial
Explanation: Cable modems typically use coaxial cables to connect to the ISP's network infrastructure.

QUESTION NO: 336
Answer: B. TACACS+
Explanation: TACACS+ (Terminal Access Controller Access-Control System Plus) can use a third-party LDAP user database for authentication.

QUESTION NO: 337
Answer: A. TCP
Explanation: TCP (Transmission Control Protocol) operates at Layer 4 of the OSI model, providing reliable, connection-oriented communication between devices.

QUESTION NO: 338
Answer: B. Full duplex and 1GB speed
Explanation: Full duplex operation at 1GB speed would provide the best choice for link port aggregation, maximizing throughput between the distribution switch and the access switch.

QUESTION NO: 339
Answer: D. Uninterruptible power supply
Explanation: An uninterruptible power supply (UPS) would be the best solution to ensure continuous operation during power spikes, providing temporary power to keep systems running until normal power is restored.

QUESTION NO: 340
Answer: D. Peer-to-peer
Explanation: Peer-to-peer network topology is only possible between two users, where each node can communicate directly with other nodes without the need for a central server.A
''')
