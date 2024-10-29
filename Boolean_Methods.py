def evaluate_conditions(a,b):
    a, b = map(int, input ('Enter two values separated by space: ').split())
    is_even = (a % 2 == 0 and b % 2 == 0)
    is_greater = (a > 10 or b > 10)
    polarity = (a > 0 and b > 0) or (a < 0 and b < 0)
    print (f"{is_even}, {is_greater}, {polarity}")


evaluate_conditions(int, int)
