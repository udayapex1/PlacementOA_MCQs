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

def c(g1, g2):
    return list(dict.fromkeys(g1[:2] + g2[:2]))

# Unit 1 & OSI (15 Qs)
add_q("Easy", "OSI Model", c(S1, S2),
  "Which layer of the OSI model is responsible for end-to-end communication, segmentation, flow control, and error recovery?",
  ["Data Link Layer", "Network Layer", "Transport Layer", "Session Layer"], 2,
  "The Transport Layer (Layer 4) provides transparent, reliable end-to-end data transfer between source and destination processes through segmentation, flow control, and error control.")

add_q("Easy", "Network Topologies", c(S1, S3),
  "In a Star topology, what happens if a single client workstation cable gets disconnected?",
  ["The entire network crashes immediately.", "Only that specific workstation loses network access.", "The central switch shuts down.", "Data packets begin colliding on all ports."], 1,
  "In a Star topology, each device has an independent point-to-point connection to a central device (switch). A failure in one cable isolates only that connected node.")

add_q("Medium", "Network Topologies", c(H1, S1),
  "How many full-duplex physical links are required to connect 12 routers in a fully connected Mesh topology?",
  ["12", "66", "132", "144"], 1,
  "For N nodes in a full mesh topology, total duplex links = N(N - 1) / 2. For N = 12: 12 * 11 / 2 = 66 links.")

add_q("Easy", "Network Topologies", c(S2, S3),
  "Which network topology relies on a single central linear coaxial cable called a backbone terminated at both ends?",
  ["Ring Topology", "Bus Topology", "Star Topology", "Mesh Topology"], 1,
  "Bus topology uses a shared single cable (backbone) to which all network nodes connect via drop lines. Terminators at both ends absorb signal reflections.")

add_q("Medium", "Network Components", c(H1, H2),
  "What is the key functional difference between a Layer 2 Switch and a Layer 3 Switch?",
  ["Layer 2 switches support fiber optics while Layer 3 switches support only copper.", "Layer 2 switches filter frames using MAC addresses, whereas Layer 3 switches inspect IP addresses to route packets between VLANs at hardware speeds.", "Layer 2 switches operate at the Network layer while Layer 3 switches operate at the Physical layer.", "Layer 2 switches eliminate broadcast domains while Layer 3 switches expand collision domains."], 1,
  "Layer 2 switches forward frames within a single broadcast domain using MAC table lookups. Layer 3 switches combine switching with hardware-based IP routing capabilities (ASICs).")

add_q("Easy", "Network Components", c(S1, S2),
  "Which device operates strictly at Layer 1 (Physical Layer) of the OSI model and broadcasts all incoming bits to every connected port?",
  ["Network Switch", "Hub", "Router", "Firewall"], 1,
  "A Hub is a Layer 1 multiport repeater that receives electrical/optical signals and regenerates them out of all other ports without reading MAC or IP addresses.")

add_q("Medium", "Network Components", c(H2, H1),
  "Why is a Gateway considered a Layer 7 (Application) device compared to a standard Router?",
  ["Because Gateways cannot process IP addresses.", "Because Gateways convert data protocols between completely different network architectures and application data formats.", "Because Gateways only handle physical signal amplification.", "Because Gateways use MAC addresses exclusively."], 1,
  "While routers connect networks operating on the same network protocol (IP), a Gateway translates protocols across all 7 layers.")

add_q("Easy", "PAN/LAN/MAN/WAN", c(S1, S2),
  "Bluetooth (IEEE 802.15.1) connections between a smartwatch and a smartphone form which type of network?",
  ["LAN (Local Area Network)", "PAN (Personal Area Network)", "MAN (Metropolitan Area Network)", "SAN (Storage Area Network)"], 1,
  "A PAN (Personal Area Network) covers a short range (typically under 10 meters) around an individual person.")

add_q("Medium", "VPN", c(S3, P3),
  "What primary protocol mechanism allows a Virtual Private Network (VPN) to securely send private corporate traffic over the public internet?",
  ["Dynamic Host Configuration", "Tunneling and Encapsulation (e.g., IPsec/OpenVPN) combined with Encryption", "CSMA/CD Collision Detection", "Stateless Packet Filtering"], 1,
  "VPNs use tunneling protocols (such as IPsec, OpenVPN, or WireGuard) to encapsulate private network packets inside public IP packets, encrypting the payload.")

add_q("Easy", "Network Topologies", c(S1, S2),
  "What major disadvantage is associated with a Ring network topology without FDDI dual rings?",
  ["High cost of cabling compared to Mesh.", "A break in any single point of the cable or node failure breaks the entire ring loop.", "Heavy signal interference from central switches.", "Requires manual assignment of MAC addresses."], 1,
  "In a basic single-ring topology, data tokens pass sequentially from node to node in one direction. A single cable break or failed host breaks the loop.")

add_q("Medium", "OSI Model", c(P1, P3),
  "During data encapsulation, what is the Protocol Data Unit (PDU) called at Layer 2 (Data Link Layer)?",
  ["Datagram", "Segment", "Packet", "Frame"], 3,
  "At Layer 2 (Data Link), the PDU is called a Frame (containing header, payload, and trailer with CRC).")

add_q("Medium", "OSI Model", c(H1, P2),
  "At which OSI layer do data compression, character encoding (ASCII/Unicode), and payload encryption take place?",
  ["Application Layer", "Presentation Layer", "Session Layer", "Transport Layer"], 1,
  "The Presentation Layer (Layer 6) acts as the data translator, handling syntax formatting, data compression, and encryption/decryption.")

add_q("Hard", "OSI Model", c(P1, P2),
  "A web application receives an HTTP response, but cannot insert dialogue checkpoints to resume an interrupted file download. Which OSI layer's theoretical responsibility is missing?",
  ["Transport Layer", "Session Layer", "Presentation Layer", "Network Layer"], 1,
  "The Session Layer (Layer 5) is theoretically responsible for establishing, managing, synchronizing, and inserting checkpoints into ongoing dialogues between application processes.")

add_q("Easy", "TCP/IP Model", c(S1, S2),
  "How many layers are defined in the modern 5-layer TCP/IP reference model used in computer science textbooks?",
  ["3", "4", "5", "7"], 2,
  "The modern 5-layer TCP/IP reference model consists of: Application, Transport, Network (Internet), Data Link, and Physical layers.")

add_q("Medium", "TCP/IP Model", c(H1, S3),
  "Which layer of the 4-layer DoD TCP/IP model corresponds directly to the combination of OSI Physical and Data Link layers?",
  ["Internet Layer", "Network Access / Host-to-Network Layer", "Transport Layer", "Application Layer"], 1,
  "The Network Access layer (Host-to-Network) in the classic 4-layer TCP/IP architecture covers hardware protocols, physical media, device drivers, and MAC framing.")

print("Base loaded.")
