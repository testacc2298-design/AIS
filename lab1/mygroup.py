groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]

def filter_by_average_mark_v2(students, min_avg):
    result = list(filter(
        lambda s: (sum(s["marks"]) / len(s["marks"])) > min_avg,
        students
    ))

    if not result:
        print(f"\nНет студентов со средним баллом выше {min_avg}.")
        return

    print(f"\nСтуденты со средним баллом выше {min_avg}:\n")
    print(f"{'Имя':<15} {'Фамилия':<12} {'Средний балл':<15} {'Оценки'}")
    print("-" * 60)

    for s in result:
        avg = sum(s["marks"]) / len(s["marks"])
        marks_str = ", ".join(str(m) for m in s["marks"])
        print(f"{s['name']:<15} {s['surname']:<12} {avg:<15.2f} {marks_str}")

threshold = float(input("Введите минимальный средний балл: "))
filter_by_average_mark_v2(groupmates, threshold)
