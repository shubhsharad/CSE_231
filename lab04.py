# def rotate(s,n):
#     length=len(s)
#     n = n%length
#     if length>1:
#         return s[length-n:] + s[:length-n]
#     else:
#         return "String hasnt been changed or is of only length 1"

# x = input("enter String:")
# y = int(input("enter integer"))
# print(rotate(x,y))




# x = input("enter number: ")
# def digit_count(s):
#     sval=str(float(s))
#     print (sval)
#     zero_count=0
#     even_count=0
#     odd_count=0
#     for d in sval:
#         if d == ".":
#             continue
#         if int(d)% 10 == 0:
#             zero_count += 1
#         elif int(d) % 2 == 0:
#             even_count += 1
#         elif int(d) % 2 != 0:
#             odd_count += 1
#     return (even_count, odd_count, zero_count)

# print(digit_count(x))

# def float_check(x):
#     return x.replace('.','',1).isdigit()

# x = input('enter number: ')
# print(float_check(x))
         