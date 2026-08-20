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

SERVICE = ["TCS", "Infosys", "Wipro", "Accenture", "Cognizant", "Capgemini", "LTIMindtree", "Tech Mahindra", "HCL", "Deloitte", "IBM"]
PRODUCT = ["Amazon", "Microsoft", "Google", "Meta", "Adobe", "Oracle", "SAP", "ServiceNow", "Atlassian", "Goldman Sachs", "JPMorgan", "PayPal", "Flipkart", "Walmart Global Tech", "Visa", "Mastercard"]
HARDWARE = ["Cisco", "Qualcomm", "Samsung", "Nvidia", "Intel", "Juniper Networks", "Arista Networks", "VMware"]

print("Building question database...")
