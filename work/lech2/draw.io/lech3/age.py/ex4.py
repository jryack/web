print("Please select operation ")

print("1.Add ")#+
print("2.Subtract")#-
print("3.Multipy")#*
print("Divide")#/
Selec = int(input("Select operations form 1, 2, 3, 4 : "))
if Selec >= 5 :
    print("Wrong choice ")
    exit()
E1 = int(input("Enter first number :")) 
E2 = int(input("Enter second number :"))
if Selec in[1,2,3,4]:

    if Selec == 1 :
        print(E1+E2) 
    
    elif Selec == 2 :
        print(E1-E2) 

    elif Selec == 3 :
        print(E1*E2) 

elif Selec == 4 :
    print(E1/E2) 


