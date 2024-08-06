def is_armstrong(number) :
    digits = str(number)
    num_digit = len(digits)
    total = 0
    for digit in digits :
        total =  total + int(digit)**num_digit
    if total == number :
        return True
    else :
        return False 