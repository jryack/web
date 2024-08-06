ets1 = int(input("Enter the score for test 1:"))
ets2 = int(input("Enter the score for test 2 "))
ets3 = int(input("Enter the score for test 3 "))

average = (ets1 + ets2 + ets3)/3
print("The average score is",average)

if average > 96:
    print("That is great average!",average )