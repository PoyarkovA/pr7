def decimal_to_binary(integer_part):
    if integer_part == 0:
        return "0"
    elif integer_part < 0:
        return "-" + decimal_to_binary(-integer_part)
    else:
        return decimal_to_binary(integer_part // 2) + str(integer_part % 2)

def fractional_to_binary(fractional_part, depth=0):
    if depth >= 10 or fractional_part == 0: 
        return ""
    else:
        fractional_part *= 2
        bit = int(fractional_part)
        return str(bit) + fractional_to_binary(fractional_part - bit, depth + 1)

def decimal_to_octal(integer_part):
    if integer_part == 0:
        return "0"
    elif integer_part < 0:
        return "-" + decimal_to_octal(-integer_part)
    else:
        return decimal_to_octal(integer_part // 8) + str(integer_part % 8)

def fractional_to_octal(fractional_part, depth=0):
    if depth >= 10 or fractional_part == 0: 
        return ""
    else:
        fractional_part *= 8
        digit = int(fractional_part)
        return str(digit) + fractional_to_octal(fractional_part - digit, depth + 1)

def get_decimal_number():
    user_input = input("Введите число: ").replace(',', '.')  
    try:
        return float(user_input)  
    except ValueError:
        print("Ошибка: необходимо ввести число.")
        return None  

def convert_number():
    decimal_number = get_decimal_number()  
    if decimal_number is None:
        return  

    is_negative = decimal_number < 0
    decimal_number = abs(decimal_number)  

    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    binary_integer = decimal_to_binary(integer_part)
    binary_fractional = fractional_to_binary(fractional_part)
    binary_result = f"{binary_integer}.{binary_fractional}"

    octal_integer = decimal_to_octal(integer_part)
    octal_fractional = fractional_to_octal(fractional_part)
    octal_result = f"{octal_integer}.{octal_fractional}"

    if is_negative:
        binary_result = "-" + binary_result
        octal_result = "-" + octal_result

    print(f"Двоичное представление: {binary_result}")
    print(f"Восьмеричное представление: {octal_result}")

convert_number()