students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]

max_grade = max(grades)
max_student = students[grades.index(max_grade)]
print(f"Найвища оцінка у: {max_student}")

passed_students = [students[i] for i in range(len(students)) if grades[i] > 60]
print(f"Студенти з оцінкою > 60: {passed_students}")

failed_count = len([g for g in grades if g < 60])
print(f"Не склали: {failed_count}")

logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
unique_logs = set(logs)
for log in unique_logs:
    print(f"{log}: {logs.count(log)}")

error_percent = logs.count("error") / len(logs) * 100
print(f"Відсоток error: {error_percent:.2f}%")

print("-" * 50)

expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]

max_day = max(expenses, key=lambda x: x[1])
print(f"Найбільші витрати були у {max_day[0]}: {max_day[1]} грн")

total_expenses = sum([day[1] for day in expenses])
print(f"Загальні витрати за тиждень: {total_expenses} грн")
days_over_100 = [day[0] for day in expenses if day[1] > 100]
print(f"Дні з витратами понад 100 грн: {days_over_100}")

print("-" * 50)

products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]

total_check = sum([item[1] * item[2] for item in products])
print(f"Загальна сума чеку: {total_check} грн")
most_expensive = max(products, key=lambda x: x[2])
print(f"Найдорожчий товар за одиницю: {most_expensive[0]} - {most_expensive[2]} грн")

summary_list = [f"{item[0]} - {item[1] * item[2]} грн" for item in products]
print("Список товарів та сум:")
for line in summary_list:
    print(line)

print("-" * 50)

squares = [x**2 for x in range(1, 31) if x % 2 == 0 and x % 4 != 0 and x not in [10, 14, 18]]
print(f"Квадрати з умовою: {squares}")




