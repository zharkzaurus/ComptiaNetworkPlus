print('''
QUESTION NO: 261
An office area contains two PoE-enabled WAPs. After the area was remodeled, new cable
uplinks were installed in the ceiling above the fluorescent lights. However, after the WAPs
were reconnected, users reported slowness and application errors. An intern reviewed the
network and discovered a lot of CRC errors. A network engineer reviewed the intern's work
and realized UTP cabling was used. Which of the following is the MOST likely cause of the
CRC errors?
A. Insufficient power at the antennas
B. PoE and UTP incompatibility
C. Electromagnetic interference
D. Wrong cable pinout

QUESTION NO: 262
Which of the following is used to elect an STP root?
A. A bridge ID
B. A bridge protocol data unit
C. Interface port priority
D. A switch's root port

QUESTION NO: 263
A technician wants to install a WAP in the center of a room that provides service in a radius
surrounding a radio. Which of the following antenna types should the AP utilize?
A. Omni
B. Directional
C. Yagi
D. Parabolic

QUESTION NO: 264
A company's cloud model consists of the following:
- An on-premises data center
- An IaaS cloud provider
- A private-direct connection from on premises to IaaS
Which of the following best describes the deployment model the company is using?
A. Public
B. Private
C. Hybrid
D. Community

QUESTION NO: 265
Which of the following demarcation connections would be MOST appropriate to use with a
cable modem being installed in a SOHO situation?
A. RG6
B. Cat 6
C. RJ11
D. Multimode fiber

QUESTION NO: 266
A network security technician is designing a solution for a secure remote access scheme with
the following requirements:
- The solution must allow for users at multiple locations to access
corporate resources.
- The on-premises equipment will not handle non-corporate, resource-
bound traffic.
Which of the following should the network security technician consider when designing the
solution? (Choose two.)
A. Clientless VPN
B. Personal VPN
C. Full-tunnel VPN
D. Client-to-site VPN
E. Site-to-site VPN
F. Split-tunnel VPN

QUESTION NO: 267
If a technician does not assign an IP address to a device, the DHCP server will assign the
device
A. static IP address.
B. reservation.
C. dynamic IP address.
D. MAC address.

QUESTION NO: 268
A device is connected to a managed Layer 3 network switch. The MAC address of the device
is known, but the static IP address assigned to the device is not. Which of the following
features of a Layer 3 network switch should be used to determine the IPv4 address of the
device?
A. MAC table
B. Neighbor Discovery Protocol
C. ARP table
D. IPConfig
E. ACL table

QUESTION NO: 269
An IP address is maintained despite a failing UPS that causes a workstation to restart several
times. Which of the following would allow this to occur?
A. DHCP reservation
B. DHCP scope
C. Name server
D. Root DNS server

QUESTION NO: 270
A technician monitors a switch interface and notices it is not forwarding frames on a trunked
port.
However, the cable and interfaces are in working order. Which of the following is MOST likely
the cause of the issue?
A. STP policy
B. Flow control
C. 802.1Q configuration
D. Frame size
''')
answer = input(print("Do you have your answers? yes/no"))
if answer == "yes":
    print('''

NO:261 = D
Explanation: The CRC errors are likely caused by using the wrong cable pinout after the area was remodeled. UTP cabling should follow specific pinout standards to ensure proper transmission.

NO:262 = A
Explanation: The STP root bridge is elected based on the Bridge ID, which consists of a combination of the Bridge Priority and MAC Address. The switch with the lowest Bridge ID becomes the root bridge.

NO:263 = A
Explanation: An omnidirectional antenna broadcasts signal in all directions, making it suitable for providing coverage in a radius surrounding the access point.

NO:264 = C
Explanation: The described deployment model, consisting of an on-premises data center, an IaaS cloud provider, and a private-direct connection between them, represents a hybrid cloud deployment.

NO:265 = C
Explanation: RJ11 is the most appropriate demarcation connection to use with a cable modem in a SOHO situation, as it is the standard connector for telephone lines.

NO:266 = D, F
Explanation: When designing a secure remote access solution with the specified requirements, the network security technician should consider using both client-to-site VPN (such as SSL VPN or IPSec VPN) and split-tunnel VPN to ensure that only corporate-bound traffic is handled by the on-premises equipment.

NO:267 = C
Explanation: If a technician does not assign an IP address to a device, the DHCP server will assign the device a dynamic IP address from its pool of available addresses.

NO:268 = C
Explanation: To determine the IPv4 address of a device connected to a managed Layer 3 network switch, the technician should check the ARP table, which maps MAC addresses to corresponding IPv4 addresses.

NO:269 = A
Explanation: A DHCP reservation would allow the IP address to be maintained despite the workstation restarting, as the DHCP server reserves a specific IP address for the device based on its MAC address.

NO:270 = A
Explanation: The most likely cause of the issue where the switch interface is not forwarding frames on a trunked port is the Spanning Tree Protocol (STP) policy, which may be blocking the port to prevent network loops.
''')
