

## Функция для создания пароля для заданного числа
def generate_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0 and i + j == n:  # Добавляем проверку на сумму
                password += str(i) + str(j)
    return password

# Создание паролей для чисел от 3 до 20
for num in range(3, 21):
    print("_______________________________________________________________________________")
    num = int(input("Введите число от 3 до 20: "))
    if 3 < num > 20:
        print("ОШИБКА! Число должно быть от 3 до 20.")
        continue
    password = generate_password(num)
    if 3 <= num <= 20:
        print(f"Пароль для числа {num}: {password}")

