def get_a_num():
    while(True):
        num = input("enter a number: ")
        try:
            num = int(num)
        except ValueError:
            print("please enter a integer")
            continue
        else:
            break
    return num 

    
num1 = get_a_num()
num2 = get_a_num()

total = num1 + num2
print(str(num1) + " + " + str(num2) + " is " + str(total))

