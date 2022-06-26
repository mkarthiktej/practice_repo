starting_number = int(input("please enter the starting number"))
ending_number = int(input("please enter the ending number"))
for number in range(starting_number, ending_number):
    if number > 1:
        for div in range(2, number):
            if number%div ==0:
                break
            elif number % 2 != 0:
                pass
                # break
        else:
            print(f"the number {number}is prime")




