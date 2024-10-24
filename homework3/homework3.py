def decimal_to_base13(n):
    digits = '0123456789ABC'

    if n < 0:
        return '-' + decimal_to_base13(-n)
    elif n == 0:
        return '0'
    
    remainder = n % 13
    return decimal_to_base13(n // 13) + digits[remainder]

def get_valid_input():
    user_input = input("Введите число: ")
    try:
        decimal_number = float(user_input)
        return decimal_number
    except ValueError:
        print("Ошибка: введите корректное число (можно отрицательное и дробное).")
        return get_valid_input() 

decimal_number = get_valid_input()

base13_number = decimal_to_base13(int(decimal_number))

print(f"Число {decimal_number} в тринадцатеричной системе: {base13_number}")
