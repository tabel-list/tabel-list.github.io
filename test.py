def multiply_and_adjust(x):
    result = x * 100
    
    # Если дробная часть равна 0, то оставляем только целую часть
    if result.is_integer():
        return int(result)  # Преобразуем в целое число
    else:
        return result  # Оставляем с плавающей точкой

# Примеры:
print(multiply_and_adjust(0.096))  # 20
print(multiply_and_adjust(0.205))  # 20.5
