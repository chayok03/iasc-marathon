my_list = ["молоко", "хліб", "яйця", "сир", "яблука"]
print(my_list)
my_list.append("кава")
print(my_list)

list_grades = [9, 11, 12, 5, 7, 8]
print(list_grades)
averege_grade = sum(list_grades) / len(list_grades)
print(averege_grade)

names = ["Оля", "Ігор", "Андрій", "Марія", "Богдан"]
names.sort()
print(names)

cities = ["Київ", "Львів", "Хмельницький", "Житомир", "Чернігів"]
cities[1] = "Чернігів"
print(cities)
print(cities[0])
print(cities[-1])

anime_list = ["Naruto", "Killer Seven", "Death Note", "Bleach", "One Piece"]
print(anime_list)
print(len(anime_list))
anime_list.remove("Bleach")
print(anime_list)
anime_list.sort()
anime_list.reverse()
print(anime_list)
