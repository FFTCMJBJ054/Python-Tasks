def process_list(number):
    while True:
        listed_number = []
        num_count = int(input("How many numbers are in your list: "))
        for num in range (0,num_count):
            number = int(input("Enter your numbers: "))
            listed_number.append(number)
            listed_number.sort()
        check = bool(5 in listed_number)
        print (f"{listed_number}, {max(listed_number)}, {min(listed_number)}, {check}")


process_list(list)
