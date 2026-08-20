import json

questions = []

def add_q(difficulty, topic, companyPattern, question, options, answer, explanation):
    qid = len(questions) + 1
    questions.append({
        "id": qid,
        "difficulty": difficulty,
        "topic": topic,
        "companyPattern": companyPattern,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation
    })

# ==============================================================================
# UNIT 1 & 2 & 3: Introduction, Topologies, Devices, OSI & TCP/IP Models
# ==============================================================================

add_q(
    "Easy", "OSI Model", ["TCS", "Infosys", "Wipro", "Accenture"],
    "Which layer of the OSI model is responsible for end-to-end communication, flow control, and error recovery across a network?",
    ["Data Link Layer", "Network Layer", "Transport Layer", "Session Layer"],
    2,
    "The Transport Layer (Layer 4) provides transparent transfer of data between end systems, guaranteeing reliable data delivery through flow control, segmentation, and error recovery. Data Link layer works point-to-point within the same segment."
)

add_q(
    "Easy", "Network Topologies", ["Cognizant", "Capgemini", "TCS"],
    "In a network topology where every node is connected to a central hub or switch, what happens if one client device cable fails?",
    ["The entire network goes down", "Only that client device loses connectivity", "The central switch shuts down automatically", "Data collides continuously across the bus"],
    1,
    "In a Star Topology, all devices are connected independently to a central device (hub/switch). A failure in one client's cable only disconnects that specific device without affecting the rest of the network."
)

add_q(
    "Medium", "OSI Model", ["Amazon", "Cisco", "Qualcomm"],
    "What is the correct order of Protocol Data Units (PDUs) as data moves down from the Application layer to the Physical layer in the OSI model?",
    ["Data -> Segment -> Packet -> Frame -> Bits", "Bits -> Frame -> Packet -> Segment -> Data", "Data -> Packet -> Segment -> Frame -> Bits", "Segment -> Data -> Frame -> Packet -> Bits"],
    0,
    "As data descends the OSI model: Application/Presentation/Session produce Data; Transport encapsulates it into Segments (or Datagrams); Network encapsulates into Packets; Data Link encapsulates into Frames; Physical converts frames into Bits."
)

add_q(
    "Easy", "TCP/IP Model", ["Infosys", "Accenture", "HCL"],
    "How many layers are defined in the original TCP/IP protocol suite model, and which layer corresponds to both Physical and Data Link layers of the OSI model?",
    ["7 layers; Network Interface layer", "4 layers; Network Interface (Host-to-Network) layer", "5 layers; Transport layer", "4 layers; Internet layer"],
    1,
    "The original TCP/IP model has 4 layers: Application, Transport, Internet, and Network Interface (Host-to-Network). The Network Interface layer handles physical transmission and media access control, combining OSI Layers 1 and 2."
)

add_q(
    "Medium", "Network Components", ["Cisco", "Juniper Networks", "Tech Mahindra"],
    "Which statement correctly distinguishes between a Layer 2 Switch and a Router (Layer 3)?",
    ["Switches operate on IP addresses using routing tables; Routers operate on MAC addresses using CAM tables.", "Switches operate on MAC addresses and forward within the same broadcast domain; Routers operate on IP addresses and interconnect different broadcast domains.", "Switches perform packet encapsulation while Routers perform bit synchronization only.", "Switches split broadcast domains while Routers split collision domains only."],
    1,
    "Layer 2 switches filter and forward Ethernet frames based on hardware MAC addresses within a LAN (single broadcast domain). Routers operate at Layer 3 using IP addresses to route packets between separate networks/broadcast domains."
)

add_q(
    "Easy", "Network Topologies", ["TCS", "IBM", "Deloitte"],
    "What is the total number of physical duplex links required to connect 'N' nodes in a fully connected Mesh topology?",
    ["N", "N - 1", "N(N - 1) / 2", "N^2"],
    2,
    "In a full mesh topology, every node connects to every other node. For N nodes, each node requires (N - 1) connections. Dividing by 2 for bidirectional/duplex links gives N(N - 1) / 2."
)

add_q(
    "Hard", "OSI Model", ["Google", "Meta", "Microsoft"],
    "Consider a host sending an HTTP request over TLS. At which OSI layers do encryption (TLS) and process-to-process port identification occur?",
    ["Presentation Layer (Layer 6) & Transport Layer (Layer 4)", "Application Layer (Layer 7) & Network Layer (Layer 3)", "Session Layer (Layer 5) & Data Link Layer (Layer 2)", "Presentation Layer (Layer 6) & Network Layer (Layer 3)"],
    0,
    "TLS/SSL handles data encryption, representation, and compression, which maps conceptually to the Presentation Layer (Layer 6). Port numbers identify specific application processes, which is managed by the Transport Layer (Layer 4)."
)

add_q(
    "Medium", "Network Components", ["Arista Networks", "Cisco", "Amazon"],
    "Why does a Layer 2 Ethernet Switch eliminate collisions on a full-duplex network, unlike a Hub?",
    ["Switches use CSMA/CD to detect collision signals.", "Switches provide microsegmentation where each switch port is a separate collision domain.", "Switches operate at Layer 3 and drop colliding IP packets.", "Switches use token passing to grant access to the physical media."],
    1,
    "A hub creates a single shared collision domain for all connected devices. A switch creates dedicated bandwidth on each port (microsegmentation), placing each port in its own collision domain. Under full-duplex, send and receive paths are separate, eliminating collisions."
)

add_q(
    "Easy", "OSI Model", ["Infosys", "Wipro", "Cognizant"],
    "Dialog control, session checkpointing, and synchronization are primary responsibilities of which OSI layer?",
    ["Transport Layer", "Session Layer", "Presentation Layer", "Application Layer"],
    1,
    "The Session Layer (Layer 5) establishes, manages, synchronizes, and terminates dialogues/sessions between application processes running on different devices."
)

add_q(
    "Hard", "TCP/IP Model", ["Qualcomm", "Intel", "Samsung"],
    "During packet decapsulation at a receiving host, how does the Network Layer (IP) know whether to pass the payload to TCP or UDP?",
    ["By inspecting the EtherType field in the IP header.", "By inspecting the Protocol field in the IPv4 header (or Next Header in IPv6).", "By querying the ARP cache for port assignments.", "By reading the TCP/UDP port numbers directly from the Ethernet header."],
    1,
    "The IPv4 header contains an 8-bit 'Protocol' field (e.g., 6 for TCP, 17 for UDP) which tells the IP layer which upper Transport layer protocol should receive the payload. In IPv6, the 'Next Header' field fulfills this role."
)

# ==============================================================================
# UNIT 4: Physical Layer & Signal Transmission
# ==============================================================================

add_q(
    "Medium", "Physical Layer", ["Qualcomm", "Intel", "Cisco"],
    "According to Nyquist's Theorem, what is the maximum bit rate for a noiseless channel with a bandwidth of 3 kHz carrying signals with 4 voltage levels?",
    ["6 kbps", "12 kbps", "24 kbps", "48 kbps"],
    1,
    "Nyquist Bit Rate = 2 * Bandwidth * log2(L). Here Bandwidth B = 3000 Hz, L = 4 levels. Bit Rate = 2 * 3000 * log2(4) = 6000 * 2 = 12,000 bps = 12 kbps."
)

add_q(
    "Hard", "Physical Layer", ["Google", "Nvidia", "Qualcomm"],
    "Using Shannon's Capacity Formula, calculate the theoretical maximum data rate of a channel having a bandwidth of 1 MHz and a Signal-to-Noise Ratio (SNR) of 63.",
    ["1 Mbps", "6 Mbps", "12 Mbps", "63 Mbps"],
    1,
    "Shannon Capacity C = B * log2(1 + SNR). Given B = 1 MHz = 1,000,000 Hz, SNR = 63. C = 10^6 * log2(1 + 63) = 10^6 * log2(64) = 10^6 * 6 = 6 Mbps."
)

add_q(
    "Easy", "Physical Layer", ["TCS", "Accenture", "Capgemini"],
    "Which guided transmission medium uses total internal reflection to transmit light pulses with minimal attenuation over long distances?",
    ["Shielded Twisted Pair (STP)", "Coaxial Cable", "Single-mode Fiber Optic Cable", "Unshielded Twisted Pair (UTP)"],
    2,
    "Fiber optic cables transmit data as light signals using total internal reflection within a glass/plastic core, offering immunity to electromagnetic interference and high bandwidth over long distances."
)

add_q(
    "Medium", "Physical Layer", ["Qualcomm", "Samsung", "Intel"],
    "What is the main purpose of Manchester Encoding used in classic Ethernet (10Base-T)?",
    ["To compress data bytes before transmission.", "To provide self-clocking synchronization by guaranteeing a mid-bit transition.", "To double the effective data throughput without increasing bandwidth.", "To eliminate high-frequency noise using digital filters."],
    1,
    "In Manchester encoding, every bit duration has a transition at the midpoint (low-to-high for 1, high-to-low for 0). This transition provides embedded clock synchronization for the receiver."
)

add_q(
    "Easy", "Physical Layer", ["Infosys", "Wipro", "HCL"],
    "Signal loss during transmission due to resistance of the medium is known as:",
    ["Distortion", "Attenuation", "Thermal Noise", "Crosstalk"],
    1,
    "Attenuation is the gradual loss in signal strength (amplitude) as it propagates through a transmission medium. Amplifiers or repeaters are used to compensate for attenuation."
)

add_q(
    "Hard", "Physical Layer", ["Nvidia", "Qualcomm", "Intel"],
    "A channel has a Signal-to-Noise Ratio expressed as 30 dB. What is the linear Signal-to-Noise Ratio (SNR) value?",
    ["30", "100", "1000", "3000"],
    2,
    "SNR_dB = 10 * log10(SNR). 30 = 10 * log10(SNR) => log10(SNR) = 3 => linear SNR = 10^3 = 1000."
)

# ==============================================================================
# UNIT 5: Data Link Layer, Framing, Switching & Ethernet
# ==============================================================================

add_q(
    "Medium", "Data Link Layer", ["Amazon", "Microsoft", "TCS"],
    "In Bit Stuffing used by Data Link layer framing (e.g., HDLC), what action does the sender take when it encounters five consecutive '1' bits in the data stream?",
    ["Stuffs a '1' bit after the fifth '1'", "Stuffs a '0' bit after the fifth '1'", "Inverts the next bit to '0'", "Sends an ESC control character"],
    1,
    "HDLC frame delimiter flag is 01111110 (6 ones). To prevent user data from mimicking the frame flag, the sender automatically inserts (stuffs) a '0' bit after any sequence of five consecutive '1's. The receiver automatically strips any '0' following five '1's."
)

add_q(
    "Hard", "Data Link Layer", ["Goldman Sachs", "Amazon", "Cisco"],
    "A 1 km long 100 Mbps CSMA/CD Ethernet network has a propagation speed of 2 x 10^8 m/s. What is the minimum frame size required for proper collision detection?",
    ["100 bits", "500 bits", "1000 bits", "2000 bits"],
    2,
    "For CSMA/CD collision detection, Frame Transmission Time (Tt) >= 2 * Propagation Delay (Tp). Tp = Distance / Speed = 1000 m / (2 x 10^8 m/s) = 5 microseconds. 2 * Tp = 10 microseconds. Minimum Frame Size = Bit Rate * (2 * Tp) = 100 Mbps * 10 us = 100 x 10^6 * 10 x 10^-6 = 1000 bits."
)

add_q(
    "Easy", "Data Link Layer", ["Infosys", "TCS", "Cognizant"],
    "What is the standard length of an IEEE 802 MAC address, and how is it usually formatted?",
    ["32 bits formatted as dotted decimal", "48 bits (6 bytes) formatted as hexadecimal pairs", "64 bits formatted as colon-separated decimals", "128 bits formatted as hex quads"],
    1,
    "A MAC address is a 48-bit (6-byte) physical hardware address, typically written in hexadecimal notation separated by colons or hyphens (e.g., 00:1A:2B:3C:4D:5E). The first 24 bits represent the Organizationally Unique Identifier (OUI)."
)

add_q(
    "Medium", "Data Link Layer", ["Cisco", "Walmart Global Tech", "Flipkart"],
    "How does CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) differ from CSMA/CD in wireless networks?",
    ["CSMA/CA aborts frame transmission instantly upon detecting a collision.", "CSMA/CA cannot detect collisions while transmitting because receivers cannot listen and send on the same wireless frequency simultaneously; hence it uses explicit ACK frames.", "CSMA/CA relies on token passing rather than backoff timers.", "CSMA/CA is used only in wired switches."],
    1,
    "In wireless networks (Wi-Fi), a transceiver cannot listen for collisions while transmitting due to signal strength disparities. Thus, CSMA/CA avoids collisions using random backoff timers, Inter-Frame Spacing (IFS), and explicit ACK frames (or RTS/CTS)."
)

add_q(
    "Hard", "Data Link Layer", ["Cisco", "VMware", "Juniper Networks"],
    "In a Go-Back-N ARQ protocol with an m-bit sequence number, what is the maximum allowable sender window size (Ws)?",
    ["2^m", "2^m - 1", "2^(m - 1)", "2^m + 1"],
    1,
    "In Go-Back-N ARQ with an m-bit sequence field, sequence numbers range from 0 to 2^m - 1. The sender window size must satisfy Ws <= 2^m - 1 to prevent ambiguity when ACKs are lost."
)

add_q(
    "Hard", "Data Link Layer", ["Amazon", "Microsoft", "Goldman Sachs"],
    "In Selective Repeat ARQ with an m-bit sequence number, what are the maximum sender window size (Ws) and receiver window size (Wr)?",
    ["Ws = 2^m - 1, Wr = 1", "Ws = 2^(m - 1), Wr = 2^(m - 1)", "Ws = 2^m, Wr = 2^m", "Ws = 2^m - 1, Wr = 2^m - 1"],
    1,
    "In Selective Repeat ARQ, both sender and receiver maintain windows of size Ws = Wr = 2^(m - 1) so that window overlap between old and new sequence numbers does not cause duplicate frame acceptance."
)

add_q(
    "Medium", "Data Link Layer", ["TCS", "Wipro", "Infosys"],
    "Using a 7-bit Hamming Code with single-bit error correction, how many parity bits are required to protect 4 data bits?",
    ["2", "3", "4", "5"],
    1,
    "Using the formula 2^p >= d + p + 1: For d = 4 data bits, if p = 3: 2^3 = 8 >= 4 + 3 + 1 = 8. So 3 parity bits are required (positions 1, 2, 4)."
)

add_q(
    "Medium", "Data Link Layer", ["Arista Networks", "Cisco", "Oracle"],
    "What is the primary function of Virtual Local Area Networks (VLANs) defined under IEEE 802.1Q?",
    ["To increase the speed of physical Ethernet ports.", "To logically segment a single physical switch into multiple isolated broadcast domains.", "To automatically assign IP addresses to hosts.", "To replace Layer 3 routers entirely."],
    1,
    "VLANs (IEEE 802.1Q) allow network administrators to logically segment a Layer 2 switch into multiple distinct broadcast domains, improving network performance, security, and management."
)

# ==============================================================================
# UNIT 6 & 7: Network Layer, IPv4/IPv6 & Subnetting / CIDR / VLSM
# ==============================================================================

add_q(
    "Medium", "IP Addressing", ["Amazon", "Flipkart", "TCS", "Accenture"],
    "What is the subnet mask and total number of usable host IP addresses for a network block with CIDR notation 192.168.10.0/26?",
    ["255.255.255.128, 126 hosts", "255.255.255.192, 62 hosts", "255.255.255.224, 30 hosts", "255.255.255.240, 14 hosts"],
    1,
    "A /26 subnet mask has 26 ones: 11111111.11111111.11111111.11000000 = 255.255.255.192. Number of host bits = 32 - 26 = 6. Total addresses = 2^6 = 64. Usable host addresses = 64 - 2 (Network ID & Broadcast ID) = 62 hosts."
)

add_q(
    "Hard", "IP Addressing", ["Google", "Microsoft", "Goldman Sachs"],
    "An organization is allocated the IP block 172.16.0.0/16 and needs to create subnets that can support at least 500 hosts per subnet. What is the maximum number of such subnets that can be created?",
    ["64 subnets", "128 subnets", "256 subnets", "512 subnets"],
    1,
    "To support at least 500 hosts: 2^h - 2 >= 500 => 2^h >= 502 => h = 9 bits for hosts (since 2^9 = 512). Subnet prefix length = 32 - 9 = /23. Original prefix was /16. Subnetting bits borrowed = 23 - 16 = 7 bits. Number of subnets = 2^7 = 128 subnets."
)

add_q(
    "Easy", "IP Addressing", ["Infosys", "TCS", "Capgemini"],
    "Which of the following IP ranges is designated as RFC 1918 Private IP address space?",
    ["11.0.0.0 to 11.255.255.255", "172.16.0.0 to 172.31.255.255", "192.168.0.0 to 192.169.255.255", "169.254.0.0 to 169.254.255.255"],
    1,
    "RFC 1918 defines private IP ranges: Class A: 10.0.0.0/8, Class B: 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), Class C: 192.168.0.0/16 (192.168.0.0 - 192.168.255.255). 169.254.0.0/16 is APIPA."
)

add_q(
    "Medium", "IP Addressing", ["Cisco", "Amazon", "Walmart Global Tech"],
    "What is the network address and broadcast address for a host with IP 10.1.50.75 and subnet mask 255.255.240.0 (/20)?",
    ["Network: 10.1.48.0, Broadcast: 10.1.63.255", "Network: 10.1.32.0, Broadcast: 10.1.47.255", "Network: 10.1.50.0, Broadcast: 10.1.50.255", "Network: 10.1.0.0, Broadcast: 10.1.255.255"],
    0,
    "Subnet mask 255.255.240.0 has block size 256 - 240 = 16 in the 3rd octet. Multiples of 16 in 3rd octet are 0, 16, 32, 48, 64... Host 10.1.50.75 falls in range 10.1.48.0 to 10.1.63.255. Network ID = 10.1.48.0, Broadcast ID = 10.1.63.255."
)

add_q(
    "Easy", "Network Layer", ["TCS", "Infosys", "Wipro"],
    "What is the primary function of Network Address Translation (NAT)?",
    ["To assign dynamic IP addresses automatically to local hosts.", "To map multiple private IP addresses behind a single public IP address for internet access.", "To translate MAC addresses to IP addresses.", "To encrypt IP packet payloads during transit."],
    1,
    "NAT (specifically NAT/PAT or NAPT) allows multiple hosts on a local private network (RFC 1918) to share a single public IP address when communicating with external internet servers, conserving public IPv4 addresses."
)

add_q(
    "Medium", "IPv6", ["Qualcomm", "Cisco", "Intel"],
    "Which of the following statements about IPv6 is FALSE?",
    ["IPv6 addresses are 128 bits in length.", "IPv6 headers do not include a checksum field to reduce processing overhead at routers.", "IPv6 relies on broadcast messaging for address discovery.", "IPv6 uses Neighbor Discovery Protocol (NDP) instead of ARP."],
    2,
    "IPv6 completely eliminates broadcast messaging; instead, it uses Multicast (specifically Solicited-Node Multicast) and Neighbor Discovery Protocol (NDP) for host discovery, eliminating network-wide broadcast noise."
)

add_q(
    "Hard", "Routing", ["Cisco", "Juniper Networks", "Arista Networks"],
    "Which routing algorithm and metric are used by Open Shortest Path First (OSPF)?",
    ["Distance Vector algorithm using Hop Count metric", "Link State algorithm using Dijkstra's algorithm and Cost metric based on bandwidth", "Path Vector algorithm using AS Path metric", "Bellman-Ford algorithm using Delay metric"],
    1,
    "OSPF is an interior gateway protocol (IGP) based on the Link-State routing concept. It builds a complete topology graph using Link State Advertisements (LSAs) and calculates shortest paths using Dijkstra's algorithm based on interface Cost (10^8 / Bandwidth)."
)

add_q(
    "Medium", "Routing", ["Cisco", "Amazon", "Google"],
    "What mechanism is used by Distance Vector routing protocols (like RIP) to prevent two-node routing loops caused by slow convergence?",
    ["Spanning Tree Algorithm", "Split Horizon with Poison Reverse", "Dijkstra's Shortest Path First", "Three-Way Handshake"],
    1,
    "Distance Vector protocols use Split Horizon (never advertising a route back out the interface it was learned from) and Poison Reverse (advertising unreachable routes with infinite metric of 16) to prevent two-node routing loops."
)

add_q(
    "Hard", "Routing", ["Google", "Meta", "Microsoft"],
    "Which protocol is used for routing traffic between different Autonomous Systems (AS) across the global Internet?",
    ["OSPF (Open Shortest Path First)", "RIP (Routing Information Protocol)", "BGP (Border Gateway Protocol)", "IS-IS (Intermediate System to Intermediate System)"],
    2,
    "Border Gateway Protocol (BGP) is the standardized Path Vector exterior gateway protocol (EGP) designed to exchange routing and reachability information among Autonomous Systems on the global Internet."
)

add_q(
    "Easy", "IP Addressing", ["Accenture", "TCS", "Cognizant"],
    "If a DHCP server is unreachable, a Windows host automatically assigns itself an IP address from the range 169.254.x.x. What is this address called?",
    ["Loopback IP", "APIPA (Automatic Private IP Addressing)", "Multicast IP", "Default Gateway IP"],
    1,
    "APIPA (Automatic Private IP Addressing) uses the link-local IPv4 range 169.254.0.1 to 169.254.255.254 when a host cannot communicate with a DHCP server."
)

# ==============================================================================
# UNIT 8: Address Resolution & Helper Protocols (ARP, ICMP, DHCP)
# ==============================================================================

add_q(
    "Medium", "ARP", ["Amazon", "Cisco", "Infosys"],
    "Host A wants to send an IP packet to Host B on the same local network, but Host A does not know Host B's MAC address. What message exchange occurs?",
    ["Host A sends an ARP Request via Unicast; Host B replies via Broadcast.", "Host A sends an ARP Request via Broadcast (FF:FF:FF:FF:FF:FF); Host B replies via Unicast.", "Host A sends a DHCP Request via Broadcast; DHCP server replies with Host B's MAC address.", "Host A sends an ICMP Echo Request; Host B replies with Echo Reply containing its MAC."],
    1,
    "ARP Request is sent as a Layer 2 Broadcast (destination MAC FF:FF:FF:FF:FF:FF) so all hosts on the local link receive it. The target host Host B recognizes its IP and replies with an ARP Reply sent as a Layer 2 Unicast directly back to Host A."
)

add_q(
    "Medium", "ICMP", ["TCS", "Wipro", "Capgemini"],
    "What protocol and ICMP message type are utilized by the 'ping' command line utility to test network reachability?",
    ["TCP; ICMP Type 0 (Echo Reply) and Type 8 (Echo Request)", "IP / ICMP; Type 8 (Echo Request) and Type 0 (Echo Reply)", "UDP; ICMP Type 3 (Destination Unreachable)", "ARP; ICMP Type 11 (Time Exceeded)"],
    1,
    "The 'ping' tool uses ICMP (IP protocol 1). The client sends an ICMP Echo Request (Type 8, Code 0), and the destination responds with an ICMP Echo Reply (Type 0, Code 0)."
)

add_q(
    "Hard", "ICMP", ["Google", "Amazon", "Cisco"],
    "How does the traditional 'traceroute' utility on Linux discover intermediate routers along a network path?",
    ["By gradually increasing the Time-To-Live (TTL) field in IP packet headers starting from 1 and capturing ICMP Time Exceeded (Type 11) messages.", "By sending ARP requests to every router in the routing table.", "By querying DNS servers for trace records.", "By sending TCP SYN packets with sequential port numbers."],
    0,
    "Traceroute sends packets with incremental TTL values starting at 1. Each hop decrements TTL by 1. When TTL reaches 0, the router drops the packet and responds with an ICMP Time Exceeded (Type 11, Code 0) message back to the source, revealing the router's IP address."
)

add_q(
    "Medium", "DHCP", ["Infosys", "TCS", "Deloitte"],
    "What is the standard 4-step sequence of messages exchanged between a client and a server during DHCP IP address allocation?",
    ["DORA: Discover -> Offer -> Request -> Acknowledge", "ROAD: Request -> Offer -> Acknowledge -> Discover", "AROD: Acknowledge -> Request -> Offer -> Discover", "DROP: Discover -> Request -> Offer -> Ping"],
    0,
    "The DHCP lease handshake uses DORA: 1. DHCP Discover (Client broadcast), 2. DHCP Offer (Server unicast/broadcast offer), 3. DHCP Request (Client broadcast acceptance), 4. DHCP Acknowledgement (Server confirmation)."
)

add_q(
    "Easy", "ARP", ["Cognizant", "HCL", "Tech Mahindra"],
    "What security vulnerability occurs when an attacker broadcasts forged ARP messages on a local network to associate their MAC address with a legitimate IP address?",
    ["SYN Flooding", "ARP Spoofing / Poisoning (Man-in-the-Middle)", "DNS Amplification", "Buffer Overflow"],
    1,
    "ARP Spoofing (or ARP Poisoning) involves sending fake ARP replies onto a LAN to corrupt the ARP caches of target hosts, enabling Man-in-the-Middle (MitM) eavesdropping or denial of service."
)

# ==============================================================================
# UNIT 9: Transport Layer (TCP, UDP, Handshakes, Flow & Congestion Control)
# ==============================================================================

add_q(
    "Medium", "TCP", ["Amazon", "Microsoft", "TCS", "Accenture"],
    "What flags are set in the TCP header during the standard 3-Way Handshake establishment phase?",
    ["1: SYN, 2: SYN-ACK, 3: ACK", "1: SYN, 2: ACK, 3: FIN", "1: PSH, 2: SYN-ACK, 3: RST", "1: SYN, 2: PSH-ACK, 3: ACK"],
    0,
    "TCP connection establishment: Step 1: Client sends SYN flag set. Step 2: Server responds with SYN and ACK flags set. Step 3: Client sends ACK flag set. Connection is then ESTABLISHED."
)

add_q(
    "Hard", "TCP", ["Google", "Amazon", "Microsoft", "Goldman Sachs"],
    "During TCP connection teardown (4-Way Wavehand), what is the purpose of the TIME_WAIT state on the active closer host?",
    ["To wait for the remote host to send a SYN packet.", "To ensure the final ACK packet is received by the peer and to allow old duplicate segments in the network to expire.", "To retransmit unacknowledged data payloads.", "To calculate the final Round Trip Time (RTT)."],
    1,
    "TIME_WAIT (lasting 2 * MSL, Maximum Segment Lifetime) ensures: 1. If the final ACK is lost, the host can retransmit ACK when receiving the peer's retransmitted FIN. 2. Any delayed duplicate packets from this connection expire in the network so they don't corrupt a future socket connection."
)

add_q(
    "Medium", "TCP", ["Cisco", "Oracle", "Qualcomm"],
    "In TCP flow control, what does the 'Receiver Window' (rwnd) advertised in the TCP header indicate?",
    ["The total maximum bandwidth of the physical link.", "The amount of available space in the receiver's buffer that can accept incoming data without overflowing.", "The congestion state of intermediate routers.", "The total number of packet collisions on the wire."],
    1,
    "TCP Flow Control uses a sliding window protocol. The receiver advertises its available buffer space in the 'Window Size' field (rwnd) of every ACK segment, preventing a fast sender from swamping a slow receiver."
)

add_q(
    "Hard", "TCP", ["Microsoft", "Meta", "Google", "Amazon"],
    "In TCP congestion control, what triggers the Fast Retransmit mechanism before the retransmission timeout (RTO) expires?",
    ["Receipt of a TCP FIN segment", "Receipt of 3 Duplicate Acknowledgments (DupACKs) for the same sequence number", "A drop in the receiver's window size to zero", "Receipt of an ICMP Destination Unreachable packet"],
    1,
    "When a TCP sender receives 3 identical duplicate ACKs for a specific packet segment, it assumes that packet was lost in transit and immediately retransmits the missing segment (Fast Retransmit) without waiting for the RTO timer to expire."
)

add_q(
    "Medium", "TCP vs UDP", ["Infosys", "TCS", "Accenture"],
    "Which of the following application scenarios is UDP preferred over TCP?",
    ["File transfer via SFTP", "Web browsing via HTTPS", "Real-time video streaming and VoIP gaming", "Email transmission via SMTP"],
    2,
    "UDP is lightweight, connectionless, and has minimal overhead without retransmission delays. This makes UDP ideal for real-time video/audio streaming and online gaming, where low latency is critical and lost packets can be tolerated."
)

add_q(
    "Easy", "Transport Layer", ["Wipro", "Capgemini", "Cognizant"],
    "What constitutes a unique Network Socket pair for a point-to-point TCP connection?",
    ["Source MAC and Destination MAC addresses", "Source IP Address, Source Port, Destination IP Address, Destination Port", "IP Address and Subnet Mask", "Process ID and Thread ID"],
    1,
    "A TCP socket is uniquely defined by a 4-tuple: (Source IP Address, Source Port Number, Destination IP Address, Destination Port Number)."
)

add_q(
    "Hard", "TCP", ["Qualcomm", "Nvidia", "Intel"],
    "Calculate the maximum throughput of a TCP connection with a window size of 64 KB and a Round Trip Time (RTT) of 20 milliseconds.",
    ["1.6 Mbps", "13.1 Mbps", "26.2 Mbps", "52.4 Mbps"],
    2,
    "Throughput = Window Size / RTT. Window Size = 64 KB = 64 * 1024 * 8 bits = 524,288 bits. RTT = 20 ms = 0.02 seconds. Throughput = 524,288 bits / 0.02 s = 26,214,400 bps ≈ 26.2 Mbps."
)

add_q(
    "Medium", "TCP", ["Cisco", "VMware", "Juniper Networks"],
    "What TCP flag is used to abruptly reset or terminate a connection when an unexpected segment arrives or an invalid handshake is attempted?",
    ["FIN", "URG", "RST", "PSH"],
    2,
    "The RST (Reset) flag immediately aborts a TCP connection without going through the normal graceful 4-way termination sequence."
)

# ==============================================================================
# UNIT 10: Application Layer Protocols & Well-Known Ports
# ==============================================================================

add_q(
    "Easy", "Application Layer", ["TCS", "Infosys", "Wipro", "Cognizant"],
    "Match the standard well-known port numbers to their corresponding default protocols: DNS, HTTP, HTTPS, SSH.",
    ["DNS: 53, HTTP: 80, HTTPS: 443, SSH: 22", "DNS: 80, HTTP: 53, HTTPS: 22, SSH: 443", "DNS: 22, HTTP: 80, HTTPS: 8080, SSH: 53", "DNS: 53, HTTP: 8080, HTTPS: 443, SSH: 21"],
    0,
    "Standard default port numbers: DNS uses UDP/TCP port 53; HTTP uses TCP port 80; HTTPS uses TCP port 443; SSH uses TCP port 22."
)

add_q(
    "Medium", "DNS", ["Amazon", "Microsoft", "Google"],
    "In the Domain Name System (DNS), which record type maps a domain hostname to an IPv6 address?",
    ["A Record", "AAAA Record", "CNAME Record", "MX Record"],
    1,
    "An 'AAAA' (Quad-A) record maps a domain name to a 128-bit IPv6 address. An 'A' record maps to a 32-bit IPv4 address; 'CNAME' creates an alias; 'MX' specifies mail exchange servers."
)

add_q(
    "Medium", "HTTP", ["Amazon", "Flipkart", "Walmart Global Tech"],
    "How does HTTP/1.1 Persistent Connections (Keep-Alive) improve web performance compared to original HTTP/1.0?",
    ["It encrypts all HTTP headers using TLS automatically.", "It allows multiple HTTP requests and responses to be sent over a single underlying TCP connection without re-establishing TCP handshakes.", "It converts text responses into binary format.", "It uses UDP instead of TCP for data transfers."],
    1,
    "HTTP/1.0 established a separate TCP connection for every single asset (HTML, image, CSS), introducing heavy RTT handshake overhead. HTTP/1.1 introduced persistent connections, reusing one TCP connection for multiple HTTP requests."
)

add_q(
    "Hard", "HTTP", ["Google", "Meta", "ServiceNow"],
    "What major architectural enhancement was introduced in HTTP/2 compared to HTTP/1.1?",
    ["Switching from TCP to UDP/QUIC transport.", "Binary framing layer with multiplexing of requests over a single TCP connection, head-of-line blocking reduction at HTTP level, and HPACK header compression.", "Elimination of SSL/TLS certificates.", "Mandatory use of XML payload formatting."],
    1,
    "HTTP/2 introduced binary framing, multiplexing multiple concurrent request/response streams over a single TCP connection, server push, and HPACK header compression, greatly overcoming HTTP/1.1 head-of-line blocking."
)

add_q(
    "Medium", "Application Layer", ["TCS", "Accenture", "IBM"],
    "Which protocols are used for retrieving email messages from a mail server to a client mail app, and what is the key difference between them?",
    ["SMTP and POP3; SMTP deletes emails on download while POP3 keeps them on the server.", "POP3 and IMAP; POP3 typically downloads emails locally and removes them from server, whereas IMAP syncs emails across devices directly on the server.", "FTP and SFTP; FTP is unencrypted while SFTP is encrypted.", "SNMP and NTP; SNMP tracks time while NTP manages mail queues."],
    1,
    "POP3 (Port 110/995) downloads emails to a local device, usually deleting them from the server. IMAP (Port 143/993) synchronizes email folders and states live across multiple client devices directly on the mail server."
)

add_q(
    "Easy", "Application Layer", ["Infosys", "Wipro", "Capgemini"],
    "Which protocol operates on TCP ports 20 and 21 for transferring files between hosts?",
    ["TFTP", "FTP", "SFTP", "HTTP"],
    1,
    "FTP (File Transfer Protocol) uses two ports: TCP Port 21 for command/control connection, and TCP Port 20 for data transfer."
)

# ==============================================================================
# UNIT 11: Network Security & Cryptography
# ==============================================================================

add_q(
    "Medium", "Network Security", ["Amazon", "Microsoft", "Goldman Sachs"],
    "In a Public Key Infrastructure (PKI) system using RSA encryption, if Alice wants to send a confidential encrypted message to Bob, which key must Alice use to encrypt the message?",
    ["Alice's Private Key", "Alice's Public Key", "Bob's Public Key", "Bob's Private Key"],
    2,
    "In asymmetric encryption, to ensure confidentiality, the sender (Alice) encrypts the plaintext using the recipient's (Bob's) Public Key. Only Bob's corresponding Private Key can decrypt the ciphertext."
)

add_q(
    "Hard", "Network Security", ["Google", "Meta", "PayPal"],
    "How does a Digital Signature provide both Authentication and Non-Repudiation for a transmitted message?",
    ["The sender encrypts the entire message using the receiver's public key.", "The sender hashes the message and encrypts the hash value using the sender's own Private Key; anyone with sender's Public Key can verify it.", "The sender encrypts the hash using a shared secret symmetric key.", "The sender requests a digital token from a local DHCP server."],
    1,
    "A digital signature is created by hashing the message and encrypting the digest using the sender's Private Key. Recipients decrypt the signature with the sender's Public Key. Successful decryption authenticates the sender's identity and provides non-repudiation."
)

add_q(
    "Medium", "Network Security", ["Cisco", "Oracle", "PwC"],
    "What is the difference between a Statefully Inspecting Firewall and a Packet Filtering Firewall?",
    ["Packet filtering firewalls inspect payload data using AI algorithms; stateful firewalls look only at MAC addresses.", "Packet filtering firewalls examine isolated header fields (IP/Port) without context; stateful firewalls track active connection states (e.g., TCP SYN/ACK sequences) in a state table.", "Stateful firewalls operate only at Layer 1; packet filtering operates at Layer 7.", "Stateful firewalls replace routers entirely."],
    1,
    "Stateless packet filters evaluate each packet in isolation against ACL rules. Stateful firewalls track connection states (such as TCP handshakes and sequence numbers) in a state table, dynamically allowing returning payload traffic for established sessions."
)

add_q(
    "Hard", "Network Security", ["Google", "Cloudflare", "Amazon"],
    "During a TLS 1.2 Handshake, what role does Diffie-Hellman Ephemeral (DHE / ECDHE) key exchange play in security?",
    ["It prevents DNS cache poisoning attacks.", "It provides Perfect Forward Secrecy (PFS), ensuring past session keys cannot be decrypted even if the server's long-term private key is compromised later.", "It speeds up symmetrical encryption by skipping hash calculations.", "It authenticates the client without requiring a password."],
    1,
    "Ephemeral Diffie-Hellman (ECDHE) generates temporary, single-session key pairs for each connection. This achieves Perfect Forward Secrecy (PFS): compromising the server's master private key in the future does not allow an attacker to decrypt past recorded session traffic."
)

add_q(
    "Easy", "Network Security", ["TCS", "Infosys", "Cognizant"],
    "What type of network attack floods a server with millions of spoofed incoming requests from a network of compromised distributed devices (botnet)?",
    ["Man-in-the-Middle (MitM) Attack", "Distributed Denial of Service (DDoS) Attack", "SQL Injection", "Cross-Site Scripting (XSS)"],
    1,
    "A Distributed Denial of Service (DDoS) attack harnesses a botnet of infected host machines to overwhelm a target server's bandwidth or computing resources, rendering services unavailable to legitimate users."
)

# ==============================================================================
# UNIT 12: Wireless & Mobile Networks
# ==============================================================================

add_q(
    "Medium", "Wireless Networks", ["Qualcomm", "Intel", "Samsung"],
    "In Wi-Fi IEEE 802.11 wireless networks, what is the purpose of the optional RTS/CTS (Request to Send / Clear to Send) handshaking mechanism?",
    ["To encrypt wireless frames using WPA3.", "To resolve the 'Hidden Node Problem' and mitigate collisions on shared radio channels.", "To automatically boost antenna power output.", "To assign dynamic IP addresses to mobile clients."],
    1,
    "The Hidden Node Problem occurs when two stations cannot hear each other but can both reach the Access Point (AP). RTS/CTS reserves the wireless channel prior to frame transmission, notifying all nearby nodes to defer transmission."
)

add_q(
    "Easy", "Wireless Networks", ["Infosys", "Wipro", "TCS"],
    "What identifier is broadcast by a wireless Access Point (AP) to advertise the human-readable name of a Wi-Fi network?",
    ["BSSID", "SSID (Service Set Identifier)", "MAC Address", "Subnet Mask"],
    1,
    "SSID (Service Set Identifier) is the 32-character unique name that identifies a wireless local area network (WLAN)."
)

add_q(
    "Medium", "Wireless Networks", ["Qualcomm", "Samsung", "Cisco"],
    "Which wireless frequency bands are used by standard Wi-Fi 6 (IEEE 802.11ax)?",
    ["2.4 GHz only", "5 GHz only", "2.4 GHz and 5 GHz", "60 GHz millimeter wave only"],
    2,
    "Wi-Fi 6 (802.11ax) operates across both the 2.4 GHz and 5 GHz bands, introducing OFDMA and MU-MIMO for higher efficiency. (Wi-Fi 6E extends this into the 6 GHz band)."
)

# ==============================================================================
# ADVANCED TOPICS: SDN, CDN, HTTP/3, QUIC, Cloud Networking
# ==============================================================================

add_q(
    "Hard", "Advanced Topics", ["Google", "Meta", "Cloudflare"],
    "What protocol is used by HTTP/3 as its underlying transport layer, replacing TCP?",
    ["SCTP", "QUIC (Quick UDP Internet Connections)", "RSVP", "RTP"],
    1,
    "HTTP/3 replaces TCP with QUIC, an encrypted transport protocol built on top of UDP. QUIC eliminates TCP head-of-line blocking across multiplexed streams and reduces connection establishment latency to zero or 1 RTT."
)

add_q(
    "Hard", "Advanced Topics", ["Cisco", "VMware", "Arista Networks"],
    "In Software-Defined Networking (SDN) architecture, what critical structural separation is implemented?",
    ["Separation of IPv4 addresses from IPv6 addresses", "Separation of the Control Plane (routing logic/decision making) from the Data Plane (packet forwarding hardware)", "Separation of physical switches from routers", "Separation of application data from DNS queries"],
    1,
    "SDN decouples the network Control Plane (which decides how packets should be routed via a centralized software controller) from the underlying Data/Forwarding Plane (which physically moves packets based on rules)."
)

add_q(
    "Medium", "Advanced Topics", ["Amazon", "Akamai", "Netflix", "Cloudflare"],
    "What is the primary operational mechanism of a Content Delivery Network (CDN)?",
    ["To store backup copies of databases in secure cloud vaults.", "To cache static web content at geographically distributed Edge Locations close to end-users using Anycast routing.", "To replace DNS servers with direct IP connections.", "To perform server-side database querying."],
    1,
    "CDNs maintain edge proxy servers globally. Using Anycast DNS/IP routing, user requests are directed to the nearest edge node, serving cached static assets (images, videos, JS/CSS) with minimal latency and reducing origin server load."
)

add_q(
    "Hard", "Advanced Topics", ["Amazon", "Google", "Microsoft"],
    "What is the key architectural difference between a Forward Proxy and a Reverse Proxy?",
    ["A Forward Proxy protects servers; a Reverse Proxy protects network routers.", "A Forward Proxy acts on behalf of clients (hiding client identities from destination servers); a Reverse Proxy acts on behalf of servers (hiding backend server topology from clients).", "Forward proxies work at Layer 3; Reverse proxies work at Layer 2.", "There is no functional difference."],
    1,
    "A Forward Proxy sits in front of client devices to control outgoing web access and mask client IPs. A Reverse Proxy sits in front of backend origin servers to handle SSL termination, load balancing, caching, and shield server internal IPs."
)

add_q(
    "Medium", "Advanced Topics", ["Microsoft", "Amazon", "VMware"],
    "In Kubernetes and Cloud Networking, what is a Virtual IP (VIP) managed by a Service abstraction used for?",
    ["To assign MAC addresses to containers.", "To provide a stable, load-balanced single endpoint address that routes traffic to dynamic Pod instances.", "To encrypt disk storage volumes.", "To establish BGP routing between data centers."],
    1,
    "In Kubernetes, container Pods are ephemeral with dynamic IP addresses. A Service assigns a static Virtual IP (VIP) and automatically load balances traffic across healthy backend target Pods."
)

