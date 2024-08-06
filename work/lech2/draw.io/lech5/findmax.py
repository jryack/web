def findmax(*args):
    if not args:
        return None
    Max_value = args[0]
    for number in args :
        if number > Max_value :
            Max_value = number
            return Max_value
        
result = findmax(3,7,2,8)
print(f"The maximum value is: {result}")
