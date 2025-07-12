contacts = {
    "Anna": "093-123-45-67",
    "Ivan": "050-888-99-00",
    "Olha": "097-777-33-22"
}

contacts["Taras"] = "063-000-11-22"

del contacts["Ivan"]

print("Імена у телефонній книзі:", list(contacts.keys()))
print("Номери у телефонній книзі:", list(contacts.values()))
print("Katya є у телефонній книзі?", "Katya" in contacts)

grades = {
    "math": 88,
    "physics": 75,
    "english": 93,
    "history": 59
}

max_subject = max(grades, key=grades.get)
print("Найвища оцінка з предмету:", max_subject)

average_grade = sum(grades.values()) / len(grades)
print("Середній бал:", average_grade)

high_scores = [subject for subject, score in grades.items() if score > 80]
print("Предмети з оцінкою > 80:", high_scores)

transactions = [
    ("Anna", 200),
    ("Ivan", -50),
    ("Anna", 100),
    ("Olha", 500),
    ("Ivan", 150),
    ("Olha", -100),
]

balances = {}
for name, amount in transactions:
    balances[name] = balances.get(name, 0) + amount

print("Баланс клієнтів:", balances)

richest = max(balances, key=balances.get)

print("Клієнт з найбільшим балансом:", richest)

negative_balances = [name for name, balance in balances.items() if balance < 0]

print("Клієнти з від'ємним балансом:", negative_balances)

text = "hello world hello again hello world test world"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Підрахунок слів:", word_count)

import json

student = {
    "name": "Anna",
    "age": 20,
    "courses": ["math", "physics", "english"]
}

student_json = json.dumps(student)
print("JSON-рядок:", student_json)
student_dict = json.loads(student_json)
student_dict["courses"].append("history")
print("Оновлений словник:", student_dict)