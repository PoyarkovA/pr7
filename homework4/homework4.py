def is_valid_number(value):
    try:
        float(value.replace(',', '.')) 
        return True
    except ValueError:
        return False

def get_number(prompt):
    value = input(prompt)
    if is_valid_number(value):
        return float(value.replace(',', '.'))
    else:
        print("Ошибка: введите корректное число.")
        return get_number(prompt) 

a = get_number("Введите значение a: ")
b = get_number("Введите значение b: ")
c = get_number("Введите значение c: ")

x = 7 * b + 2 * c - a

print(f"Результат: x = {x}")
