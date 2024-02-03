print("\t\t\tSimple calculator ".upper())
print("\nEnter Two Numbers to perform operations like addition, subtraction, multiplication, division".capitalize())

a=float(input("\nEnter the first number : "))
b = float(input("\nEnter the second number : "))

while (a,b)!=0 :
    print("\nSelect the operation to  perform \n\n 1.Addition\t2.subtraction\t3.multiplication\t4.division")
    opt=input("\nEnter option: ".lower())
    if opt =="add" or opt=="addition" or opt=="1":
        print(f"\nResult of adding {a} and {b} = ",a+b)
        print("\n\t\t\t\t press Q to quit")
    elif opt == "sub" or opt=="subtraction" or opt=="2":
        print(f"\nResult of subtracting {a} and {b} = ",a-b)
        print("\n\t\t\t\t press Q to quit")
    elif opt == "mul" or opt=="multiplication" or opt=="3":
        print(f"\nResult of multiplying {a} and {b} = ",a*b)
        print("\n\t\t\t\t press Q to quit")
    elif opt == "div" or opt=="division" or opt=="4":
        print(f"\nResult of dividing {a} and {b} = ",a/b)
        print("\n\t\t\t\t press Q to quit")
    else :
        print("Invalid Option")
        quit()


