# values
counter = 0
factor = 1
try:
    # input
    user_number = int(input("enter a number: "))
    if user_number == 0:
        print("0 is a factor of all numbers")
    # loop
    while counter != user_number:
        # process
        counter = counter + 1
        remainder = user_number % factor
        # factor finder
        if remainder == 0:
            print(" {} is a factor of {}".format(counter, user_number))
            factor = factor + 1
        # factor search
        else:
            factor = factor + 1
            continue
# error handling
except ValueError:
    print("invalid input")
finally:
    print("done..")
