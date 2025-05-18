import random # Модуль для случайного выбора
import string # Модуль в котором содержатся буквы и цифры
import pyperclip # Модуль для копирования в буфер обмена

def generate_password(length, use_upper, use_lower, use_digits, use_symbols): # Функция для генерации пароля с 5 параметрами
    characters = "" # Изначально символов для пароля нет
    if use_upper: # Если используем заглавные буквы, то в символы для пароля добавляются загл. буквы
        characters += string.ascii_uppercase
    if use_lower: # Если используем прописные буквы, то в символы для пароля добавляются прописные буквы
        characters += string.ascii_lowercase
    if use_digits: # Если используем цифры, то в символы для пароля добавляются цифры
        characters += string.digits
    if use_symbols: # Если используем спец. символы, то в символы для пароля добавляются спец. символы
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if not characters: # Если не были выбраны символы для пароля, то вызывается исключение ValueError
        raise ValueError("Не выбраны символы для генерации пароля.")

    # Обеспечить наличие хотя бы одного символа каждого выбранного типа
    password_chars = []

    if use_upper: # Если используем заглавные буквы, то добавляется случайная загл. буква
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lower: # Если используем прописные буквы, то добавляется случайная прописная буква
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_digits: # Если используем цифры, то добавляется случайная цифра
        password_chars.append(random.choice(string.digits))
    if use_symbols: # Если используем спец. символы, то добавляется случайный спец. символ
        password_chars.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/"))

    # Остальные символы
    remaining_length = length - len(password_chars) # Из числа символов пароля вычитаем число символов которые уже есть в пароле
    password_chars += random.choices(characters, k=remaining_length) # Случайный выбор из символов для пароля, k - число символов которые выбираются

    # Перемешать для случайности
    random.shuffle(password_chars)

    # Итоговый пароль
    password = ''.join(password_chars)
    return password # Возвращаем значение пароля

def main(): # Функция для самой программы
    print("Добро пожаловать в генератор паролей!\n")
    try: # Проверка правильности ввода данных (целое число)
        length = int(input("Введите длину пароля: "))
    except ValueError: # Если было введено не целое число, то длина пароля задается 12
        print("Некорректный ввод. Устанавливаем длину 12.")
        length = 12

    use_upper = input("Включать ли заглавные буквы? (да/нет): ").lower() == 'да' # Если введеное значение - да, то используем загл. буквы (переменная - True)
    use_lower = input("Включать ли строчные буквы? (да/нет): ").lower() == 'да' # Если введеное значение - да, то используем прописные буквы (переменная - True)
    use_digits = input("Включать ли цифры? (да/нет): ").lower() == 'да' # Если введеное значение - да, то используем цифры (переменная - True)
    use_symbols = input("Включать ли специальные символы? (да/нет): ").lower() == 'да' # Если введеное значение - да, то используем спец. символы (переменная - True)

    try: # Проверка правильности
        # Вызываем функцию генерации пароля, передавая 5 аргументов, и возвращенное значение будет в переменной password
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nВаш надежный пароль: {password}") # Выводим получившийся пароль
        # Копирование в буфер обмена
        pyperclip.copy(password)
        print("Пароль скопирован в буфер обмена!")
    except ValueError as e: # При ошибке сообщаем об этом
        print(f"Ошибка: {e}")

main()