import json

questions = []

def q(topic, difficulty, companies, question, options, answer_idx, explanation):
    questions.append({
        "id": len(questions) + 1,
        "difficulty": difficulty,
        "topic": topic,
        "companyPattern": companies,
        "question": question,
        "options": options,
        "answer": answer_idx,
        "explanation": explanation
    })

print("Generating 250 OS Questions...")
