import json

questions = []

def add_q(difficulty, topic, companyPattern, question, options, answer, explanation):
    qid = len(questions) + 1
    assert difficulty in ["Easy", "Medium", "Hard"], f"Invalid difficulty {difficulty} in Q{qid}"
    assert len(options) == 4, f"Options count must be 4 in Q{qid}"
    assert 0 <= answer <= 3, f"Answer index out of range in Q{qid}"
    assert len(explanation) >= 15, f"Explanation too short in Q{qid}"
    
    questions.append({
        "id": qid,
        "difficulty": difficulty,
        "topic": topic,
        "companyPattern": companyPattern,
        "question": str(question).strip(),
        "options": [str(opt).strip() for opt in options],
        "answer": int(answer),
        "explanation": str(explanation).strip()
    })

S1 = ["TCS", "Infosys", "Accenture"]
S2 = ["Wipro", "Cognizant", "Capgemini"]
S3 = ["LTIMindtree", "Tech Mahindra", "HCL", "Deloitte", "IBM"]
P1 = ["Amazon", "Microsoft", "Google"]
P2 = ["Meta", "Adobe", "Oracle", "SAP"]
P3 = ["ServiceNow", "Atlassian", "Goldman Sachs", "JPMorgan", "PayPal"]
P4 = ["Flipkart", "Walmart Global Tech", "Visa", "Mastercard"]
H1 = ["Cisco", "Qualcomm", "Samsung"]
H2 = ["Nvidia", "Intel", "Juniper Networks", "Arista Networks", "VMware"]

def c(*groups):
    res = []
    for g in groups:
        res.extend(g[:2])
    return list(dict.fromkeys(res))

# Load Q1-Q35
import build_all_units
questions = build_all_units.questions

# ==============================================================================
# 3. DATA LINK LAYER (25 Qs, Q36 - Q60)
# ==============================================================================
add_q("Medium", "Data Link Layer", c(P1, H1),
  "In HDLC bit stuffing, what action does the sender take when it detects five consecutive '1' bits in the user data payload?",
  ["Inverts the next bit to '0'", "Automatically inserts a '0' bit after the fifth '1'", "Stuffs an ESC character", "Appends a 16-bit CRC checksum"], 1,
  "To prevent user data from matching the HDLC frame delimiter flag (01111110, six ones), sender hardware automatically inserts (stuffs) a '0' bit after five consecutive '1's. The receiver automatically strips any '0' following five '1's.")

add_q("Hard", "Data Link Layer", c(P1, P3, H1),
  "A 1 km long 100 Mbps CSMA/CD Ethernet network has a signal propagation speed of 2 x 10^8 m/s. What is the minimum frame size required to guarantee collision detection?",
  ["100 bits", "500 bits", "1000 bits", "2000 bits"], 2,
  "For CSMA/CD collision detection, Transmission Time (Tt) >= 2 * Propagation Delay (Tp). Tp = 1000 m / (2x10^8 m/s) = 5 us. Round trip 2*Tp = 10 us. Min Frame Size = Bandwidth * 2*Tp = 100 Mbps * 10 us = 1000 bits.")

add_q("Easy", "Data Link Layer", c(S1, S2),
  "What is the standard length of an IEEE 802 MAC address and how is it structured?",
  ["32 bits formatted in dotted decimal", "48 bits (6 bytes) written in hexadecimal pairs", "64 bits written in binary", "128 bits written in hexadecimal"], 1,
  "A MAC address is a 48-bit (6-byte) physical hardware address. The first 24 bits represent the Organizationally Unique Identifier (OUI) assigned by IEEE, and the remaining 24 bits are assigned by the manufacturer.")

add_q("Medium", "Data Link Layer", c(H1, H2),
  "How does CSMA/CA differ from CSMA/CD when operating in wireless 802.11 Wi-Fi networks?",
  ["CSMA/CA instantly aborts frame transmission upon detecting a collision.", "CSMA/CA cannot detect collisions while transmitting due to RF signal attenuation, so it uses collision avoidance timers and explicit ACK acknowledgments.", "CSMA/CA relies on physical token passing ring topologies.", "CSMA/CA operates strictly at Layer 3."], 1,
  "In wireless transceivers, transmitting power blinds local receivers, preventing real-time collision detection. CSMA/CA avoids collisions by sensing media, using random backoff slots, and requiring explicit ACK frames for every transmission.")

add_q("Hard", "Data Link Layer", c(H1, P1),
  "In a Go-Back-N ARQ protocol with an m-bit sequence number, what is the maximum allowable sender window size (Ws)?",
  ["2^m", "2^m - 1", "2^(m - 1)", "2^m + 1"], 1,
  "With an m-bit sequence number, sequence numbers range from 0 to 2^m - 1. The maximum sender window size Ws must be 2^m - 1 to prevent window overlap ambiguity if ACKs are lost.")

add_q("Hard", "Data Link Layer", c(P1, P3),
  "In Selective Repeat ARQ with an m-bit sequence number, what are the maximum sender window size (Ws) and receiver window size (Wr)?",
  ["Ws = 2^m - 1, Wr = 1", "Ws = 2^(m - 1), Wr = 2^(m - 1)", "Ws = 2^m, Wr = 2^m", "Ws = 2^m - 1, Wr = 2^m - 1"], 1,
  "In Selective Repeat ARQ, sender and receiver windows are equal: Ws = Wr = 2^(m - 1). This ensures no overlap between current sequence numbers and retransmitted frame sequence numbers.")

add_q("Medium", "Data Link Layer", c(S1, S3),
  "In a 7-bit Hamming Code with single-bit error correction capability, how many parity bits are required to protect 4 data bits?",
  ["2 parity bits", "3 parity bits", "4 parity bits", "5 parity bits"], 1,
  "Using 2^p >= d + p + 1: For d = 4 data bits, if p = 3: 2^3 = 8 >= 4 + 3 + 1 = 8. So 3 parity bits are placed at bit positions 1, 2, and 4.")

add_q("Medium", "Data Link Layer", c(H1, H2),
  "What is the primary function of IEEE 802.1Q Virtual Local Area Networks (VLANs)?",
  ["To increase physical Ethernet port speeds.", "To logically segment a physical Layer 2 switch into multiple isolated broadcast domains.", "To assign IP addresses automatically to host devices.", "To route packets between distant Autonomous Systems."], 1,
  "IEEE 802.1Q VLANs allow network administrators to partition a physical switch into multiple isolated logical broadcast domains, enhancing network security and reducing broadcast traffic.")

add_q("Easy", "Data Link Layer", c(S1, S2),
  "Which error detection technique appends a polynomial remainder calculated via modulo-2 binary division to the end of a data frame?",
  ["Checksum", "Parity Bit", "Cyclic Redundancy Check (CRC)", "Hamming Distance"], 2,
  "Cyclic Redundancy Check (CRC) treats data as a binary polynomial and performs modulo-2 division by a generator polynomial (e.g., CRC-32), appending the remainder as a frame check sequence (FCS).")

add_q("Medium", "Data Link Layer", c(H1, S2),
  "What is the minimum frame size for a standard Ethernet (IEEE 802.3) frame excluding preamble?",
  ["32 bytes", "64 bytes", "128 bytes", "1518 bytes"], 1,
  "The minimum Ethernet frame length is 64 bytes (46 bytes payload + 18 bytes header/trailer). Frames smaller than 64 bytes are considered runt frames caused by collisions.")

add_q("Easy", "Data Link Layer", c(S2, S3),
  "What MAC destination address is used to broadcast a frame to all hosts on a local Ethernet segment?",
  ["00:00:00:00:00:00", "FF:FF:FF:FF:FF:FF", "127.0.0.1", "255.255.255.255"], 1,
  "FF:FF:FF:FF:FF:FF is the 48-bit Layer 2 broadcast MAC address. All network interfaces on the local LAN accept frames addressed to this destination.")

add_q("Medium", "Data Link Layer", c(H1, H2),
  "What switch mechanism prevents Layer 2 switching loops in Ethernet networks with redundant physical links?",
  ["Border Gateway Protocol (BGP)", "Spanning Tree Protocol (STP / IEEE 802.1D)", "Network Address Translation (NAT)", "Open Shortest Path First (OSPF)"], 1,
  "Spanning Tree Protocol (STP / IEEE 802.1D) detects network loops and blocks redundant physical switch ports to construct a single loop-free logical forwarding topology.")

add_q("Hard", "Data Link Layer", c(H1, H2),
  "How does a Layer 2 Switch handle an incoming unicast frame whose destination MAC address is NOT present in its MAC address table (CAM table)?",
  ["The switch drops the frame immediately.", "The switch floods the frame out of all ports except the receiving ingress port (Unknown Unicast Flooding).", "The switch sends an ICMP Destination Unreachable message.", "The switch sends an ARP request to the router."], 1,
  "When a switch receives a frame destined for an unknown unicast address, it floods the frame out of all active ports in the same VLAN except the port it arrived on (Unknown Unicast Flooding).")

add_q("Easy", "Data Link Layer", c(S1, S2),
  "What method of framing inserts an ESC (Escape) byte before any byte in the data payload that matches a control flag character?",
  ["Bit Stuffing", "Byte Stuffing (Character Stuffing)", "Physical Layer Coding Violations", "Clock Synchronization"], 1,
  "Byte Stuffing (Character Stuffing) inserts an ESC control byte before any data byte that matches the frame Flag or ESC byte itself so the receiver treats it as raw data.")

add_q("Medium", "Data Link Layer", c(H1, P1),
  "In Stop-and-Wait ARQ, if the bit rate is 1 Mbps, propagation delay is 20 ms, and frame size is 1000 bits, what is the channel utilization?",
  ["2.4%", "4.76%", "10%", "50%"], 1,
  "Frame transmission time Tt = 1000 bits / 10^6 bps = 1 ms. Round Trip Time RTT = 2 * 20 ms = 40 ms. Total time = Tt + RTT = 41 ms. Utilization U = Tt / (Tt + RTT) = 1 / 41 ≈ 0.0243 = 2.43% (or 4.76% if RTT=20ms total). Here 1 / (1 + 40) = 2.43% (option A: 2.4%).")

add_q("Hard", "Data Link Layer", c(H1, H2),
  "What is the maximum payload size (MTU) for a standard Ethernet II frame?",
  ["64 bytes", "512 bytes", "1500 bytes", "9000 bytes"], 2,
  "The standard Ethernet Maximum Transmission Unit (MTU) is 1500 bytes. Payload above 1500 bytes requires IP fragmentation unless Jumbo Frames (up to 9000 bytes) are enabled.")

add_q("Easy", "Data Link Layer", c(S1, S3),
  "In a Ethernet frame structure, what is the purpose of the 7-byte Preamble followed by the 1-byte Start Frame Delimiter (SFD)?",
  ["To carry destination MAC addresses.", "To allow receiver clock synchronization and signal start of frame timing.", "To calculate CRC error detection.", "To identify the VLAN ID tag."], 1,
  "The 7-byte Preamble (alternating 10101010 bits) and 1-byte SFD (10101011) allow physical layer receiver hardware to synchronize internal bit clocks before reading frame headers.")

add_q("Medium", "Data Link Layer", c(H1, H2),
  "What switching method reads only the first 6 bytes of an incoming frame (destination MAC) before immediately forwarding it to reduce latency?",
  ["Store-and-Forward Switching", "Cut-Through Switching", "Fragment-Free Switching", "Adaptive Switching"], 1,
  "Cut-Through switching inspects only the destination MAC address (first 6 bytes) and starts forwarding immediately, providing minimal latency but potentially forwarding corrupt frames.")

add_q("Medium", "Data Link Layer", c(H1, H2),
  "What switching method reads the first 64 bytes of a frame to ensure no collision runt frames are forwarded before switching?",
  ["Store-and-Forward", "Cut-Through", "Fragment-Free Switching", "Layer 3 Routing"], 2,
  "Fragment-Free switching reads the first 64 bytes of the frame (the minimum collision window) before forwarding to filter out collision runt frames while maintaining lower latency than Store-and-Forward.")

add_q("Easy", "Data Link Layer", c(S1, S2),
  "What switching method reads the ENTIRE frame into memory and verifies the CRC trailer before forwarding?",
  ["Store-and-Forward Switching", "Cut-Through Switching", "Fragment-Free Switching", "Fast-Forward Switching"], 0,
  "Store-and-Forward switching receives and buffers the entire frame, checks the CRC FCS trailer for errors, drops corrupt frames, and then forwards valid frames.")

add_q("Hard", "Data Link Layer", c(P1, P3),
  "What field in an IEEE 802.1Q tagged Ethernet frame specifies the VLAN ID (VID)?",
  ["EtherType field (0x0800)", "Tag Control Information (TCI) 12-bit VLAN ID field", "Preamble bit sequence", "CRC Trailer"], 1,
  "The 802.1Q header inserts a 4-byte tag into the Ethernet frame. Inside this tag, 12 bits are allocated for the VLAN ID (VID), supporting up to 4094 distinct VLANs.")

add_q("Medium", "Data Link Layer", c(S2, S3),
  "Which protocol automates the configuration of trunk links and VLAN definitions across multiple interconnected switches in a Cisco enterprise network?",
  ["VTP (VLAN Trunking Protocol)", "STP (Spanning Tree Protocol)", "LACP (Link Aggregation Control Protocol)", "CDP"], 0,
  "VLAN Trunking Protocol (VTP) propagates VLAN configurations (add, delete, rename VLANs) automatically across switches over trunk links within a management domain.")

add_q("Medium", "Data Link Layer", c(H1, H2),
  "What protocol standard (IEEE 802.3ad) allows grouping multiple physical Ethernet links into a single logical high-bandwidth trunk link (NIC Teaming / EtherChannel)?",
  ["LACP (Link Aggregation Control Protocol)", "STP", "VRRP", "BGP"], 0,
  "Link Aggregation Control Protocol (LACP / IEEE 802.3ad) combines multiple physical links into a single logical link, providing load balancing and redundancy.")

add_q("Hard", "Data Link Layer", c(P1, H1),
  "If the generator polynomial for CRC is G(x) = x^3 + x + 1 (binary 1011), how many zero bits must be appended to the message payload before performing binary modulo-2 division?",
  ["1 bit", "2 bits", "3 bits", "4 bits"], 2,
  "For a generator polynomial of degree n (here G(x) has degree 3), exactly n zero bits (3 zeros) must be appended to the message polynomial before division.")

add_q("Easy", "Data Link Layer", c(S1, S2),
  "What is a 'Runt Frame' in Ethernet networking?",
  ["A frame larger than 9000 bytes.", "A frame smaller than 64 bytes usually damaged by a collision.", "A frame with an invalid IP address.", "A frame transmitted over fiber optics."], 1,
  "A Runt Frame is an Ethernet frame smaller than the minimum required 64 bytes, typically created when a transmitting host aborts transmission due to a collision.")

print(f"Current Q count: {len(questions)}")

# ==============================================================================
# 4. NETWORK LAYER & ROUTING PROTOCOLS (25 Qs, Q61 - Q85)
# ==============================================================================
add_q("Medium", "Routing", c(H1, H2),
  "Which routing algorithm and metric are used by RIP (Routing Information Protocol)?",
  ["Link State algorithm using Bandwidth metric", "Distance Vector (Bellman-Ford) algorithm using Hop Count metric (max 15 hops)", "Path Vector algorithm using AS Path metric", "Dijkstra algorithm using Delay metric"], 1,
  "RIP is a Distance Vector routing protocol based on the Bellman-Ford algorithm. It uses Hop Count as its routing metric, with a maximum limit of 15 hops (16 is infinity/unreachable).")

add_q("Hard", "Routing", c(H1, H2, P1),
  "In distance vector routing protocols, what condition causes the 'Count-to-Infinity' problem?",
  ["Fast convergence of link states across routers.", "Routing loops where two or more routers continually increment metrics for an unreachable destination due to slow convergence.", "Excessive memory consumption in OSPF link-state databases.", "Duplicate MAC address assignments."], 1,
  "Count-to-Infinity occurs when a link fails and routers exchange outdated routing updates back and forth, slowly incrementing the metric step-by-step up to infinity before realizing the destination is unreachable.")

add_q("Medium", "Routing", c(H1, P1),
  "How does the 'Split Horizon' rule prevent routing loops in Distance Vector protocols?",
  ["It drops all IP packets with TTL = 0.", "It prevents a router from advertising a route back out the same interface from which it originally learned that route.", "It encrypts routing updates with RSA keys.", "It forces routers to recalculate shortest paths every 10 seconds."], 1,
  "Split Horizon dictates that a router must never advertise a route back out of the interface through which it originally received that route, preventing simple two-node routing loops.")

add_q("Hard", "Routing", c(H1, H2),
  "What is 'Poison Reverse' in distance vector routing?",
  ["A security attack that corrupts router ARP tables.", "An extension to Split Horizon where a router explicitly advertises a failed route back out the receiving interface with an infinite metric (e.g. 16 for RIP).", "A method to compress IP headers.", "A firewall rule that blocks ICMP packets."], 1,
  "Poison Reverse enhances Split Horizon: when a router learns a route has failed, it explicitly advertises that route back out the interface it came from with an infinite metric (cost 16), immediately breaking loops.")

add_q("Hard", "Routing", c(H1, H2, P1),
  "Which algorithm is executed by Open Shortest Path First (OSPF) to compute the shortest loop-free path to all destinations?",
  ["Bellman-Ford Algorithm", "Dijkstra's Shortest Path First (SPF) Algorithm", "Floyd-Warshall Algorithm", "Kruskal's Minimum Spanning Tree Algorithm"], 1,
  "OSPF is a Link-State routing protocol that builds a complete topology database (LSDB) and executes Dijkstra's Shortest Path First (SPF) algorithm to construct the shortest-path routing tree.")

add_q("Medium", "Routing", c(H1, H2),
  "What metric formula is used by default in Cisco OSPF to calculate interface Cost?",
  ["Cost = Hop Count", "Cost = Reference Bandwidth (100 Mbps) / Interface Bandwidth", "Cost = Delay + Load + Reliability", "Cost = Packet Loss Rate * 100"], 1,
  "OSPF metric Cost = Reference Bandwidth / Interface Bandwidth (Default Ref BW = 10^8 bps = 100 Mbps). E.g., a 10 Mbps Ethernet link has Cost = 100/10 = 10, whereas a 100 Mbps FastEthernet link has Cost = 1.")

add_q("Hard", "Routing", c(P1, P2, H1),
  "Which Border Gateway Protocol (BGP) attribute is evaluated FIRST during the path selection algorithm when multiple routes to the same destination exist on a router?",
  ["AS_Path length", "Highest Weight (Cisco proprietary) / Highest Local Preference", "Lowest MED (Multi-Exit Discriminator)", "Lowest Router ID"], 1,
  "In BGP route selection, Weight (local to router) is evaluated first. If equal, Local Preference (highest preferred across AS) is evaluated next, followed by locally originated routes, shortest AS_Path, lowest Origin, and lowest MED.")

add_q("Medium", "Routing", c(H1, H2),
  "What type of BGP peering session is established between two routers belonging to DIFFERENT Autonomous Systems (AS)?",
  ["iBGP (Internal BGP)", "eBGP (External BGP)", "OSPF Area 0", "RIPv2"], 1,
  "eBGP (External BGP) connects routers in different Autonomous Systems (AS). iBGP (Internal BGP) exchanges exterior routing information between routers within the same AS.")

add_q("Easy", "Network Layer", c(S1, S2),
  "What is the function of the Time-To-Live (TTL) field in an IPv4 header?",
  ["To measure packet latency in milliseconds.", "To limit packet lifetime and prevent infinite routing loops by decrementing by 1 at each router hop.", "To specify the encryption algorithm used.", "To define maximum transmission throughput."], 1,
  "The 8-bit TTL field in IPv4 (Hop Limit in IPv6) is decremented by 1 by every router that forwards the packet. If TTL reaches 0, the packet is discarded and an ICMP Time Exceeded message is sent back.")

add_q("Medium", "Network Layer", c(P1, H1),
  "If an IP packet of 4000 bytes enters a router interface with an MTU of 1500 bytes, what action does the router take if the Don't Fragment (DF) bit is set to 1?",
  ["The router fragments the packet into 3 smaller packets.", "The router drops the packet and sends an ICMP Destination Unreachable (Fragmentation Needed) error back to the source.", "The router compresses the payload.", "The router overrides the MTU limit."], 1,
  "If a packet exceeds interface MTU and the DF (Don't Fragment) bit is 1, the router cannot fragment it and must drop it, returning an ICMP Type 3 Code 4 (Fragmentation Needed) packet to the sender (used in Path MTU Discovery).")

add_q("Hard", "Network Layer", c(H1, P1),
  "In IPv4 header fragmentation, how is the Fragment Offset value calculated for a fragment carrying payload starting at byte 1480?",
  ["1480", "740", "185", "370"], 2,
  "The IPv4 Fragment Offset field measures offset in 8-byte (64-bit) blocks. Offset = Payload Byte Start / 8 = 1480 / 8 = 185.")

add_q("Easy", "Network Layer", c(S1, S2),
  "What is the standard length of an IPv4 header without optional fields?",
  ["10 bytes", "20 bytes", "32 bytes", "40 bytes"], 1,
  "The minimum IPv4 header length is 20 bytes (5 words of 32 bits, indicated by IHL = 5). Options can extend it up to 60 bytes.")

add_q("Medium", "Network Layer", c(H1, H2),
  "What is the fixed header size of an IPv6 packet?",
  ["20 bytes", "32 bytes", "40 bytes", "64 bytes"], 2,
  "IPv6 features a streamlined fixed-length header of 40 bytes (320 bits), eliminating variable option processing overhead at intermediate routers for faster hardware routing.")

add_q("Medium", "Network Layer", c(H1, P1),
  "Which field in the IPv6 base header replaces the IPv4 'Time-To-Live (TTL)' field?",
  ["Flow Label", "Next Header", "Hop Limit", "Traffic Class"], 2,
  "In IPv6, the 'Hop Limit' field replaces IPv4's TTL field, serving the exact same loop prevention purpose by decrementing at each router hop.")

add_q("Easy", "Network Layer", c(S2, S3),
  "Which field in the IPv6 header replaces the IPv4 'Protocol' field to indicate upper layer protocols or extension headers?",
  ["Payload Length", "Next Header", "Flow Label", "Traffic Class"], 1,
  "The 8-bit 'Next Header' field in IPv6 specifies either the upper-layer transport protocol (e.g. 6 for TCP, 17 for UDP) or an IPv6 Extension Header in a daisy-chain structure.")

add_q("Hard", "Routing", c(H1, H2),
  "What routing protocol uses Administrative Distance (AD) value 90 in Cisco systems?",
  ["OSPF", "EIGRP (Internal)", "RIP", "eBGP"], 1,
  "Administrative Distance (AD) ranks routing protocol trustworthiness. Cisco AD values: Connected = 0, Static = 1, eBGP = 20, EIGRP (Internal) = 90, OSPF = 110, RIP = 120, iBGP = 200.")

add_q("Easy", "Routing", c(S1, S2),
  "What Administrative Distance (AD) value is assigned to a directly connected network interface?",
  ["0", "1", "10", "110"], 0,
  "Directly connected interfaces have the most trusted Administrative Distance of 0. Static routes default to AD = 1.")

add_q("Medium", "Routing", c(H1, H2),
  "In OSPF, what is the role of Area 0?",
  ["It is a stub area reserved for dial-up links.", "It is the mandatory Backbone Area to which all other non-backbone areas must connect for inter-area routing.", "It is reserved exclusively for IPv6 routing.", "It handles BGP route redistribution."], 1,
  "OSPF Area 0 (0.0.0.0) is the core Backbone Area. All other OSPF areas (Area 1, Area 2, etc.) must connect to Area 0 directly or via virtual links to prevent inter-area routing loops.")

add_q("Hard", "Routing", c(H1, H2),
  "What OSPF router role is assigned to a router that has interfaces attached to both Area 0 and a non-backbone Area 1?",
  ["Internal Router (IR)", "Area Border Router (ABR)", "Autonomous System Boundary Router (ASBR)", "Designated Router (DR)"], 1,
  "An Area Border Router (ABR) attaches to multiple OSPF areas, maintaining a separate LSDB topology map for each area and summarizing routes between Area 0 and non-backbone areas.")

add_q("Hard", "Routing", c(H1, H2),
  "What OSPF router role is assigned to a router that redistributes routes learned from an external routing protocol (e.g., BGP or RIP) into OSPF?",
  ["ABR", "ASBR (Autonomous System Boundary Router)", "DR", "BDR"], 1,
  "An Autonomous System Boundary Router (ASBR) sits at the edge of an OSPF domain and redistributes external routes (from BGP, RIP, static, etc.) into the OSPF network using Type 5 LSAs.")

add_q("Medium", "Routing", c(H1, H2),
  "Why do OSPF routers elect a Designated Router (DR) and Backup Designated Router (BDR) on a multiaccess broadcast network (like Ethernet)?",
  ["To assign IP addresses to hosts.", "To reduce the number of OSPF adjacency relationships from N(N-1)/2 to 2N and limit LSA flooding overhead.", "To encrypt routing updates.", "To replace default gateways."], 1,
  "On broadcast multiaccess networks, electing a DR and BDR reduces required adjacencies from N(N-1)/2 to 2N, requiring routers to form full adjacencies only with the DR/BDR to minimize LSA exchange traffic.")

add_q("Easy", "Routing", c(S1, S2),
  "Which multicast IP address is used by OSPF to send hello packets to All OSPF Routers?",
  ["224.0.0.1", "224.0.0.5", "224.0.0.6", "224.0.0.9"], 1,
  "OSPF uses IPv4 multicast address 224.0.0.5 (AllSPFRouters) for general hello packets and 224.0.0.6 (AllDRouters) to send updates to DR/BDR routers.")

add_q("Hard", "Routing", c(P1, P2),
  "What path vector mechanism does BGP use to prevent routing loops between Autonomous Systems?",
  ["Decrementing TTL at each hop.", "Inspecting the AS_PATH attribute; if a router sees its own local AS number in the AS_PATH, it rejects the route.", "Calculating Dijkstra shortest path.", "Using Split Horizon."], 1,
  "BGP loop prevention: Every router prepends its AS number to the AS_PATH attribute when advertising routes to eBGP peers. If a router receives an update containing its own AS number in AS_PATH, it drops the route.")

add_q("Medium", "Network Layer", c(S2, P4),
  "What is the difference between Connection-Oriented Packet Switching (Virtual Circuit) and Connectionless Packet Switching (Datagram)?",
  ["Datagram networks reserve bandwidth along a pre-established route; Virtual Circuits route each packet independently.", "Virtual Circuit networks establish a dedicated logical path before transmitting data; Datagram networks route each packet independently using destination IP addresses.", "Datagram networks work only at Layer 1; Virtual Circuits work at Layer 7.", "There is no difference."], 1,
  "Virtual Circuit networks (e.g., Frame Relay, ATM, MPLS) establish a logical path (VC ID) before data transfer. Datagram networks (e.g., standard IP) route each packet independently based on IP address lookups.")

add_q("Easy", "Network Layer", c(S1, S3),
  "What protocol translates private IP addresses to a public IP address using dynamic source port numbers (PAT)?",
  ["ARP", "NAT / PAT (Port Address Translation)", "DHCP", "DNS"], 1,
  "Port Address Translation (PAT / Overloaded NAT) maps thousands of private IP addresses to a single public IP address by assigning unique source TCP/UDP port numbers to outgoing connections.")

print(f"Current Q count: {len(questions)}")

# ==============================================================================
# 5. IP ADDRESSING, SUBNETTING, CIDR & VLSM (35 Qs, Q86 - Q120)
# ==============================================================================
add_q("Medium", "IP Addressing", c(S1, S2, P4),
  "What is the subnet mask and total number of usable host IP addresses for a network with CIDR notation 192.168.10.0/26?",
  ["255.255.255.128, 126 hosts", "255.255.255.192, 62 hosts", "255.255.255.224, 30 hosts", "255.255.255.240, 14 hosts"], 1,
  "A /26 prefix has 26 subnet bits (11111111.11111111.11111111.11000000 = 255.255.255.192). Host bits h = 32 - 26 = 6. Total IPs = 2^6 = 64. Usable hosts = 64 - 2 = 62 hosts.")

add_q("Hard", "IP Addressing", c(P1, P3, H1),
  "An enterprise is assigned IP block 172.16.0.0/16 and must construct subnets that support at least 500 hosts per subnet. What is the maximum number of such subnets that can be created?",
  ["64 subnets", "128 subnets", "256 subnets", "512 subnets"], 1,
  "To support 500 hosts: 2^h - 2 >= 500 => h = 9 bits for hosts (2^9 = 512). Prefix length = 32 - 9 = /23. Original prefix was /16. Subnet bits borrowed = 23 - 16 = 7 bits. Number of subnets = 2^7 = 128 subnets.")

add_q("Easy", "IP Addressing", c(S1, S2),
  "Which of the following IP address ranges is designated as RFC 1918 Private IP address space?",
  ["11.0.0.0 to 11.255.255.255", "172.16.0.0 to 172.31.255.255", "192.168.0.0 to 192.169.255.255", "169.254.0.0 to 169.254.255.255"], 1,
  "RFC 1918 private ranges: Class A: 10.0.0.0/8, Class B: 172.16.0.0/12 (172.16.0.0 - 172.31.255.255), Class C: 192.168.0.0/16 (192.168.0.0 - 192.168.255.255).")

add_q("Medium", "IP Addressing", c(H1, P1),
  "What are the network address and broadcast address for a host with IP 10.1.50.75 and subnet mask 255.255.240.0 (/20)?",
  ["Network: 10.1.48.0, Broadcast: 10.1.63.255", "Network: 10.1.32.0, Broadcast: 10.1.47.255", "Network: 10.1.50.0, Broadcast: 10.1.50.255", "Network: 10.1.0.0, Broadcast: 10.1.255.255"], 0,
  "Mask 255.255.240.0 has block size 256 - 240 = 16 in 3rd octet. Multiples of 16 are 0, 16, 32, 48, 64. IP 10.1.50.75 falls in subnet 10.1.48.0/20 with range 10.1.48.0 to 10.1.63.255.")

add_q("Easy", "IP Addressing", c(S1, S3),
  "If a host cannot reach a DHCP server, Windows automatically assigns an IP from 169.254.x.x. What is this address known as?",
  ["Loopback Address", "APIPA (Automatic Private IP Addressing)", "Multicast Address", "Default Gateway"], 1,
  "APIPA (Automatic Private IP Addressing) automatically assigns a link-local IPv4 address in the 169.254.0.0/16 block when DHCP resolution fails.")

add_q("Hard", "IP Addressing", c(H1, P1),
  "A point-to-point router link requires only 2 usable host IP addresses. What is the optimal CIDR subnet mask prefix to conserve address space?",
  ["/28", "/29", "/30", "/32"], 2,
  "A /30 subnet mask (255.255.255.252) provides 2^2 = 4 total IP addresses: 1 network ID, 1 broadcast ID, and exactly 2 usable host IPs, ideal for point-to-point serial links. (/31 is RFC 3021 for point-to-point, but /30 is traditional standard).")

add_q("Medium", "IP Addressing", c(S2, S3),
  "What is the first usable host IP address in the subnet 192.168.1.128/28?",
  ["192.168.1.128", "192.168.1.129", "192.168.1.130", "192.168.1.143"], 1,
  "Subnet 192.168.1.128/28 has Network ID = 192.168.1.128. First usable host = Network ID + 1 = 192.168.1.129. Broadcast ID = 192.168.1.143.")

add_q("Medium", "IP Addressing", c(S1, P4),
  "What is the broadcast IP address for the subnet containing host IP 172.16.35.10 with subnet mask 255.255.248.0 (/21)?",
  ["172.16.35.255", "172.16.39.255", "172.16.47.255", "172.16.31.255"], 1,
  "Mask 255.255.248.0 has block size 256 - 248 = 8 in 3rd octet. Multiples of 8: 0, 8, 16, 24, 32, 40... Host 172.16.35.10 lies in subnet 172.16.32.0. Broadcast ID = 172.16.39.255.")

add_q("Easy", "IP Addressing", c(S1, S2),
  "What Class of IPv4 addresses is reserved for IP Multicasting (e.g. 224.0.0.0 to 239.255.255.255)?",
  ["Class A", "Class B", "Class C", "Class D"], 3,
  "Class D IPv4 addresses (range 224.0.0.0 to 239.255.255.255) are reserved for IP multicast traffic. Class E (240.0.0.0 to 255.255.255.255) is reserved for experimental use.")

add_q("Easy", "IP Addressing", c(S2, S3),
  "What default subnet mask is associated with a Class B IPv4 network?",
  ["255.0.0.0", "255.255.0.0", "255.255.255.0", "255.255.255.240"], 1,
  "Class A default mask = 255.0.0.0 (/8); Class B default mask = 255.255.0.0 (/16); Class C default mask = 255.255.255.0 (/24).")

add_q("Hard", "IP Addressing", c(P1, P3, H1),
  "Supernetting (Route Aggregation) summarizes four Class C networks: 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, and 192.168.3.0/24 into a single CIDR route. What is the summarized route?",
  ["192.168.0.0/22", "192.168.0.0/23", "192.168.0.0/21", "192.168.1.0/22"], 0,
  "The 3rd octets in binary are: 0 (00000000), 1 (00000001), 2 (00000010), 3 (00000011). The first 6 bits of 3rd octet match (000000). Total matching prefix bits = 8 + 8 + 6 = 22 bits. Summarized route = 192.168.0.0/22.")

add_q("Medium", "IP Addressing", c(S1, P4),
  "What is the IPv4 Loopback IP address used by a host to send packets back to its own local TCP/IP protocol stack?",
  ["0.0.0.0", "127.0.0.1", "192.168.1.1", "255.255.255.255"], 1,
  "127.0.0.1 (or any address in 127.0.0.0/8 block) is the IPv4 loopback address used for internal testing without sending traffic onto physical network cards.")

add_q("Medium", "IP Addressing", c(H1, H2),
  "What is the IPv6 equivalent of the IPv4 Loopback address 127.0.0.1?",
  ["::0", "::1", "fe80::1", "ff02::1"], 1,
  "In IPv6, the loopback address is written as ::1 (127 zero bits followed by a single 1 bit).")

add_q("Easy", "IP Addressing", c(S1, S2),
  "Which IPv6 address scope is automatically configured on every IPv6-enabled interface and begins with the prefix fe80::/10?",
  ["Global Unicast Address", "Link-Local Address", "Unique Local Address", "Multicast Address"], 1,
  "Link-Local IPv6 addresses (fe80::/10) are automatically assigned to every IPv6 interface for local communication on the same link segment, analogous to IPv4 APIPA.")

add_q("Medium", "IP Addressing", c(H1, P1),
  "Variable Length Subnet Masking (VLSM) allows network engineers to:",
  ["Convert IPv4 addresses into IPv6 addresses automatically.", "Subnet a network space into subnets of unequal sizes to prevent IP address wastage.", "Encrypt IP packet headers.", "Assign static MAC addresses."], 1,
  "VLSM (Variable Length Subnet Masking) enables dividing IP address blocks into subnets of varying prefix lengths (/24, /28, /30) tailored to host counts, maximizing address space efficiency.")

add_q("Hard", "IP Addressing", c(P1, P3),
  "A company has subnet 10.20.0.0/22. How many total IP addresses (including network and broadcast) are contained within this CIDR block?",
  ["256", "512", "1024", "2048"], 2,
  "Host bits h = 32 - 22 = 10. Total IP addresses = 2^10 = 1024 IPs. (Usable host IPs = 1024 - 2 = 1022).")

add_q("Medium", "IP Addressing", c(S2, S3),
  "What is the network ID of host IP 192.168.5.200/27?",
  ["192.168.5.128", "192.168.5.192", "192.168.5.224", "192.168.5.0"], 1,
  "/27 has block size 256 - 224 = 32 in 4th octet. Multiples of 32: 0, 32, 64, 96, 128, 160, 192, 224. Host .200 falls between 192 and 223. Network ID = 192.168.5.192.")

add_q("Hard", "IP Addressing", c(H1, P1),
  "How many usable subnets and host IPs per subnet are obtained if network 192.168.1.0/24 is subnetted using a /29 mask?",
  ["8 subnets, 6 hosts per subnet", "32 subnets, 6 hosts per subnet", "16 subnets, 14 hosts per subnet", "8 subnets, 30 hosts per subnet"], 1,
  "Original prefix /24, new prefix /29. Subnet bits borrowed = 29 - 24 = 5 bits. Subnets = 2^5 = 32 subnets. Host bits = 32 - 29 = 3 bits. Usable hosts per subnet = 2^3 - 2 = 6 hosts.")

add_q("Easy", "IP Addressing", c(S1, S2),
  "Which field in the IPv4 address indicates whether an IP belongs to Class A, Class B, or Class C under classful addressing?",
  ["The leading high-order bits of the first octet.", "The last octet bits.", "The subnet mask length.", "The TTL value."], 0,
  "Classful addressing inspects leading bits of first octet: Class A starts with 0 (1-126), Class B starts with 10 (128-191), Class C starts with 110 (192-223).")

add_q("Medium", "IP Addressing", c(S1, P4),
  "What is the broadcast IP address of network 10.0.0.0/13?",
  ["10.0.255.255", "10.7.255.255", "10.15.255.255", "10.255.255.255"], 1,
  "/13 prefix has mask 255.248.0.0. Block size in 2nd octet = 256 - 248 = 8. Multiples: 0, 8, 16... Network 10.0.0.0/13 ranges from 10.0.0.0 to 10.7.255.255. Broadcast ID = 10.7.255.255.")

add_q("Hard", "IP Addressing", c(P1, P2),
  "What IPv6 address compression rule allows replacing consecutive sections of zero words with '::'?",
  ["Zero Compression can be applied multiple times per address.", "Zero Compression can be applied ONLY ONCE per IPv6 address to prevent ambiguous expansion.", "Leading zeros within a 16-bit hex group cannot be omitted.", "Colons are replaced with periods."], 1,
  "Zero compression ('::') can be used only ONCE in an IPv6 address string. Multiple '::' usages would create ambiguity regarding how many zero groups belong to each section.")

add_q("Easy", "IP Addressing", c(S1, S3),
  "Which IPv6 prefix defines Unique Local Addresses (ULA), equivalent to IPv4 RFC 1918 private IP addresses?",
  ["2001::/16", "fe80::/10", "fc00::/7 (or fd00::/8)", "ff00::/8"], 2,
  "Unique Local IPv6 Addresses (fc00::/7, commonly fd00::/8) are intended for local communication inside a site, non-routable on the public global Internet.")

add_q("Medium", "IP Addressing", c(S2, S3),
  "If a host has IP 192.168.1.50 and subnet mask 255.255.255.240 (/28), what is the valid usable host range for this subnet?",
  ["192.168.1.48 to 192.168.1.63", "192.168.1.49 to 192.168.1.62", "192.168.1.33 to 192.168.1.46", "192.168.1.1 to 192.168.1.254"], 1,
  "Block size for /28 is 16. Subnets: 0, 16, 32, 48, 64. Host .50 belongs to subnet 192.168.1.48/28. Network ID = .48, Broadcast ID = .63. Usable host range = 192.168.1.49 to 192.168.1.62.")

add_q("Medium", "IP Addressing", c(P1, P4),
  "What is the wildcard mask used in OSPF ACL configurations for a /27 subnet mask (255.255.255.224)?",
  ["0.0.0.31", "0.0.0.63", "0.0.0.15", "0.0.0.255"], 0,
  "Wildcard Mask = 255.255.255.255 - Subnet Mask. 255.255.255.255 - 255.255.255.224 = 0.0.0.31.")

add_q("Hard", "IP Addressing", c(P1, P3),
  "An ISP aggregates four /24 routes: 203.0.112.0/24, 203.0.113.0/24, 203.0.114.0/24, 203.0.115.0/24. What single CIDR supernet block represents all four?",
  ["203.0.112.0/22", "203.0.112.0/23", "203.0.112.0/21", "203.0.114.0/22"], 0,
  "3rd octets in binary: 112 (01110000), 113 (01110001), 114 (01110010), 115 (01110011). Common bits = 6 bits. Total prefix = 8 + 8 + 6 = 22. Summarized route = 203.0.112.0/22.")

add_q("Easy", "IP Addressing", c(S1, S2),
  "What IPv4 address 0.0.0.0 represents in routing tables?",
  ["Loopback interface", "Default Route / Any Network", "Limited Broadcast", "APIPA address"], 1,
  "0.0.0.0/0 represents the Default Route (quad-zero route) in routing tables, used to forward traffic destined for networks not explicitly matched by any specific route.")

add_q("Medium", "IP Addressing", c(S2, S3),
  "What is the limited broadcast IP address used by a host that does not yet know its IP address to send a local broadcast?",
  ["0.0.0.0", "127.0.0.1", "255.255.255.255", "192.168.255.255"], 2,
  "255.255.255.255 is the Layer 3 Limited Broadcast address. Packets sent to this destination are delivered to all hosts on the local network segment but dropped by routers.")

add_q("Hard", "IP Addressing", c(H1, P1),
  "How many host IP addresses are usable in a CIDR network block /23?",
  ["254", "510", "512", "1022"], 1,
  "Host bits h = 32 - 23 = 9. Total IPs = 2^9 = 512. Usable host IPs = 512 - 2 = 510 hosts.")

add_q("Easy", "IP Addressing", c(S1, S3),
  "Which RFC defines NAT (Network Address Translation) and Private IP space allocation?",
  ["RFC 791", "RFC 1918", "RFC 2616", "RFC 3550"], 1,
  "RFC 1918 (Address Allocation for Private Internets) defines private IPv4 address blocks for Class A, B, and C networks.")

add_q("Medium", "IP Addressing", c(S1, P4),
  "What IP address range is designated for Class E addresses?",
  ["192.0.0.0 to 223.255.255.255", "224.0.0.0 to 239.255.255.255", "240.0.0.0 to 255.255.255.254", "128.0.0.0 to 191.255.255.255"], 2,
  "Class E IPv4 addresses span from 240.0.0.0 to 255.255.255.254 (first 4 bits 1111) and are reserved for experimental and research purposes.")

add_q("Hard", "IP Addressing", c(H1, P1),
  "What is EUI-64 in IPv6 host address auto-configuration?",
  ["A method to hash IPv6 passwords.", "A technique that converts a 48-bit MAC address into a 64-bit Interface Identifier by inserting 0xFFFE in the middle and flipping the 7th bit.", "A 64-bit encryption key used in WPA2.", "A routing metric used in BGP."], 1,
  "EUI-64 formats a 64-bit IPv6 interface ID from a 48-bit MAC address by inserting 16-bit 'FF:FE' in the middle and flipping the Universal/Local (U/L) 7th bit.")

add_q("Easy", "IP Addressing", c(S1, S2),
  "What is the CIDR prefix length for a subnet mask of 255.255.255.248?",
  ["/27", "/28", "/29", "/30"], 2,
  "255.255.255.248 has 24 + 5 = 29 ones (11111000 in last octet), corresponding to CIDR notation /29.")

add_q("Medium", "IP Addressing", c(S2, S3),
  "If host A (10.1.1.5/24) sends a packet to host B (10.1.2.5/24), how does host A know host B is on a DIFFERENT subnet?",
  ["By checking host B's MAC address.", "By performing a bitwise AND operation on host B's IP with host A's subnet mask and comparing it to host A's network ID.", "By broadcasting an ARP request.", "By querying a DNS root server."], 1,
  "Host A performs bitwise AND between destination IP 10.1.2.5 and its own subnet mask 255.255.255.0 resulting in 10.1.2.0. Since 10.1.2.0 != 10.1.1.0, Host A knows destination is off-subnet and routes to default gateway.")

add_q("Hard", "IP Addressing", c(P1, P3),
  "What is the maximum number of hosts supported in a network with mask 255.255.240.0?",
  ["2046", "4094", "4096", "8190"], 1,
  "Mask 255.255.240.0 is /20. Host bits = 32 - 20 = 12. Usable hosts = 2^12 - 2 = 4096 - 2 = 4094 hosts.")

add_q("Easy", "IP Addressing", c(S1, S2),
  "Which device modifies source IP addresses in packet headers during SNAT (Source Network Address Translation)?",
  ["Layer 2 Switch", "NAT Router / Firewall", "DNS Server", "Hub"], 1,
  "A NAT-enabled Router or Firewall modifies the source IP address in IP packet headers when forwarding outgoing traffic from private internal networks to public networks.")

print(f"Current Q count: {len(questions)}")

# ==============================================================================
# 6. ADDRESS RESOLUTION & HELPER PROTOCOLS (20 Qs, Q121 - Q140)
# ==============================================================================
add_q("Medium", "ARP", c(S1, P1),
  "Host A wants to send a packet to Host B on the local subnet. Host A checks its ARP cache and finds no entry for Host B. What frame sequence follows?",
  ["Host A sends an ARP Request via Layer 2 Broadcast (FF:FF:FF:FF:FF:FF); Host B responds with an ARP Reply via Unicast.", "Host A sends an ARP Request via Unicast; Host B responds via Broadcast.", "Host A sends a DHCP Request to the router.", "Host A sends an ICMP Echo Request to the default gateway."], 0,
  "Host A broadcasts an ARP Request (destination MAC FF:FF:FF:FF:FF:FF) asking 'Who has Host B's IP?'. Host B receives the broadcast and replies directly to Host A via unicast ARP Reply containing its MAC address.")

add_q("Medium", "ARP", c(H1, H2),
  "What is a 'Gratuitous ARP' message used for in enterprise networks?",
  ["To request an IP address from a DHCP server.", "An unprompted ARP announcement sent by a host to announce its IP-to-MAC mapping or update neighbor ARP caches after an IP/Failover change.", "To resolve domain names to IP addresses.", "To terminate a TCP connection."], 1,
  "Gratuitous ARP is an unsolicited ARP Request/Reply broadcast by a host to inform the LAN of its IP-to-MAC binding, commonly used to update switches/hosts during high-availability cluster failovers or IP address changes.")

add_q("Hard", "ARP", c(H1, H2),
  "How does Proxy ARP function on a router interface?",
  ["The router blocks all ARP broadcasts.", "The router responds to ARP requests on behalf of remote target hosts located on a different subnet, supplying its own interface MAC address.", "The router translates IPv4 addresses to IPv6 addresses.", "The router encrypts ARP packets."], 1,
  "Proxy ARP enables a router to answer ARP requests for destination IPs that are not on the local subnet. The router supplies its own interface MAC address, pretending to be the target host so traffic is routed through it.")

add_q("Easy", "ICMP", c(S1, S2),
  "What transport layer protocol and IP protocol number are used by ICMP (Internet Control Message Protocol)?",
  ["TCP; Protocol 6", "UDP; Protocol 17", "None (ICMP is encapsulated directly inside IP packets with Protocol 1)", "Ethernet; Protocol 0"], 2,
  "ICMP does not use TCP or UDP. ICMP messages are encapsulated directly within IPv4 datagrams with IP Protocol number field set to 1.")

add_q("Medium", "ICMP", c(S1, S3),
  "What ICMP Type and Code are returned when a router drops an IP packet because its Time-To-Live (TTL) expired at 0?",
  ["ICMP Type 0, Code 0 (Echo Reply)", "ICMP Type 8, Code 0 (Echo Request)", "ICMP Type 11, Code 0 (Time Exceeded)", "ICMP Type 3, Code 3 (Port Unreachable)"], 2,
  "When a router decrements an IP packet's TTL to 0, it drops the packet and sends an ICMP Type 11 Code 0 (Time Exceeded) error message back to the source address.")

add_q("Hard", "ICMP", c(P1, H1),
  "How does the Linux 'traceroute' utility determine intermediate router IPs along a path?",
  ["By sending ICMP Echo Requests with fixed TTL = 64.", "By sending UDP/ICMP probes with incrementally increasing TTL values starting at 1, capturing ICMP Time Exceeded (Type 11) replies from each hop router.", "By querying DNS root servers.", "By inspecting BGP routing tables."], 1,
  "Traceroute sends probe packets (UDP or ICMP) starting with TTL = 1. Each successive hop decrements TTL to 0, drops the packet, and sends back an ICMP Time Exceeded (Type 11) message, revealing that router's IP.")

add_q("Easy", "DHCP", c(S1, S2),
  "What is the standard 4-step message sequence for acquiring a dynamic IP address lease from a DHCP server?",
  ["DORA: Discover -> Offer -> Request -> Acknowledge", "ROAD: Request -> Offer -> Acknowledge -> Discover", "AROD: Acknowledge -> Request -> Offer -> Discover", "DATA: Discover -> Accept -> Transfer -> Ack"], 0,
  "DHCP lease sequence follows DORA: 1. DHCP Discover (Client broadcast), 2. DHCP Offer (Server unicast/broadcast), 3. DHCP Request (Client broadcast acceptance), 4. DHCP Acknowledgment (Server confirmation).")

add_q("Medium", "DHCP", c(S1, S2),
  "What UDP port numbers are used by DHCP clients and DHCP servers?",
  ["Client: 53, Server: 53", "Client: 68, Server: 67", "Client: 80, Server: 443", "Client: 161, Server: 162"], 1,
  "DHCP operates over UDP: DHCP Server listens on UDP Port 67, and DHCP Client listens on UDP Port 68.")

add_q("Hard", "DHCP", c(H1, H2),
  "How does a DHCP Relay Agent assist clients located on a subnet without a local DHCP server?",
  ["It acts as a secondary DHCP server.", "It intercepts Layer 2 broadcast DHCP Discover frames and forwards them as Layer 3 unicast IP packets to a remote DHCP server.", "It assigns static IP addresses stored in RAM.", "It drops all DHCP requests."], 1,
  "Because routers drop Layer 2 broadcasts, a DHCP Relay Agent (ip helper-address) receives client DHCP broadcasts, converts them into unicast IP packets, and forwards them across routers to a centralized remote DHCP server.")

add_q("Medium", "NDP", c(H1, H2),
  "What IPv6 protocol suite replaces IPv4 ARP and ICMP Router Discovery?",
  ["RARP", "Neighbor Discovery Protocol (NDP / ICMPv6)", "DHCPv4", "IGMP"], 1,
  "IPv6 Neighbor Discovery Protocol (NDP), built on ICMPv6, replaces ARP and router discovery using Neighbor Solicitation (NS) and Neighbor Advertisement (NA) multicast messages.")

add_q("Easy", "ICMP", c(S1, S2),
  "Which command line tool sends ICMP Echo Request (Type 8) messages to test basic IP connectivity?",
  ["traceroute", "ping", "netstat", "nslookup"], 1,
  "The 'ping' utility sends ICMP Echo Request (Type 8, Code 0) packets to a target host and listens for ICMP Echo Reply (Type 0, Code 0) responses.")

add_q("Medium", "ICMP", c(S2, S3),
  "What ICMP message type and code are returned when a host attempts to connect to a closed UDP port on a reachable server?",
  ["Type 0, Code 0", "Type 3, Code 3 (Destination Unreachable: Port Unreachable)", "Type 11, Code 0", "Type 5, Code 0"], 1,
  "When a packet reaches a target server but no application is listening on the destination UDP port, the operating system responds with ICMP Type 3 Code 3 (Port Unreachable).")

add_q("Hard", "ARP", c(P1, P3),
  "What network attack occurs when an attacker sends fake ARP responses to poison neighbor ARP tables and intercept local LAN traffic?",
  ["DNS Poisoning", "ARP Spoofing / Poisoning (Man-in-the-Middle)", "SYN Flood", "Buffer Overflow"], 1,
  "ARP Spoofing involves broadcasting forged ARP replies mapping a legitimate gateway IP to the attacker's MAC address, allowing the attacker to intercept, inspect, or modify LAN traffic (MitM attack).")

add_q("Easy", "RARP", c(S1, S2),
  "What historical protocol was used by diskless workstations to request their IP address given their hardware MAC address before DHCP existed?",
  ["ARP", "RARP (Reverse Address Resolution Protocol)", "ICMP", "IGMP"], 1,
  "Reverse ARP (RARP) allowed a host to broadcast its MAC address to request its IP address from a RARP server. RARP was later superseded by BOOTP and DHCP.")

add_q("Medium", "DHCP", c(S1, S3),
  "When a DHCP client reaches 50% of its lease time (T1 timer), what action does it take?",
  ["It drops its IP address immediately.", "It sends a unicast DHCP Request to the issuing DHCP server to renew its lease.", "It broadcasts a DHCP Discover frame.", "It restarts the computer."], 1,
  "At 50% of the lease duration (T1 timer), the DHCP client sends a unicast DHCP REQUEST to the issuing server to extend its lease. If no reply, at 87.5% (T2 timer) it broadcasts to any available DHCP server.")

add_q("Hard", "ICMP", c(H1, H2),
  "What ICMP message type is used by a router to inform a host of a more optimal gateway router for a specific destination network?",
  ["ICMP Type 3 (Unreachable)", "ICMP Type 5 (Redirect)", "ICMP Type 8 (Echo)", "ICMP Type 12 (Parameter Problem)"], 1,
  "ICMP Redirect (Type 5) is sent by a router to inform a sending host that a better first-hop router exists on the local link for a given destination.")

add_q("Easy", "DHCP", c(S1, S2),
  "Is a DHCP Discover packet sent as a Unicast, Multicast, or Broadcast frame?",
  ["Unicast", "Multicast", "Broadcast (Destination IP 255.255.255.255, MAC FF:FF:FF:FF:FF:FF)", "Anycast"], 2,
  "A client initializing with no IP address sends DHCP Discover as a Layer 3 Broadcast (255.255.255.255) and Layer 2 Broadcast (FF:FF:FF:FF:FF:FF).")

add_q("Medium", "NDP", c(H1, H2),
  "What ICMPv6 message type is broadcast by an IPv6 host to determine the link-layer MAC address of a neighbor?",
  ["Router Advertisement (RA)", "Neighbor Solicitation (NS)", "Neighbor Advertisement (NA)", "Router Solicitation (RS)"], 1,
  "In IPv6 NDP, Neighbor Solicitation (NS - ICMPv6 Type 135) sent to a Solicited-Node Multicast address replaces IPv4 ARP requests to request a neighbor's MAC address.")

add_q("Medium", "DHCP", c(S2, S3),
  "What DHCP message is sent by a client to explicitly notify the DHCP server that it is releasing its IP address lease?",
  ["DHCP Decline", "DHCP Release", "DHCP Inform", "DHCP NACK"], 1,
  "DHCP Release is sent unicast by a client to the DHCP server when it gracefully disconnects or unbinds its IP address lease before lease expiration.")

add_q("Hard", "DHCP", c(H1, P1),
  "What security feature on Layer 2 switches filters rogue DHCP server responses by designating switch ports as Trusted or Untrusted?",
  ["Dynamic ARP Inspection (DAI)", "DHCP Snooping", "Port Security", "BPDU Guard"], 1,
  "DHCP Snooping is a Layer 2 security mechanism that intercepts DHCP messages, drops DHCP Offers from untrusted ports, and builds a binding database of IP-to-MAC-to-Port mappings.")


# ==============================================================================
# 7. TRANSPORT LAYER (30 Qs, Q141 - Q170)
# ==============================================================================
add_q("Medium", "TCP", c(S1, P1),
  "What sequence of flags is exchanged during the standard TCP 3-Way Handshake connection setup phase?",
  ["SYN -> SYN-ACK -> ACK", "SYN -> ACK -> FIN", "PSH -> SYN-ACK -> ACK", "SYN -> FIN-ACK -> ACK"], 0,
  "TCP Handshake: 1. Client sends SYN (specifying ISN). 2. Server responds with SYN-ACK (acknowledging client ISN and specifying server ISN). 3. Client sends ACK. Connection enters ESTABLISHED state.")

add_q("Hard", "TCP", c(P1, P2, H1),
  "During TCP graceful termination (4-Way Handshake), why does the active closing host enter the TIME_WAIT state for 2 * MSL (Maximum Segment Lifetime)?",
  ["To wait for DNS update responses.", "To ensure the remote peer received the final ACK and to allow any delayed duplicate segments in the network to expire.", "To retransmit unacknowledged data payloads.", "To measure round-trip time."], 1,
  "TIME_WAIT (2 * MSL, typically 1-2 minutes) ensures: 1. If final ACK is lost, the peer's retransmitted FIN can be answered with ACK. 2. Any old delayed packets expire in the network so they don't corrupt future sockets.")

add_q("Medium", "TCP", c(H1, H2),
  "In TCP Flow Control, what does the 'Receiver Window' (rwnd) field advertised in TCP ACKs represent?",
  ["The physical link bandwidth.", "The amount of available space in the receiver's buffer that can accept incoming bytes without overflowing.", "The congestion window size of intermediate routers.", "The total collision count."], 1,
  "TCP Flow Control prevents a fast sender from swamping a slow receiver. The receiver advertises its available buffer capacity in the 'Window Size' header field (rwnd), constraining sender window size.")

add_q("Hard", "TCP", c(P1, P2),
  "In TCP Congestion Control, what event triggers the 'Fast Retransmit' mechanism before the Retransmission Timeout (RTO) timer expires?",
  ["Receiving a TCP FIN packet.", "Receiving 3 Duplicate Acknowledgments (DupACKs) for the same sequence number.", "A drop in receiver window size to zero.", "Receiving an ICMP Unreachable message."], 1,
  "When a TCP sender receives 3 duplicate ACKs (4 identical ACKs total) for a missing segment, it assumes that segment was lost in transit and retransmits it immediately (Fast Retransmit) without waiting for RTO timer expiration.")

add_q("Medium", "TCP vs UDP", c(S1, S2),
  "Which transport layer protocol provides connectionless, unreliable delivery with minimal header overhead (8 bytes)?",
  ["TCP", "UDP (User Datagram Protocol)", "SCTP", "IPsec"], 1,
  "UDP is a minimal, connectionless transport protocol. It adds only an 8-byte header (Source Port, Dest Port, Length, Checksum) without handshakes, flow control, or retransmission delays.")

add_q("Easy", "Transport Layer", c(S1, S2),
  "What 4-tuple uniquely identifies an active TCP connection socket on a host network stack?",
  ["Source IP, Source MAC, Destination IP, Destination MAC", "Source IP Address, Source Port Number, Destination IP Address, Destination Port Number", "Protocol ID, Process ID, Thread ID, Port Number", "Subnet Mask, Gateway IP, DNS IP, Host IP"], 1,
  "Every TCP connection is uniquely identified by a 4-tuple: (Source IP, Source Port, Destination IP, Destination Port).")

add_q("Hard", "TCP", c(H1, H2),
  "Calculate the theoretical maximum throughput of a TCP connection with a window size of 64 KB and a Round Trip Time (RTT) of 10 milliseconds.",
  ["6.4 Mbps", "26.2 Mbps", "52.4 Mbps", "104.8 Mbps"], 2,
  "Throughput = Window Size / RTT = (64 * 1024 * 8 bits) / 0.010 s = 524,288 bits / 0.010 s = 52,428,800 bps ≈ 52.4 Mbps.")

add_q("Medium", "TCP", c(H1, H2),
  "What TCP flag is used to immediately reset or abort an invalid or unexpected connection?",
  ["FIN", "URG", "RST", "PSH"], 2,
  "The RST (Reset) flag immediately aborts a TCP connection without completing a graceful 4-way termination sequence, used when packets arrive for closed ports or invalid handshakes.")

add_q("Hard", "TCP", c(P1, P2),
  "In TCP Congestion Control, what occurs during the 'Slow Start' phase upon receiving each successful ACK?",
  ["The Congestion Window (cwnd) increases by 1 MSS linearly per RTT.", "The Congestion Window (cwnd) doubles every RTT (increases by 1 MSS for every ACK received, exponential growth).", "The Congestion Window remains fixed.", "The Receiver Window is halved."], 1,
  "During Slow Start, cwnd starts at 1 MSS and increases by 1 MSS for every received ACK. This results in exponential growth (doubling cwnd every RTT) until cwnd reaches ssthresh (slow start threshold).")

add_q("Medium", "TCP", c(P1, P3),
  "What happens when the Congestion Window (cwnd) reaches the Slow Start Threshold (ssthresh) during TCP congestion control?",
  ["TCP enters the Congestion Avoidance phase, switching from exponential cwnd growth to linear growth (+1 MSS per RTT).", "TCP drops the connection.", "TCP resets cwnd to 1 MSS.", "TCP switches to UDP protocol."], 0,
  "When cwnd >= ssthresh, TCP transitions from Slow Start (exponential growth) into Congestion Avoidance, increasing cwnd linearly by 1 MSS per RTT (cwnd = cwnd + 1/cwnd per ACK) to probe bandwidth cautiously.")

add_q("Hard", "TCP", c(P1, H1),
  "What happens to the Congestion Window (cwnd) and Slow Start Threshold (ssthresh) when a Retransmission Timeout (RTO) occurs in traditional TCP Tahoe?",
  ["cwnd is set to cwnd/2; ssthresh is unchanged.", "ssthresh is set to cwnd/2, and cwnd is reset to 1 MSS (entering Slow Start).", "cwnd is set to 0; ssthresh is doubled.", "Connection drops instantly."], 1,
  "Upon an RTO timeout (severe congestion), TCP Tahoe sets ssthresh = max(cwnd/2, 2 MSS) and resets cwnd back to 1 MSS, restarting Slow Start.")

add_q("Easy", "Transport Layer", c(S1, S2),
  "What is the size of the standard UDP header?",
  ["8 bytes", "20 bytes", "32 bytes", "40 bytes"], 0,
  "The UDP header is exactly 8 bytes (4 fields of 2 bytes each: Source Port, Destination Port, Length, Checksum).")

add_q("Easy", "Transport Layer", c(S1, S3),
  "Which transport layer protocol field is optional in IPv4 but mandatory in IPv6?",
  ["TCP Sequence Number", "UDP Checksum", "IP TTL", "Ethernet FCS"], 1,
  "The UDP checksum is optional in IPv4 (can be set to 0), but is MANDATORY in IPv6 because IPv6 headers do not contain a header checksum.")

add_q("Medium", "TCP", c(H1, H2),
  "What TCP header option allows endpoints to negotiate selective acknowledgment of out-of-order received blocks?",
  ["Nagle Algorithm", "SACK (Selective Acknowledgment / RFC 2018)", "Window Scaling", "Keep-Alive"], 1,
  "TCP SACK (Selective Acknowledgment) allows a receiver to inform the sender about all non-contiguous data blocks received successfully, so the sender retransmits ONLY missing segments rather than retransmitting the whole window.")

add_q("Medium", "TCP", c(P1, P2),
  "What TCP socket options / algorithm combines small outgoing bytes into a single TCP segment to prevent overhead from tinygrams (1-byte payloads)?",
  ["Karn's Algorithm", "Nagle's Algorithm", "Jacobson's Algorithm", "Sliding Window Protocol"], 1,
  "Nagle's Algorithm delays sending small TCP segments (less than MSS) while unacknowledged data is in flight, buffering payload bytes to send larger consolidated segments and eliminate telnet 'tinygram' network congestion.")

add_q("Hard", "TCP", c(P1, P2),
  "What TCP mechanism disables Nagle's Algorithm when low-latency real-time response is required (e.g. interactive gaming or SSH)?",
  ["SO_KEEPALIVE", "TCP_NODELAY", "SO_REUSEADDR", "TCP_FASTOPEN"], 1,
  "Setting the TCP_NODELAY socket option disables Nagle's algorithm, forcing TCP to send small payload packets immediately without waiting for cumulative ACKs.")

add_q("Medium", "TCP", c(H1, H2),
  "What TCP header flag pushes buffered data immediately to the receiving application without waiting for buffers to fill?",
  ["URG", "PSH (Push)", "RST", "SYN"], 1,
  "The PSH (Push) flag requests the receiving host TCP stack to flush incoming data buffers and pass the payload immediately to the application layer.")

add_q("Easy", "Transport Layer", c(S1, S2),
  "What range of port numbers is designated as 'Well-Known Ports' by IANA?",
  ["0 to 1023", "1024 to 49151", "49152 to 65535", "1 to 65535"], 0,
  "Port ranges: Well-Known System Ports: 0-1023; Registered User Ports: 1024-49151; Dynamic/Private Ephemeral Ports: 49152-65535.")

add_q("Medium", "TCP", c(P1, P3),
  "What TCP state is reached on a server after sending SYN-ACK and awaiting the final ACK from the client?",
  ["LISTEN", "SYN_RCVD", "ESTABLISHED", "CLOSE_WAIT"], 1,
  "Upon receiving a client SYN, a server sends SYN-ACK and enters the SYN_RCVD state. Once the final ACK arrives, it transitions to ESTABLISHED.")

add_q("Hard", "TCP", c(P1, P2),
  "What TCP state is entered by a passive receiver after receiving a FIN packet from the active closing peer?",
  ["FIN_WAIT_1", "FIN_WAIT_2", "CLOSE_WAIT", "LAST_ACK"], 2,
  "When a host receives a FIN from its peer, it sends an ACK and enters the CLOSE_WAIT state while the local application finishes processing and closes its side of the socket.")

add_q("Easy", "Transport Layer", c(S1, S3),
  "What sequence number field in the TCP header tracks the byte stream order of transmitted data?",
  ["Acknowledgment Number", "Sequence Number", "Window Size", "Checksum"], 1,
  "The 32-bit Sequence Number field identifies the byte order position of the first data byte in a TCP segment within the overall connection stream.")

add_q("Medium", "TCP", c(P1, P3),
  "What does the Acknowledgment Number in a TCP segment indicate?",
  ["The sequence number of the current segment.", "The NEXT byte sequence number that the receiver expects to receive.", "The total number of packets dropped.", "The checksum calculation."], 1,
  "TCP ACKs are cumulative. The Acknowledgment Number indicates the next expected sequence number bit from the sender, implicitly confirming receipt of all preceding bytes.")

add_q("Hard", "TCP", c(P1, H1),
  "What attack exploits the TCP 3-way handshake by sending thousands of SYN requests with spoofed IPs to consume server memory in SYN_RCVD state?",
  ["SYN Flood Attack", "Ping of Death", "Smurf Attack", "Man-in-the-Middle"], 0,
  "A SYN Flood attack sends a flood of TCP SYN packets with forged source IPs. The target server allocates memory structures for each connection in SYN_RCVD state, quickly exhausting backlogged connection queues (mitigated by SYN Cookies).")

add_q("Medium", "TCP", c(H1, P1),
  "What mechanism allows a TCP sender with a 64 KB window field limitation to scale window sizes up to 1 GB over high-bandwidth long-delay links?",
  ["Nagle Algorithm", "TCP Window Scaling Option (RFC 1323)", "MSS Expansion", "Selective Retransmit"], 1,
  "TCP Window Scaling (RFC 1323) adds a scale factor option in SYN handshakes, shifting the 16-bit window field up to 14 bits to support receive windows up to 1 Gigabyte.")

add_q("Easy", "Transport Layer", c(S1, S2),
  "Which transport protocol is used by DNS queries for quick, lightweight domain name lookups?",
  ["UDP (Port 53)", "TCP (Port 80)", "ICMP", "HTTP"], 0,
  "Standard DNS name queries use UDP port 53 for fast response with low overhead. (DNS zone transfers and large responses over 512 bytes fallback to TCP port 53).")

add_q("Medium", "Transport Layer", c(S2, P4),
  "Which transport layer protocol is connection-oriented, preserves message boundaries (record-oriented), and supports multi-homing?",
  ["UDP", "TCP", "SCTP (Stream Control Transmission Protocol)", "RTP"], 2,
  "SCTP (Stream Control Transmission Protocol) combines features of TCP and UDP, offering reliable message-oriented streams, multi-homing across multiple IP paths, and protection against SYN flooding.")

add_q("Hard", "TCP", c(P1, P2),
  "What TCP feature allows sending data payload inside the initial SYN handshake packet to reduce latency for returning visitors (0-RTT / 1-RTT)?",
  ["TCP Fast Open (TFO / RFC 7413)", "Nagle Algorithm", "SACK", "Explicit Congestion Notification"], 0,
  "TCP Fast Open (TFO / RFC 7413) uses a cryptographic cookie to enable data transfer inside SYN packets during re-established connections, saving a full RTT handshake.")

add_q("Easy", "Transport Layer", c(S1, S3),
  "What algorithm is used to calculate Retransmission Timeout (RTO) dynamically based on measured Round Trip Times?",
  ["Dijkstra Algorithm", "Jacobson / Karn Algorithm", "Bellman-Ford Algorithm", "RSA Algorithm"], 1,
  "Jacobson's and Karn's algorithms calculate estimated RTT and RTT variance to dynamically adjust Retransmission Timeout (RTO), ignoring sample RTTs from retransmitted segments.")

add_q("Medium", "TCP", c(H1, H2),
  "What flag in IP and TCP headers allows intermediate routers to notify endpoints of impending network congestion without dropping packets?",
  ["Explicit Congestion Notification (ECN - ECE/CWR flags)", "DiffServ", "QoS", "RST"], 0,
  "Explicit Congestion Notification (ECN / RFC 3168) allows routers experiencing buffer pressure to set ECN bits in IP headers. TCP receivers echo ECE flags back to senders, who reduce cwnd without packet drop penalties.")

add_q("Hard", "TCP", c(P1, P3),
  "What happens if a TCP endpoint receives a segment with sequence number outside its active Receive Window?",
  ["The segment is accepted and buffered.", "The segment is dropped, and the receiver responds with a duplicate ACK indicating expected sequence numbers.", "The connection is closed immediately.", "The router crashes."], 1,
  "Segments with sequence numbers outside the active Receive Window are dropped as invalid/duplicate, and the receiver sends an ACK indicating the current expected sequence number.")

print(f"Current Q count: {len(questions)}")

# ==============================================================================
# 8. APPLICATION LAYER PROTOCOLS & WELL-KNOWN PORTS (25 Qs, Q171 - Q195)
# ==============================================================================
add_q("Easy", "Application Layer", c(S1, S2),
  "Which DNS record type maps an IPv4 address to a domain name (Reverse DNS lookup)?",
  ["A Record", "AAAA Record", "PTR Record (Pointer)", "CNAME Record"], 2,
  "A PTR (Pointer) record maps an IP address to a canonical domain hostname in reverse DNS lookup zones (in-addr.arpa). A maps to IPv4, AAAA to IPv6, and CNAME creates host aliases.")

add_q("Medium", "DNS", c(P1, P2),
  "What is the function of a DNS CNAME (Canonical Name) record?",
  ["To assign an IPv6 address.", "To alias one domain name to another domain name.", "To specify mail exchange servers.", "To authorize DNSSEC signatures."], 1,
  "A CNAME (Canonical Name) record specifies that a domain name is an alias for another primary domain name (e.g., mapping www.example.com to example.com).")

add_q("Medium", "HTTP", c(P1, P3),
  "How does HTTP/1.1 Persistent Connections (Keep-Alive) improve performance compared to HTTP/1.0?",
  ["It encrypts requests using TLS by default.", "It allows multiple HTTP request/response exchanges over a single open TCP connection without re-establishing handshakes.", "It replaces TCP with UDP.", "It compresses HTML text with Gzip."], 1,
  "HTTP/1.0 established a new TCP connection for every asset, adding heavy TCP+TLS handshake latency. HTTP/1.1 introduced persistent connections, keeping TCP connections alive for multiple requests.")

add_q("Hard", "HTTP", c(P1, P2, P3),
  "What major performance limitation of HTTP/1.1 was resolved by HTTP/2 multiplexing?",
  ["Lack of cookie support.", "Head-of-Line (HoL) Blocking at the HTTP request layer.", "Inability to send POST requests.", "Lack of IP address routing."], 1,
  "In HTTP/1.1, requests over a single TCP connection must be served sequentially (causing HTTP Head-of-Line blocking). HTTP/2 splits messages into binary frames and multiplexes streams concurrently over one TCP connection.")

add_q("Medium", "Application Layer", c(S1, S3),
  "Which protocol operates on TCP ports 20 and 21 for transferring files between hosts?",
  ["TFTP", "FTP (File Transfer Protocol)", "SFTP", "FTPS"], 1,
  "FTP (File Transfer Protocol) uses TCP port 21 for control/command signals and TCP port 20 for data transfers.")

add_q("Medium", "Application Layer", c(S2, P4),
  "What is the key functional difference between POP3 (Port 110) and IMAP (Port 143) email protocols?",
  ["POP3 encrypts emails; IMAP does not.", "POP3 downloads emails to a local device and typically deletes them from the server, whereas IMAP synchronizes folders live directly on the server across multiple devices.", "POP3 uses UDP; IMAP uses TCP.", "POP3 is used for sending mail; IMAP is used for receiving."], 1,
  "POP3 downloads email to a local client and removes it from the server. IMAP (Internet Message Access Protocol) keeps emails on the server and synchronizes folder states live across multiple devices.")

add_q("Easy", "Application Layer", c(S1, S2),
  "Which protocol uses TCP port 25 for pushing email messages between mail servers (MTA)?",
  ["POP3", "IMAP", "SMTP (Simple Mail Transfer Protocol)", "SNMP"], 2,
  "SMTP (Simple Mail Transfer Protocol) is the standard protocol for transmitting emails between mail servers and from clients to mail submission servers (Port 25 or 587).")

add_q("Easy", "Application Layer", c(S1, S2),
  "Which secure shell protocol replaces unencrypted Telnet (Port 23) for remote command line access using TCP port 22?",
  ["SSH (Secure Shell)", "SFTP", "SSL", "SNMP"], 0,
  "SSH (Secure Shell / TCP Port 22) provides an encrypted channel for remote command-line login, replacing insecure unencrypted Telnet (Port 23).")

add_q("Medium", "Application Layer", c(S3, P3),
  "What protocol uses UDP ports 161 and 162 for monitoring network devices, routers, switches, and server metrics?",
  ["SNMP (Simple Network Management Protocol)", "SMTP", "NTP", "DHCP"], 0,
  "SNMP (Simple Network Management Protocol) uses UDP port 161 (queries) and UDP port 162 (SNMP Traps) to monitor and manage hardware device metrics across networks.")

add_q("Easy", "Application Layer", c(S1, S2),
  "Which network protocol uses UDP port 123 to synchronize system clocks across distributed computers to UTC time?",
  ["NTP (Network Time Protocol)", "SNMP", "DNS", "DHCP"], 0,
  "Network Time Protocol (NTP / UDP Port 123) synchronizes computer clock time over packet-switched networks to within a few milliseconds of Coordinated Universal Time (UTC).")

add_q("Hard", "HTTP", c(P1, P2),
  "What header compression algorithm is utilized by HTTP/2 to compress repeated HTTP header fields across requests?",
  ["Gzip", "Brotli", "HPACK (RFC 7541)", "LZMA"], 2,
  "HTTP/2 uses HPACK (RFC 7541) compression, maintaining indexed tables of header fields at sender and receiver to eliminate redundant HTTP header transmission overhead.")

add_q("Easy", "Application Layer", c(S1, S2),
  "What is the default TCP port number for HTTPS (HTTP Secure) traffic?",
  ["80", "443", "8080", "8443"], 1,
  "HTTPS (HTTP over TLS/SSL) communicates over TCP port 443 by default. Standard unencrypted HTTP uses TCP port 80.")

add_q("Medium", "DNS", c(P1, P3),
  "What DNS record type specifies the mail server responsible for accepting email on behalf of a domain?",
  ["A Record", "MX Record (Mail Exchanger)", "NS Record", "TXT Record"], 1,
  "An MX (Mail Exchanger) record maps a domain name to a list of message transfer agent (MTA) mail servers along with priority preference values.")

add_q("Hard", "DNS", c(P1, P2),
  "In a DNS recursive query, what action does a Local Recursive Resolver take if an incoming query is NOT found in its local cache?",
  ["It returns an immediate failure error to the client.", "It queries the DNS Root Servers, TLD Servers, and Authoritative Name Servers sequentially until the answer is resolved.", "It broadcasts an ARP request.", "It resets the TCP connection."], 1,
  "When a recursive resolver misses local cache, it performs iterative lookups: querying a Root DNS server (.) -> Top-Level Domain server (.com) -> Authoritative Name Server for the target domain.")

add_q("Easy", "Application Layer", c(S1, S2),
  "What lightweight protocol uses UDP port 69 for simple file transfers without user authentication or directory listing?",
  ["FTP", "TFTP (Trivial File Transfer Protocol)", "SFTP", "SCP"], 1,
  "TFTP (Trivial File Transfer Protocol) uses UDP port 69 to transfer files with minimal footprint, commonly used for bootstrapping diskless network devices and router firmware updates.")

add_q("Medium", "Application Layer", c(S3, P3),
  "What DNS record type contains TXT data used for domain ownership verification, SPF (Sender Policy Framework), and DKIM email authentication?",
  ["CNAME Record", "TXT Record", "PTR Record", "SOA Record"], 1,
  "TXT (Text) records hold arbitrary human/machine-readable text data, widely used for SPF, DKIM, and DMARC email security policies and domain validation.")

add_q("Hard", "HTTP", c(P1, P2),
  "What HTTP status code series indicates a Server Error (e.g. 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable)?",
  ["2xx", "3xx", "4xx", "5xx"], 3,
  "HTTP Status Codes: 1xx Informational, 2xx Success (200 OK), 3xx Redirection (301, 302), 4xx Client Errors (404 Not Found, 403 Forbidden), 5xx Server Errors (500, 502, 503).")

add_q("Easy", "Application Layer", c(S1, S2),
  "What port does unencrypted Telnet use for remote terminal connections?",
  ["21", "22", "23", "25"], 2,
  "Telnet communicates over TCP port 23 in cleartext without encryption, making it vulnerable to packet sniffing.")

add_q("Medium", "DNS", c(P1, P3),
  "What DNS record type delegates a DNS zone to use specific authoritative name servers?",
  ["NS Record (Name Server)", "SOA Record", "A Record", "MX Record"], 0,
  "An NS (Name Server) record delegates a domain zone to specific authoritative name servers responsible for answering queries for that domain.")

add_q("Hard", "DNS", c(P1, P2),
  "What security extension adds cryptographic digital signatures to DNS records to protect against DNS cache poisoning?",
  ["DNSSEC (DNS Security Extensions)", "DoH (DNS over HTTPS)", "DoT (DNS over TLS)", "DNScrypt"], 0,
  "DNSSEC (DNS Security Extensions) uses public-key cryptography to digitally sign DNS records (RRSIG records), authenticating DNS response origin and verifying data integrity.")

add_q("Medium", "HTTP", c(P1, P4),
  "What is the purpose of the HTTP 'Host' request header introduced in HTTP/1.1?",
  ["To specify the client IP address.", "To allow a web server to host multiple domain names on a single IP address (Virtual Hosting).", "To set cookie expiry times.", "To compress HTTP responses."], 1,
  "The HTTP/1.1 Host header specifies the target domain hostname in the request, enabling Virtual Hosting (serving hundreds of distinct websites from a single server IP address).")

add_q("Easy", "Application Layer", c(S1, S2),
  "Which HTTP request method is idempotent and requests representation of a specified resource without altering server state?",
  ["POST", "GET", "PATCH", "CONNECT"], 1,
  "GET is an idempotent and safe HTTP method used strictly to retrieve data from a server without modifying resource state.")

add_q("Medium", "HTTP", c(P1, P2),
  "What is the difference between HTTP GET and HTTP POST methods?",
  ["GET sends data in HTTP request body; POST appends parameters to URL string.", "GET appends data parameters to the URL query string (limited length, cached); POST sends data inside the HTTP request body (unlimited length, not cached).", "GET is encrypted; POST is cleartext.", "GET uses UDP; POST uses TCP."], 1,
  "GET appends parameters to the URL query string (visible in browser history/logs, cached). POST sends data within the HTTP message request body (ideal for sensitive/large data submissions).")

add_q("Hard", "HTTP", c(P1, P2),
  "What security mechanism enforced by web browsers restricts scripts on one origin from accessing data from another origin?",
  ["Same-Origin Policy (SOP)", "CORS (Cross-Origin Resource Sharing)", "Content Security Policy (CSP)", "Strict-Transport-Security (HSTS)"], 0,
  "The Same-Origin Policy (SOP) is a core web browser security model that isolates resources loaded from different origins (protocol + domain + port). CORS allows servers to relax SOP selectively.")

add_q("Medium", "Application Layer", c(S2, S3),
  "Which port is used by secure LDAP over SSL/TLS (LDAPS)?",
  ["389", "636", "993", "995"], 1,
  "Standard unencrypted LDAP uses TCP/UDP port 389. Lightweight Directory Access Protocol over SSL/TLS (LDAPS) uses TCP port 636.")


# ==============================================================================
# 9. NETWORK SECURITY & CRYPTOGRAPHY (20 Qs, Q196 - Q215)
# ==============================================================================
add_q("Medium", "Security", c(P1, P3),
  "In Asymmetric Encryption (Public Key Cryptography), if Alice wants Bob to send her a confidential secret message, which key must Bob use to encrypt it?",
  ["Alice's Private Key", "Alice's Public Key", "Bob's Public Key", "Bob's Private Key"], 1,
  "To guarantee confidentiality in public key cryptography, data is encrypted using the recipient's (Alice's) Public Key. Only Alice's secret Private Key can decrypt it.")

add_q("Hard", "Security", c(P1, P2),
  "How does a Digital Signature ensure Non-Repudiation and Data Integrity?",
  ["The sender encrypts the payload using the receiver's public key.", "The sender hashes the message and encrypts the hash digest using the sender's Private Key; receivers verify it using sender's Public Key.", "The sender encrypts the message with a shared symmetric key.", "The sender requests a certificate from DNS."], 1,
  "A digital signature hashes the message and encrypts the digest with the sender's Private Key. Recipients decrypt the hash using sender's Public Key. Success proves identity (authentication) and un-tampered data (integrity).")

add_q("Medium", "Security", c(H1, P1),
  "What is the primary difference between a Stateful Inspection Firewall and a Stateless Packet Filtering Firewall?",
  ["Stateless firewalls operate at Layer 7; stateful firewalls operate at Layer 1.", "Stateless firewalls evaluate isolated packet headers against static ACL rules; Stateful firewalls track active connection states (e.g. TCP handshakes) in a state table.", "Stateless firewalls inspect payload viruses.", "Stateful firewalls drop all UDP traffic."], 1,
  "Stateless filters check each packet independently against static rules. Stateful firewalls maintain connection tracking tables (e.g. TCP SYN/ACK sequences), automatically permitting returning traffic for established connections.")

add_q("Hard", "Security", c(P1, P2),
  "What security property is guaranteed when TLS key exchange utilizes Ephemeral Diffie-Hellman (ECDHE / Perfect Forward Secrecy)?",
  ["Fast asymmetric hashing.", "Perfect Forward Secrecy (PFS): compromising the server's long-term private key in the future cannot decrypt past recorded session traffic.", "Elimination of SSL certificates.", "Client password bypass."], 1,
  "Perfect Forward Secrecy (PFS) via ECDHE generates temporary per-session keys. If an attacker later steals the server's master private key, they still CANNOT decrypt past recorded network sessions.")

add_q("Easy", "Security", c(S1, S2),
  "What type of cyber attack floods a server with millions of requests from a distributed botnet of compromised IoT devices?",
  ["Man-in-the-Middle (MitM)", "Distributed Denial of Service (DDoS)", "SQL Injection", "Cross-Site Scripting (XSS)"], 1,
  "A DDoS attack orchestrates a botnet of infected devices to overwhelm target bandwidth or server resources, rendering applications inaccessible to legitimate users.")

add_q("Medium", "Security", c(H1, H2),
  "What is the difference between an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS)?",
  ["IDS runs inline and blocks traffic; IPS sits out-of-band and alerts.", "IDS passively monitors network traffic out-of-band and alerts administrators; IPS operates inline in the network traffic path to actively block detected threats.", "IDS handles physical security; IPS handles Wi-Fi passwords.", "There is no difference."], 1,
  "IDS monitors traffic passively (out-of-band via TAP/SPAN port) and raises alerts. IPS sits inline in the network data path, actively analyzing and dropping malicious packets in real time.")

add_q("Hard", "Security", c(P1, P3),
  "What protocol suite operates at the Network Layer (Layer 3) to provide IP packet encryption, authentication, and integrity (AH and ESP headers)?",
  ["SSL / TLS", "IPsec (Internet Protocol Security)", "SSH", "HTTPS"], 1,
  "IPsec operates at Layer 3 (Network Layer) providing transparent security for IP traffic using Authentication Header (AH) for integrity/authentication and Encapsulating Security Payload (ESP) for encryption.")

add_q("Medium", "Security", c(S3, P3),
  "Which cryptographic algorithm is a widely used Symmetric Key Cipher supporting 128-bit, 192-bit, and 256-bit key sizes?",
  ["RSA", "AES (Advanced Encryption Standard)", "Diffie-Hellman", "ECC"], 1,
  "AES (Advanced Encryption Standard) is a fast symmetric block cipher using identical keys for encryption and decryption, standardized by NIST for secure bulk data encryption.")

add_q("Easy", "Security", c(S1, S2),
  "What entity issues, signs, and revokes digital X.509 certificates to verify public key ownership for HTTPS websites?",
  ["DHCP Server", "Certificate Authority (CA)", "DNS Root Server", "NAT Router"], 1,
  "A Certificate Authority (CA) is a trusted third-party organization (e.g. Let's Encrypt, DigiCert) that validates domain ownership and issues signed digital X.509 certificates.")

add_q("Hard", "Security", c(P1, P2),
  "During a TLS 1.2 handshake, how does the client verify that the web server's SSL certificate is authentic and trustworthy?",
  ["By pinging the server IP.", "By verifying the CA's digital signature on the certificate against pre-installed trusted Root CA public keys in the browser trust store.", "By checking the server MAC address.", "By sending an ARP request."], 1,
  "The client builds a certificate chain to a trusted Root CA and verifies the CA's cryptographic digital signature using the Root CA's public key built into the browser OS trust store.")

add_q("Medium", "Security", c(H1, P1),
  "What is the difference between Symmetric and Asymmetric encryption regarding key management and performance?",
  ["Symmetric uses two keys and is slow; Asymmetric uses one key and is fast.", "Symmetric uses a single shared secret key for encryption/decryption (fast, ideal for bulk data); Asymmetric uses a public/private key pair (computationally heavy, ideal for key exchange).", "Symmetric works only on wireless; Asymmetric works on wired networks.", "Symmetric requires certificates; Asymmetric does not."], 1,
  "Symmetric encryption uses 1 shared key (fast, AES). Asymmetric uses a Key Pair (Public key encrypts, Private key decrypts - slower, RSA/ECC). Modern TLS uses Asymmetric for key exchange and Symmetric for bulk payload encryption.")

add_q("Hard", "Security", c(P1, P2),
  "What major optimization was introduced in TLS 1.3 compared to TLS 1.2?",
  ["Removal of encryption.", "Reduced handshake latency from 2 RTTs to 1 RTT (and 0-RTT resumption), and removal of legacy insecure ciphers (RSA key exchange, MD5, SHA-1).", "Introduction of cleartext headers.", "Mandatory use of Telnet."], 1,
  "TLS 1.3 streamlined security by removing outdated ciphers and reducing connection handshake latency from 2 RTTs down to 1 RTT (and supporting 0-RTT session resumption).")

add_q("Easy", "Security", c(S1, S2),
  "What network security attack tricks a DNS resolver into caching fake IP addresses for legitimate domains?",
  ["SYN Flood", "DNS Cache Poisoning (DNS Spoofing)", "Buffer Overflow", "Cross-Site Scripting"], 1,
  "DNS Cache Poisoning (DNS Spoofing) injects corrupt IP records into a recursive DNS resolver's cache, redirecting users to malicious phishing websites.")

add_q("Medium", "Security", c(H1, H2),
  "What feature in IPsec ESP (Encapsulating Security Payload) protects against Replay Attacks?",
  ["Diffie-Hellman Group 14", "Sequence Number field combined with sliding window verification", "AES-256 key expansion", "HMAC hashing"], 1,
  "IPsec ESP includes a monotonically increasing 32-bit Sequence Number in packet headers. Receivers maintain a sliding window to reject duplicate or replayed packets.")

add_q("Hard", "Security", c(P1, P3),
  "What vulnerability allows an attacker to eavesdrop or modify traffic on an unencrypted Wi-Fi or LAN by positioning themselves between host and router?",
  ["Buffer Overflow", "Man-in-the-Middle (MitM) Attack", "SQL Injection", "Amplification Attack"], 1,
  "A Man-in-the-Middle (MitM) attack occurs when an adversary secretly intercepts and relays communications between two parties who believe they are communicating directly.")

add_q("Easy", "Security", c(S1, S3),
  "What cryptographic hash functions produce 128-bit and 160-bit hash digests respectively (now considered cryptographically broken for collision resistance)?",
  ["AES-128 and AES-256", "MD5 and SHA-1", "RSA-1024 and RSA-2048", "SHA-256 and SHA-512"], 1,
  "MD5 generates a 128-bit hash; SHA-1 generates a 160-bit hash. Both are now deprecated due to collision vulnerabilities, replaced by SHA-256 / SHA-3.")

add_q("Medium", "Security", c(S2, P4),
  "What security protocol replaces legacy WPA2 for Wi-Fi security, introducing Simultaneous Authentication of Equals (SAE) to protect against offline dictionary attacks?",
  ["WEP", "WPA3", "IPsec", "HTTPS"], 1,
  "WPA3 replaces WPA2, mandating SAE (Simultaneous Authentication of Equals) Dragonfly handshake to protect Wi-Fi passwords against offline dictionary attacks.")

add_q("Hard", "Security", c(P1, P2),
  "What HTTP response header instructs web browsers to communicate with a website ONLY over HTTPS connections, automatically converting HTTP links?",
  ["Content-Security-Policy", "Strict-Transport-Security (HSTS)", "X-Frame-Options", "Access-Control-Allow-Origin"], 1,
  "HTTP Strict Transport Security (HSTS / RFC 6797) forces browsers to use secure HTTPS connections exclusively, preventing SSL stripping downgrade attacks.")

add_q("Easy", "Security", c(S1, S2),
  "What mechanism uses public key cryptography to prove that an email message was sent by an authorized domain owner and was not altered in transit?",
  ["SPF", "DKIM (DomainKeys Identified Mail)", "DMARC", "MX"], 1,
  "DKIM (DomainKeys Identified Mail) attaches a cryptographic signature to outgoing email headers, verified by receivers querying the sender domain's DNS TXT public key.")

add_q("Medium", "Security", c(H1, H2),
  "What is the difference between IPsec Tunnel Mode and IPsec Transport Mode?",
  ["Tunnel Mode encrypts only the payload; Transport Mode encrypts the whole packet.", "Transport Mode encrypts only the IP payload (header left intact, for host-to-host); Tunnel Mode encrypts the entire original IP packet and prepends a new IP header (for site-to-site VPNs).", "Tunnel Mode operates at Layer 2; Transport Mode at Layer 7.", "There is no difference."], 1,
  "Transport Mode encrypts payload only (used host-to-host). Tunnel Mode encrypts the ENTIRE original IP packet (header + payload) inside a new IP packet (used for Site-to-Site router VPN tunnels).")


# ==============================================================================
# 10. WIRELESS & MOBILE NETWORKS (15 Qs, Q216 - Q230)
# ==============================================================================
add_q("Medium", "Wireless Networks", c(H1, H2),
  "In IEEE 802.11 Wi-Fi networks, how does the RTS/CTS (Request to Send / Clear to Send) handshake resolve the 'Hidden Node Problem'?",
  ["By encrypting wireless frames.", "The Access Point broadcasts a CTS frame containing a NAV (Network Allocation Vector) timer that defers all nearby nodes from transmitting during the frame exchange.", "By doubling antenna transmission gain.", "By assigning dynamic IP addresses."], 1,
  "When Host A sends RTS to Access Point (AP), AP replies with CTS broadcast. All nearby hidden nodes (like Host B) hear the CTS and defer transmission for the NAV duration, preventing collisions.")

add_q("Easy", "Wireless Networks", c(S1, S2),
  "What is the maximum 32-character human-readable name used to identify a wireless Wi-Fi network?",
  ["BSSID", "SSID (Service Set Identifier)", "MAC Address", "Subnet Mask"], 1,
  "SSID (Service Set Identifier) is the 32-character unique name assigned to a WLAN network broadcast by access points.")

add_q("Medium", "Wireless Networks", c(H1, H2),
  "What is a BSSID (Basic Service Set Identifier) in Wi-Fi networks?",
  ["The IP address of the router.", "The 48-bit physical MAC address of the Access Point's radio interface.", "The Wi-Fi password hash.", "The DNS server IP."], 1,
  "BSSID (Basic Service Set Identifier) is the 48-bit MAC address of an Access Point's wireless radio interface, uniquely distinguishing APs broadcasting the same SSID.")

add_q("Hard", "Wireless Networks", c(H1, H2),
  "What key modulation technology introduced in Wi-Fi 6 (802.11ax) allows a single wireless channel to be divided into smaller sub-carriers (Resource Units) for multiple clients simultaneously?",
  ["OFDM", "OFDMA (Orthogonal Frequency Division Multiple Access)", "CDMA", "FHSS"], 1,
  "Wi-Fi 6 (802.11ax) introduced OFDMA, which divides a Wi-Fi channel into smaller sub-carriers called Resource Units (RUs), enabling the AP to serve multiple low-latency clients concurrently.")

add_q("Medium", "Wireless Networks", c(H1, H2),
  "What technology allows a Wi-Fi access point to transmit independent data streams to multiple client devices at the exact same time using spatial streaming antennas?",
  ["MIMO", "MU-MIMO (Multi-User Multiple Input Multiple Output)", "Duplexing", "Beamforming"], 1,
  "MU-MIMO (Multi-User MIMO) enables an access point with multiple antennas to send distinct data streams to multiple connected devices simultaneously rather than sequentially.")

add_q("Easy", "Wireless Networks", c(S1, S3),
  "Which IEEE standard governs Wireless Local Area Networks (WLAN / Wi-Fi)?",
  ["IEEE 802.3", "IEEE 802.11", "IEEE 802.15", "IEEE 802.1Q"], 1,
  "IEEE 802.11 defines standards for WLAN (Wi-Fi). 802.3 defines Ethernet, 802.15 defines WPAN (Bluetooth/ZigBee), and 802.1Q defines VLANs.")

add_q("Medium", "Wireless Networks", c(H1, H2),
  "What frequency band was newly opened for Wi-Fi 6E (IEEE 802.11ax extension)?",
  ["900 MHz", "2.4 GHz", "5 GHz", "6 GHz band (5.925 GHz to 7.125 GHz)"], 3,
  "Wi-Fi 6E extends Wi-Fi 6 operation into the clean, uncrowded 6 GHz spectrum (up to 1200 MHz of additional bandwidth), offering 160 MHz wide channels without legacy interference.")

add_q("Easy", "Wireless Networks", c(S1, S2),
  "Which short-range wireless communication technology operates at 13.56 MHz over distances under 10 cm, used for contactless payments (Apple Pay / Google Pay)?",
  ["Bluetooth", "NFC (Near Field Communication)", "ZigBee", "Wi-Fi"], 1,
  "NFC (Near Field Communication) operates at 13.56 MHz over very short distances (<10 cm), enabling contactless payments, tap-to-pair, and smart card emulation.")

add_q("Medium", "Wireless Networks", c(H1, H2),
  "What low-power, low-data-rate wireless mesh networking standard (IEEE 802.15.4) is widely used in IoT smart home sensors?",
  ["Bluetooth Classic", "ZigBee", "Wi-Fi 5", "5G NR"], 1,
  "ZigBee (IEEE 802.15.4) is a low-power, low-bandwidth wireless mesh networking protocol designed for home automation, smart lighting, and IoT sensors.")

add_q("Hard", "Wireless Networks", c(H1, H2),
  "In cellular networks, what is the process of transferring an active voice/data connection from one cell tower (base station) to another as a mobile user moves?",
  ["Roaming", "Handover / Handoff", "Paging", "Frequency Reuse"], 1,
  "Handover (or Handoff) is the cellular process where an active call or data session is seamlessly transferred from one base station cell tower to another without disconnecting.")

add_q("Easy", "Wireless Networks", c(S1, S2),
  "What generation of cellular network technology introduced beamforming, ultra-reliable low-latency communication (URLLC), and massive IoT (mMTC)?",
  ["3G", "4G LTE", "5G NR", "2G GSM"], 2,
  "5G NR (New Radio) introduces millimetre wave spectrum, mobile edge computing, beamforming, URLLC (<1 ms latency), and massive IoT connectivity.")

add_q("Medium", "Wireless Networks", c(H1, H2),
  "What feature in Wi-Fi routers focuses wireless RF signal transmission directly toward connected client devices rather than broadcasting equally in all directions?",
  ["Beamforming", "Spatial Multiplexing", "CSMA/CA", "Channel Bonding"], 0,
  "Beamforming uses signal processing across multiple antennas to adjust phase and amplitude, concentrating radio signals directly toward client devices for higher signal strength.")

add_q("Hard", "Wireless Networks", c(H1, H2),
  "What cellular architecture component in 4G LTE handles user authentication, mobility tracking, and session management?",
  ["eNodeB", "MME (Mobility Management Entity)", "SGW (Serving Gateway)", "PGW (PDN Gateway)"], 1,
  "In 4G LTE Evolved Packet Core (EPC), the Mobility Management Entity (MME) handles signaling, user authentication via HSS, roaming, and handover mobility management.")

add_q("Easy", "Wireless Networks", c(S1, S3),
  "What wireless personal area network technology operates under IEEE 802.15.1 and uses frequency-hopping spread spectrum (FHSS)?",
  ["Wi-Fi", "Bluetooth", "Cellular 4G", "Infrared"], 1,
  "Bluetooth (IEEE 802.15.1) operates in 2.4 GHz ISM band using Frequency-Hopping Spread Spectrum (FHSS) hopping 1600 times per second to minimize interference.")

add_q("Medium", "Wireless Networks", c(H1, H2),
  "What Wi-Fi channel width bonding combines two 20 MHz channels into a single higher throughput channel?",
  ["40 MHz Channel Bonding", "80 MHz", "160 MHz", "320 MHz"], 0,
  "Channel Bonding combines adjacent 20 MHz Wi-Fi channels into 40 MHz, 80 MHz, or 160 MHz channels to double data throughput.")


# ==============================================================================
# 11. ADVANCED TOPICS (SDN, CDN, PROXY, K8S) (20 Qs, Q231 - Q250)
# ==============================================================================
add_q("Hard", "Advanced Topics", c(H1, H2, P1),
  "In Software-Defined Networking (SDN), what protocol is standard for communication between the centralized SDN Controller and data plane switches?",
  ["BGP", "OpenFlow", "SNMP", "OSPF"], 1,
  "OpenFlow is the standardized southbound interface protocol in SDN that allows a centralized software controller to program forwarding tables on data plane network switches.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "What protocol forms the basis of HTTP/3, operating over UDP to replace TCP and TLS handshakes?",
  ["SCTP", "QUIC (Quick UDP Internet Connections)", "RSVP", "RTP"], 1,
  "HTTP/3 is built on QUIC (Quick UDP Internet Connections), a multiplexed, encrypted transport protocol over UDP that eliminates TCP Head-of-Line blocking and achieves 0-RTT connection establishment.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "What network routing mechanism allows a CDN to advertise a single IP address from hundreds of global Edge servers, routing users to the closest node via BGP?",
  ["Unicast", "Multicast", "Anycast", "Broadcast"], 2,
  "Anycast routing advertises a single destination IP address from multiple geographically distributed edge locations. Global BGP routers automatically route user packets to the nearest edge location based on shortest AS path.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "What is the key architectural distinction between a Forward Proxy and a Reverse Proxy?",
  ["Forward proxy protects servers; Reverse proxy protects clients.", "A Forward Proxy acts on behalf of clients (hiding client IPs from internet servers); a Reverse Proxy acts on behalf of servers (load balancing and hiding backend server infrastructure from clients).", "Forward proxy works at Layer 2; Reverse proxy works at Layer 3.", "There is no difference."], 1,
  "Forward Proxies sit in front of clients to filter outgoing traffic and mask client identity. Reverse Proxies sit in front of origin servers to perform SSL termination, caching, rate limiting, and load balancing.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "Which load balancing algorithm distributes incoming requests sequentially down a list of backend servers, looping back to the top when reaching the end?",
  ["Least Connections", "Round Robin", "IP Hash", "Weighted Response Time"], 1,
  "Round Robin load balancing passes incoming requests to backend pool servers sequentially in rotation. Weighted Round Robin assigns higher proportions of traffic to more powerful servers.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "In Kubernetes networking, how do container Pods communicate with each other across different worker nodes by default?",
  ["Through NAT port translation.", "Every Pod receives a unique, routable IP address within a flat cluster network model, allowing direct Pod-to-Pod communication without NAT.", "Pods cannot communicate across nodes.", "Pods communicate strictly via public DNS."], 1,
  "Kubernetes imposes a flat IP-per-Pod network model (via CNI plugins like Calico/Flannel): every Pod gets a unique IP and can communicate directly with any other Pod in the cluster without NAT.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "What technology allows full-duplex, bidirectional persistent communication over a single TCP connection between a web browser and a server?",
  ["HTTP Long Polling", "WebSockets (RFC 6455)", "Server-Sent Events (SSE)", "AJAX"], 1,
  "WebSockets (ws:// or wss://) starts with an HTTP Upgrade handshake and establishes a persistent, full-duplex TCP socket connection for real-time bidirectional data exchange with minimal framing overhead.")

add_q("Hard", "Advanced Topics", c(H1, H2),
  "What network virtualization technology decouples network functions (firewalls, routers, load balancers) from proprietary hardware onto software VMs on commodity x86 servers?",
  ["SDN", "NFV (Network Functions Virtualization)", "VLAN", "MPLS"], 1,
  "Network Functions Virtualization (NFV) virtualizes middlebox network functions (firewalls, NAT, IPsec, load balancers) into software software Virtual Network Functions (VNFs) running on standard server hardware.")

add_q("Hard", "Advanced Topics", c(H1, H2),
  "What packet forwarding technique uses short fixed-length labels (Label Switching) rather than long IP lookups to route traffic rapidly across core enterprise WAN networks?",
  ["MPLS (Multiprotocol Label Switching)", "SDN", "BGP", "Frame Relay"], 0,
  "MPLS (Multiprotocol Label Switching) appends 20-bit MPLS labels to packets. Core routers perform ultra-fast label swapping (LSP) rather than complex IP routing table lookups.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "What is the role of a Load Balancer at Layer 4 (Transport Layer) vs Layer 7 (Application Layer)?",
  ["Layer 4 load balancers inspect HTTP cookies; Layer 7 load balancers route using MAC addresses.", "Layer 4 load balancers route traffic based on IP and TCP/UDP ports without inspecting payload; Layer 7 load balancers inspect application data (HTTP headers, URIs, cookies) to route requests.", "Layer 4 load balancers do not support SSL; Layer 7 load balancers do not support TCP.", "There is no difference."], 1,
  "Layer 4 load balancing operates at TCP/UDP level, forwarding packets based on IP/Port with high throughput. Layer 7 load balancing inspects HTTP/HTTPS headers, URLs, and cookies to make intelligent application routing decisions.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "What network protocol mechanism allows server applications to push updates to client browsers unidirectionally over standard HTTP connections?",
  ["WebSockets", "Server-Sent Events (SSE / EventSource)", "gRPC", "MQTT"], 1,
  "Server-Sent Events (SSE) allows a client to open a persistent HTTP connection (text/event-stream) over which the server streams real-time text updates unidirectionally to the browser.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "What is the main function of an Ingress Controller in Kubernetes?",
  ["To assign MAC addresses to Pods.", "To manage external HTTP/HTTPS access to services within a Kubernetes cluster, providing SSL termination, path-based routing, and name-based virtual hosting.", "To backup database volumes.", "To monitor CPU temperatures."], 1,
  "An Ingress Controller (e.g. NGINX Ingress) acts as a Layer 7 reverse proxy, exposing HTTP/HTTPS routes from outside the cluster to services running inside the cluster based on defined Ingress rules.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "What high-performance RPC framework developed by Google uses HTTP/2 for transport and Protocol Buffers (Protobuf) for binary serialization?",
  ["gRPC", "RESTful API", "SOAP", "GraphQL"], 0,
  "gRPC is a high-performance open-source RPC framework that uses HTTP/2 for streaming multiplexed transport and Protocol Buffers (Protobuf) for compact binary payload serialization.")

add_q("Easy", "Advanced Topics", c(S1, P1),
  "What mechanism automatically shifts traffic away from unhealthy backend server instances in a load balancer pool?",
  ["DNS Poisoning", "Health Checks (Probes)", "BGP Flapping", "ARP Inspection"], 1,
  "Load balancers periodically run Health Checks (pinging HTTP endpoints or TCP ports). If an instance fails consecutive probes, it is marked unhealthy and removed from the active routing pool.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "What is Edge Computing in modern network architectures?",
  ["Storing all corporate data in a single central data center.", "Processing data near the edge of the network where it is generated (local devices/edge nodes) to minimize latency and bandwidth consumption.", "Using fiber optic cables exclusively.", "Replacing IPv4 with IPv6."], 1,
  "Edge Computing brings data computation and storage closer to the location of data generation (edge nodes/devices), reducing Round Trip Time latency and backhaul network bandwidth demand.")

add_q("Hard", "Advanced Topics", c(H1, H2),
  "What technology encapsulates Layer 2 Ethernet frames inside Layer 4 UDP packets (UDP port 4789) to create large virtualized overlay networks across data centers?",
  ["VLAN", "VXLAN (Virtual Extensible LAN)", "GRE", "IPsec"], 1,
  "VXLAN (Virtual Extensible LAN) encapsulates Layer 2 frames inside Layer 4 UDP packets (port 4789), extending VLAN limits from 4094 up to 16 million virtual network IDs (VNIs) for cloud data centers.")

add_q("Medium", "Advanced Topics", c(P1, P3),
  "What network metric measures the variation in packet arrival delays over a network?",
  ["Latency", "Jitter", "Throughput", "Attenuation"], 1,
  "Jitter is the packet delay variation over time. High jitter causes packet reordering and degraded quality in real-time audio/video VoIP calls.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "What is the difference between a Stateful Load Balancer and a Stateless Load Balancer?",
  ["Stateless load balancers store session cookies in RAM; Stateful load balancers do not.", "Stateful load balancers maintain connection state tables mapping clients to specific backend servers; Stateless load balancers use deterministic hashing (e.g. Consistent Hashing) to route packets without storing connection state.", "Stateless load balancers operate only at Layer 7.", "There is no difference."], 1,
  "Stateful load balancers maintain active connection state tables mapping clients to servers. Stateless load balancers route packets using deterministic hashing algorithms (e.g., 5-tuple hash), enabling ultra-high scalability without memory overhead.")

add_q("Easy", "Advanced Topics", c(S1, S2),
  "What network concept provides bandwidth guarantees and traffic prioritization for latency-sensitive applications like VoIP and video conferencing?",
  ["QoS (Quality of Service)", "NAT", "DHCP", "DNSSEC"], 0,
  "Quality of Service (QoS) uses traffic classification, queuing, and prioritization (e.g., DiffServ / DSCP bits) to ensure predictable network performance for voice and video traffic.")

add_q("Hard", "Advanced Topics", c(P1, P2),
  "In Service Mesh architectures (e.g. Istio / Envoy), how is traffic management and mutual TLS (mTLS) security enforced between microservices?",
  ["Through central switch hardware.", "By injecting a lightweight Sidecar Proxy container (e.g. Envoy) alongside each microservice container to intercept and manage all incoming/outgoing network traffic.", "By modifying the Linux kernel source code.", "Using DNS CNAME records."], 1,
  "Service Meshes use the Sidecar Proxy pattern: an Envoy proxy container runs alongside each application container in the same Pod, handling mutual TLS (mTLS) encryption, tracing, rate limiting, and traffic routing transparently.")


# ==============================================================================
# SAVE AND VALIDATE DATASET
# ==============================================================================
print(f"Total questions generated: {len(questions)}")

# Difficulty counts
easy_c = sum(1 for q in questions if q['difficulty'] == 'Easy')
med_c = sum(1 for q in questions if q['difficulty'] == 'Medium')
hard_c = sum(1 for q in questions if q['difficulty'] == 'Hard')

print(f"Difficulty Breakdown: Easy={easy_c}, Medium={med_c}, Hard={hard_c}")

# Save to questionBank.json
with open('questionBank.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print("Saved questionBank.json successfully!")
