# naming varibles
n_int = int(input("Input an integer (0 terminates): "))
odd_count = 0
even_count = 0
odd_sum = 0
even_sum = 0
positive_int_count = 0

while n_int != 0:
    if n_int > 0:
        positive_int_count = positive_int_count + 1
        if n_int % 2 == 1:
            odd_count = odd_count + 1
            odd_sum = odd_sum + n_int
        elif n_int % 2 == 0:
            even_count += 1
            even_sum = even_sum + n_int
    else:
        print("This integer is negative")
       
    n_int = int(input("Input an integer (0 terminates): "))


# Good stuff goes here

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)