def digit_summary(number):
    number = input ('Enter your desired integer')
    palindrome = (number == number[::-1])
    digits_sum = 0
    for num in number:
        digits_sum += int(num)
    print (f"{len(str(number))},{palindrome},{digits_sum}")


digit_summary (int)








