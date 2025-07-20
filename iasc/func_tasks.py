def hello_world():
    print("Hello, world!")

def greet(name):
    print(f"Привіт, {name}!")

def square(n):
    return n ** 2

def add(a, b):
    return a + b

def greet_default(name="Гість"):
    print(f"Привіт, {name}!")

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(n):
    return n % 2 == 0

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

def find_name(name, name_list):
    return name in name_list

def max_of_three(a, b, c):
    return max(a, b, c)

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouаеєиіїоуюя"
    return sum(1 for char in s.lower() if char in vowels)

def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()