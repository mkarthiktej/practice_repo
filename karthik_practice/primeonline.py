lower_value = int(input("enter lower value:"))
upper_value = int(input("enter upper value:"))


print ("The Prime Numbers in the range are: ")
for number in range (lower_value, upper_value + 1):

    for i in range (2, number):
        if (number % i) == 0:
            break
    else:
        print(number)