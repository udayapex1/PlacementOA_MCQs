import json

# Master script to generate 250 Operating System MCQs

questions = []

def add(topic, difficulty, companies, question, options, answer, explanation):
    global questions
    questions.append({
        "id": len(questions) + 1,
        "difficulty": difficulty,
        "topic": topic,
        "companyPattern": companies,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation
    })

# We will populate all 250 questions systematically across 13 topics.

print("Starting generation of 250 OS Questions...")
