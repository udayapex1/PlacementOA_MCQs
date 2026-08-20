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

# Load base 15
import generate_questions_dataset
questions = generate_questions_dataset.questions

# ==============================================================================
# 2. PHYSICAL LAYER (20 Qs total, Q16 - Q35)
# ==============================================================================
add_q("Medium", "Physical Layer", c(H1, H2),
  "According to Nyquist's Theorem, what is the maximum bit rate for a noiseless channel with a bandwidth of 4 kHz carrying signals with 8 discrete voltage levels?",
  ["12 kbps", "24 kbps", "32 kbps", "64 kbps"], 1,
  "Nyquist Bit Rate = 2 * Bandwidth * log2(L). Here Bandwidth B = 4000 Hz, L = 8 levels (log2(8) = 3). Bit Rate = 2 * 4000 * 3 = 24,000 bps = 24 kbps.")

add_q("Hard", "Physical Layer", c(P1, H1),
  "Using Shannon's Capacity Formula, calculate the theoretical maximum data rate of a channel having a bandwidth of 2 MHz and a Signal-to-Noise Ratio (SNR) of 15.",
  ["2 Mbps", "4 Mbps", "8 Mbps", "16 Mbps"], 2,
  "Shannon Capacity C = Bandwidth * log2(1 + SNR). Given B = 2 MHz, SNR = 15. C = 2 * 10^6 * log2(1 + 15) = 2 * 10^6 * log2(16) = 2 * 10^6 * 4 = 8 Mbps.")

add_q("Easy", "Physical Layer", c(S1, S2),
  "Which transmission medium uses total internal reflection to transmit data as pulses of light with high bandwidth and immunity to EMI?",
  ["Shielded Twisted Pair (STP)", "Coaxial Cable", "Optical Fiber Cable", "Unshielded Twisted Pair (UTP)"], 2,
  "Optical Fiber cables convey light pulses along a ultra-pure glass core using total internal reflection, offering immune transmission against electromagnetic interference (EMI).")

add_q("Medium", "Physical Layer", c(H1, H2),
  "What is the key advantage of Manchester Encoding used in classic Ethernet?",
  ["It doubles the data transmission speed without increasing bandwidth.", "It guarantees a transition at the middle of every bit interval, providing built-in clock synchronization.", "It eliminates attenuation entirely over copper wires.", "It uses four different voltage levels to encode 2 bits per baud."], 1,
  "In Manchester encoding, every bit duration has a transition at the midpoint (low-to-high for 1, high-to-low for 0). This transition provides self-clocking synchronization for the receiver.")

add_q("Easy", "Physical Layer", c(S1, S3),
  "The gradual reduction in signal strength (amplitude) as it travels through a physical transmission medium is known as:",
  ["Distortion", "Attenuation", "Crosstalk", "Thermal Noise"], 1,
  "Attenuation is the weakening of a signal over distance due to electrical resistance or light scattering in physical media. Repeaters or amplifiers are used to boost attenuated signals.")

add_q("Hard", "Physical Layer", c(H1, H2),
  "If a channel has a Signal-to-Noise Ratio expressed as 20 dB, what is its linear SNR ratio value?",
  ["20", "100", "200", "1000"], 1,
  "SNR_dB = 10 * log10(SNR). 20 = 10 * log10(SNR) => log10(SNR) = 2 => linear SNR = 10^2 = 100.")

add_q("Medium", "Physical Layer", c(S2, S3),
  "Which twisted pair cable category supports data rates up to 10 Gbps at 500 MHz over distances up to 100 meters?",
  ["Category 5 (Cat5)", "Category 5e (Cat5e)", "Category 6a (Cat6a)", "Category 3 (Cat3)"], 2,
  "Cat6a (Category 6 Augmented) supports 10 Gbps speed up to 100 meters at frequencies up to 500 MHz, featuring tighter twists and shielding to reduce crosstalk.")

add_q("Easy", "Physical Layer", c(S1, S2),
  "What type of signal impairment is caused by unwanted coupling between adjacent wire pairs running in parallel within a cable bundle?",
  ["Attenuation", "Crosstalk", "Dispersion", "Thermal Noise"], 1,
  "Crosstalk occurs when electromagnetic interference from one wire pair leaks into an adjacent wire pair due to mutual inductance or capacitive coupling.")

add_q("Hard", "Physical Layer", c(H1, P1),
  "Calculate the Bandwidth-Delay Product for a 1 Gbps cross-country link with a one-way propagation delay of 40 milliseconds.",
  ["40 KB", "5 MB", "40 MB", "50 MB"], 1,
  "Bandwidth-Delay Product = Bandwidth * Delay. 1 Gbps = 10^9 bits/sec. Delay = 0.040 sec. Product = 10^9 * 0.040 = 40,000,000 bits. Divided by 8 = 5,000,000 bytes = 5 MB.")

add_q("Easy", "Physical Layer", c(S1, S3),
  "Which multiplexing technique divides the available frequency spectrum into smaller frequency channels allocated concurrently to different users?",
  ["TDM (Time Division Multiplexing)", "FDM (Frequency Division Multiplexing)", "WDM (Wavelength Division Multiplexing)", "CDM (Code Division Multiplexing)"], 1,
  "Frequency Division Multiplexing (FDM) divides the total bandwidth into distinct non-overlapping frequency bands assigned simultaneously to separate signals.")

add_q("Medium", "Physical Layer", c(H1, H2),
  "In Optical Fiber transmission, what parameter distinguishes Single-Mode Fiber (SMF) from Multi-Mode Fiber (MMF)?",
  ["SMF has a larger core diameter allowing multiple light paths.", "SMF has a much smaller core (~8-10 microns) allowing only a single light mode to propagate, reducing modal dispersion over long distances.", "SMF uses copper shielding instead of glass cladding.", "SMF is restricted to local area networks under 100 meters."], 1,
  "Single-Mode Fiber (SMF) has a narrow core (~9 µm) allowing a single beam of laser light to travel straight down the center, eliminating modal dispersion and enabling trans-oceanic distances.")

add_q("Medium", "Physical Layer", c(S2, P4),
  "What is the difference between Baseband and Broadband transmission?",
  ["Baseband uses analog modulation; Broadband uses digital square waves.", "Baseband transmits digital signals directly over the entire channel bandwidth without modulation; Broadband modulates signals onto analog carrier frequencies allowing multiple channels.", "Baseband requires satellite links; Broadband uses copper wires.", "Baseband supports wireless; Broadband is strictly wired."], 1,
  "Baseband transmission sends digital signals using the full bandwidth of the physical medium as unmodulated pulses (e.g., Ethernet). Broadband modulates signals onto distinct analog carrier frequencies (e.g., DSL/Cable).")

add_q("Hard", "Physical Layer", c(H1, H2),
  "A PCM (Pulse Code Modulation) system samples an audio signal at 8 kHz with 8-bit quantization. What is the resulting digital bit rate?",
  ["8 kbps", "16 kbps", "64 kbps", "128 kbps"], 2,
  "PCM Bit Rate = Sampling Rate * Bits per Sample = 8,000 samples/sec * 8 bits/sample = 64,000 bps = 64 kbps (standard DS0 channel rate).")

add_q("Easy", "Physical Layer", c(S1, S2),
  "Which wireless transmission frequency range is un-licensed and shared globally by Wi-Fi, Bluetooth, and microwave ovens?",
  ["800 MHz", "2.4 GHz ISM band", "10 GHz", "60 GHz"], 1,
  "The 2.4 GHz Industrial, Scientific, and Medical (ISM) band is an unlicensed frequency band used worldwide by Wi-Fi (802.11b/g/n), Bluetooth, ZigBee, and cordless phones.")

add_q("Medium", "Physical Layer", c(H1, P1),
  "What does the term 'Baud Rate' represent in data communication compared to 'Bit Rate'?",
  ["Baud Rate is the number of error bits detected per second.", "Baud Rate is the number of signal symbol changes per second, whereas Bit Rate is the number of actual bits transmitted per second.", "Baud Rate is always double the Bit Rate.", "Baud Rate measures link latency in milliseconds."], 1,
  "Baud rate measures symbol transitions (signal changes) per second. If each symbol carries multiple bits (e.g., QAM-16 encodes 4 bits per symbol), Bit Rate = Baud Rate * bits per symbol.")

add_q("Easy", "Physical Layer", c(S2, S3),
  "Which connector type is standard for terminating Cat5e/Cat6 Ethernet patch cables?",
  ["RJ-11", "RJ-45", "BNC", "ST Connector"], 1,
  "RJ-45 (Registered Jack 45) is the standard 8-position, 8-contact (8P8C) modular connector used for Ethernet networking cables.")

add_q("Hard", "Physical Layer", c(H1, H2),
  "What signal encoding scheme uses non-zero positive and negative voltage levels to represent bits and includes a transition at the beginning of a 0 bit but no transition for a 1 bit?",
  ["NRZ-L", "Differential Manchester", "AMI (Alternate Mark Inversion)", "NRZI (Non-Return-to-Zero Inverted)"], 1,
  "Differential Manchester encoding always transitions at the middle of the bit interval for clocking, but the presence of a transition at the beginning of the bit interval indicates a binary 0, while no transition indicates a binary 1.")

add_q("Medium", "Physical Layer", c(S1, P3),
  "Throughput of a network link is best defined as:",
  ["The theoretical maximum capability of a link under ideal conditions.", "The actual rate of successful data delivery over a channel measured over time.", "The time required for a packet to travel from source to destination.", "The total length of physical fiber optic cables."], 1,
  "Bandwidth is the theoretical maximum physical capacity, whereas Throughput is the actual rate of successful data delivery taking into account overhead, collisions, error retransmissions, and network congestion.")

add_q("Easy", "Physical Layer", c(S2, S3),
  "What component converts digital signals from a computer into analog signals for transmission over telephone lines and vice versa?",
  ["Router", "Modem (Modulator-Demodulator)", "Switch", "Hub"], 1,
  "A Modem (Modulator-Demodulator) modulates outgoing digital bits into analog carrier signals for transmission over analog lines and demodulates incoming analog signals back into digital data.")

add_q("Hard", "Physical Layer", c(H1, H2),
  "Calculate the propagation delay of a packet traveling through a 2,000 km optical fiber cable assuming a propagation speed of 2 x 10^8 m/s.",
  ["1 ms", "10 ms", "100 ms", "1 sec"], 1,
  "Propagation Delay = Distance / Speed = 2,000,000 meters / (2 x 10^8 m/s) = 2/200 = 0.01 seconds = 10 milliseconds.")

print(f"Current Q count: {len(questions)}")
