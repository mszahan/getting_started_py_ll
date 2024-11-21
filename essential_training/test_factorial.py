def factorial(num):
    if num < 0:
        return None
    if num % 1 !=0:
        return None
    if str(num) == num:
        return None
    
    mul = 1
    while num > 1:
        mul = mul * num * (num-1)
        num = num-2
    return mul


print(factorial(0))

