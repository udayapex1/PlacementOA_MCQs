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

def c(g1, g2):
    return list(dict.fromkeys(g1[:2] + g2[:2]))

S1 = ["TCS", "Infosys", "Accenture"]
S2 = ["Wipro", "Cognizant", "Capgemini"]
S3 = ["LTIMindtree", "Tech Mahindra", "HCL", "Deloitte", "IBM"]
P1 = ["Amazon", "Microsoft", "Google"]
P2 = ["Meta", "Adobe", "Oracle", "SAP"]
P3 = ["ServiceNow", "Atlassian", "Goldman Sachs", "JPMorgan", "PayPal"]
P4 = ["Flipkart", "Walmart Global Tech", "Visa", "Mastercard"]
H1 = ["Cisco", "Qualcomm", "Samsung"]
H2 = ["Nvidia", "Intel", "Juniper Networks", "Arista Networks", "VMware"]

# Load initial 15
import generate_final_bank
questions = generate_final_bank.questions
print(f"Loaded {len(questions)} base questions.")

