import json

questions = []

def add_q(difficulty, topic, companyPattern, question, options, answer, explanation):
    qid = len(questions) + 1
    # Sanity checks
    assert difficulty in ["Easy", "Medium", "Hard"], f"Invalid difficulty {difficulty} in Q{qid}"
    assert len(options) == 4, f"Options count must be 4 in Q{qid}"
    assert 0 <= answer <= 3, f"Answer index out of range in Q{qid}"
    assert len(explanation) >= 20, f"Explanation too short in Q{qid}"
    
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

# Company pools
SERVICE = ["TCS", "Infosys", "Wipro", "Accenture", "Cognizant", "Capgemini", "LTIMindtree", "Tech Mahindra", "HCL", "Deloitte", "IBM"]
PRODUCT = ["Amazon", "Microsoft", "Google", "Meta", "Adobe", "Oracle", "SAP", "ServiceNow", "Atlassian", "Goldman Sachs", "JPMorgan", "PayPal", "Flipkart", "Walmart Global Tech", "Visa", "Mastercard"]
HARDWARE = ["Cisco", "Qualcomm", "Samsung", "Nvidia", "Intel", "Juniper Networks", "Arista Networks", "VMware"]

def c(*lists):
    res = []
    for l in lists:
        res.extend(l[:2])
    return list(dict.fromkeys(res))

# ==============================================================================
# UNIT 1: INTRODUCTION & TOPOLOGIES & COMPONENTS (1-20)
# ==============================================================================
add_q("Easy", "OSI Model", ["TCS", "Infosys", "Accenture"],
  "Which OSI model layer is responsible for end-to-end communication, segmentation, flow control, and error recovery?",
  ["Data Link Layer", "Network Layer", "Transport Layer", "Session Layer"], 2,
  "The Transport Layer (Layer 4) provides transparent, reliable end-to-end data transfer between source and destination processes through segmentation, flow control, and error control. Data Link handles hop-to-hop framing, Network manages routing, and Session handles session dialogues.")

add_q("Easy", "Network Topologies", ["Wipro", "Capgemini", "TCS"],
  "In a Star topology, what happens if a single client workstation cable gets disconnected?",
  ["The entire network crashes immediately.", "Only that specific workstation loses network access.", "The central switch shuts down.", "Data packets begin colliding on all ports."], 1,
  "In a Star topology, each device has an independent point-to-point connection to a central device (switch). A failure in one cable isolates only that connected node. Ring or Bus topologies fail entirely upon a single link break.")

add_q("Medium", "Network Topologies", ["Qualcomm", "Cisco", "TCS"],
  "How many full-duplex physical links are required to connect 12 routers in a fully connected Mesh topology?",
  ["12", "66", "132", "144"], 1,
  "For N nodes in a full mesh topology, total duplex links = N(N - 1) / 2. For N = 12: 12 * 11 / 2 = 66 links. 132 is the count for simplex links, and 144 is N^2.")

add_q("Easy", "Network Topologies", ["Infosys", "Cognizant", "HCL"],
  "Which network topology relies on a single central linear coaxial cable called a backbone terminated at both ends?",
  ["Ring Topology", "Bus Topology", "Star Topology", "Mesh Topology"], 1,
  "Bus topology uses a shared single cable (backbone) to which all network nodes connect via drop lines. Terminators at both ends absorb signal reflections preventing packet rebound.")

add_q("Medium", "Network Components", ["Cisco", "Juniper Networks", "Amazon"],
  "What is the key functional difference between a Layer 2 Switch and a Layer 3 Switch?",
  ["Layer 2 switches support fiber optics while Layer 3 switches support only copper.", "Layer 2 switches filter frames using MAC addresses, whereas Layer 3 switches inspect IP addresses to route packets between VLANs at hardware speeds.", "Layer 2 switches operate at the Network layer while Layer 3 switches operate at the Physical layer.", "Layer 2 switches eliminate broadcast domains while Layer 3 switches expand collision domains."], 1,
  "Layer 2 switches forward frames within a single broadcast domain using MAC table lookups. Layer 3 switches combine switching with hardware-based IP routing capabilities (ASICs) to route traffic between different VLANs and subnets.")

add_q("Easy", "Network Components", ["TCS", "Accenture", "Capgemini"],
  "Which device operates strictly at Layer 1 (Physical Layer) of the OSI model and broadcasts all incoming bits to every connected port?",
  ["Network Switch", "Hub", "Router", "Firewall"], 1,
  "A Hub is a Layer 1 multiport repeater that receives electrical/optical signals and regenerates them out of all other ports without reading MAC or IP addresses, creating a single shared collision domain.")

add_q("Medium", "Network Components", ["Arista Networks", "Cisco", "Dell"],
  "Why is a Gateway considered a Layer 7 (Application) device compared to a standard Router?",
  ["Because Gateways cannot process IP addresses.", "Because Gateways convert data protocols between completely different network architectures and application data formats.", "Because Gateways only handle physical signal amplification.", "Because Gateways use MAC addresses exclusively."], 1,
  "While routers connect networks operating on the same network protocol (IP), a Gateway translates protocols across all 7 layers (e.g., connecting an IP network to an SNA network or translating application payload formats).")

add_q("Easy", "PAN/LAN/MAN/WAN", ["Infosys", "Wipro", "TCS"],
  "Bluetooth (IEEE 802.15.1) connections between a smartwatch and a smartphone form which type of network?",
  ["LAN (Local Area Network)", "PAN (Personal Area Network)", "MAN (Metropolitan Area Network)", "SAN (Storage Area Network)"], 1,
  "A PAN (Personal Area Network) covers a short range (typically under 10 meters) around an individual person. LAN covers a building, MAN spans a city, and SAN connects storage devices to servers.")

add_q("Medium", "VPN", ["Deloitte", "IBM", "Accenture"],
  "What primary protocol mechanism allows a Virtual Private Network (VPN) to securely send private corporate traffic over the public internet?",
  ["Dynamic Host Configuration", "Tunneling and Encapsulation (e.g., IPsec/OpenVPN) combined with Encryption", "CSMA/CD Collision Detection", "Stateless Packet Filtering"], 1,
  "VPNs use tunneling protocols (such as IPsec, OpenVPN, or WireGuard) to encapsulate private network packets inside public IP packets, encrypting the payload to ensure confidentiality and integrity across untrusted public networks.")

add_q("Easy", "Network Topologies", ["Capgemini", "Infosys", "TCS"],
  "What major disadvantage is associated with a Ring network topology without FDDI dual rings?",
  ["High cost of cabling compared to Mesh.", "A break in any single point of the cable or node failure breaks the entire ring loop.", "Heavy signal interference from central switches.", "Requires manual assignment of MAC addresses."], 1,
  "In a basic single-ring topology, data tokens pass sequentially from node to node in one direction. A single cable break or failed host breaks the loop, disrupting communication for the whole network unless dual counter-rotating rings are implemented.")

add_q("Medium", "OSI Model", ["Amazon", "Microsoft", "Goldman Sachs"],
  "During the data encapsulation process, what is the PDU (Protocol Data Unit) called at the Data Link Layer?",
  ["Datagram", "Segment", "Packet", "Frame"], 3,
  "At Layer 2 (Data Link), the PDU is called a Frame (containing header, payload, and trailer with CRC). Layer 4 uses Segments/Datagrams, Layer 3 uses Packets, and Layer 1 uses Bits.")

add_q("Medium", "OSI Model", ["Qualcomm", "Intel", "Samsung"],
  "At which OSI layer do data compression, character encoding (ASCII/Unicode), and payload encryption take place?",
  ["Application Layer", "Presentation Layer", "Session Layer", "Transport Layer"], 1,
  "The Presentation Layer (Layer 6) acts as the data translator, handling syntax formatting, data compression, and encryption/decryption before passing payloads up to Application layer or down to Session layer.")

add_q("Hard", "OSI Model", ["Google", "Meta", "Microsoft"],
  "A web developer observes that an HTTP response has arrived, but the application cannot establish dialogue checkpoints to resume an interrupted file download. Which OSI layer's theoretical responsibility is missing here?",
  ["Transport Layer", "Session Layer", "Presentation Layer", "Network Layer"], 1,
  "The Session Layer (Layer 5) is theoretically responsible for establishing, managing, synchronizing, and inserting checkpoints into ongoing dialogues between application processes so that sessions can recover from interruptions without starting over.")

add_q("Easy", "TCP/IP Model", ["Infosys", "Wipro", "TCS"],
  "How many layers are defined in the modern 5-layer TCP/IP reference model commonly taught in networking computer science curricula?",
  ["3", "4", "5", "7"], 2,
  "The modern 5-layer TCP/IP reference model consists of: Application, Transport, Network (Internet), Data Link, and Physical layers. (The original DoD TCP/IP model had 4 layers by combining Data Link and Physical into Network Access).")

add_q("Medium", "TCP/IP Model", ["Cisco", "Oracle", "IBM"],
  "Which layer of the 4-layer DoD TCP/IP model corresponds directly to the combination of OSI Physical and Data Link layers?",
  ["Internet Layer", "Network Access / Host-to-Network Layer", "Transport Layer", "Application Layer"], 1,
  "The Network Access layer (Host-to-Network) in the classic 4-layer TCP/IP architecture covers hardware protocols, physical media, device drivers, and MAC framing—encompassing OSI Layers 1 and 2.")

add_q("Easy", "Network Components", ["Accenture", "TCS", "Cognizant"],
  "What is the main role of a Repeater in a long-distance cabling infrastructure?",
  ["To translate IP addresses to MAC addresses.", "To amplify or regenerate weak electrical/optical signals to overcome attenuation over long distances.", "To filter packets based on firewall security rules.", "To allocate dynamic IP addresses to end hosts."], 1,
  "Repeaters operate at Layer 1 to regenerate and clean distorted or attenuated signals, extending the maximum allowable physical length of transmission cables.")

add_q("Medium", "Network Topologies", ["Qualcomm", "Cisco", "Nvidia"],
  "In a Tree (Hierarchical) topology, what happens if a core distribution switch fails?",
  ["Only the host directly attached to the switch fails.", "The entire sub-tree branch connected beneath that distribution switch loses connectivity.", "The network automatically converts to a full mesh topology.", "Packets loop infinitely without TTL decrement."], 1,
  "Tree topology combines Star topologies connected to a central root. If a core/distribution switch fails, all descendant child nodes and sub-branches connected under that node lose connection to the rest of the network.")

add_q("Hard", "OSI Model", ["Amazon", "Cisco", "Google"],
  "Which scenario correctly illustrates decapsulation at the receiving host?",
  ["Adding an IP header to a TCP segment.", "Removing the Ethernet header/trailer, inspecting the IP header, removing it, and passing the TCP segment to Layer 4.", "Converting application data into binary bit streams.", "Encrypting data with SSL public key."], 1,
  "Decapsulation is the bottom-up process where a receiving host strips headers at each layer (Ethernet Frame header/trailer at L2, IP header at L3, TCP header at L4) to reconstruct the original application data payload.")

add_q("Easy", "SAN", ["Deloitte", "IBM", "Capgemini"],
  "A high-performance dedicated network designed specifically to connect block-level storage devices (disk arrays, tape libraries) to servers is known as:",
  ["LAN", "MAN", "SAN (Storage Area Network)", "PAN"], 2,
  "A Storage Area Network (SAN) is a specialized, high-speed network that provides block-level network access to storage using technologies like Fibre Channel or iSCSI.")

add_q("Medium", "Network Components", ["Cisco", "Juniper Networks", "TCS"],
  "Which device separates both collision domains and broadcast domains simultaneously?",
  ["Layer 2 Switch", "Hub", "Router", "Bridge"], 2,
  "Routers operate at Layer 3 and break both collision domains (on each interface) and broadcast domains (since routers do not forward Layer 2/3 broadcasts by default). A Layer 2 switch breaks collision domains but maintains a single broadcast domain per VLAN.")

