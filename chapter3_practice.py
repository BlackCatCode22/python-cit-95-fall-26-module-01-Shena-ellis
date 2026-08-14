# # Booleans == FALSE/TRUE
# 5 == 5
# print(5 == 5)
# type(True) ## does nothing

# == (equal to)
# != (not equal to)
# != (not eaqual to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# is (is the same as)
# is not (is not the same as)

#not (7 > 6)
#6 % 2 == 0





# # < ---- 1 basic if ---- >
# print(6 % 5 == 0)
#
# # DONT FORGET TO SAY "PRINT()" !!!
#
# if 4 > 5 :
#     print('4 is greater')
# else: print('4 is not greater')
#
# x = 7
#
# print("before the if statement")
#
# if x > 5:
#     print('x is greater than 5')
#     print('This line is also inside the if statement')
#
# print('after the if statement') # this is after because it is not indented





# # < ---- 2 if and else ---- >

# number = 7
#
# if number % 2 == 0:
#     print('The number is even')
# else:
#     print('The number is odd')
#
# # % 2 finds the REMAINDER after 2





# # < ---- 3 get a number from the user ---- >
# number = int(input('Enter a whole number:'))
#
# if number > 0:
#     print('The number is positive.')
# else:
#     print('The number is negative.')
# input() returns text. int() converts that text into a whole number so you can compare it numerically.





# < ---- 4 if, elif, and else ---- >
# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
#
# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x is equal to y')
#



# # < ---- 5 and, or, and not ---- >
#
# x = 7
#
# if x > 0 and x < 10:
#     print("x is a positive single-digit number")
#
# if 0 < x < 10:
#     print("x is a positive single-digit number")
#
#
# number = 9
#
# if number % 2 == 0 or number % 3 == 0:
#     print("The number is divisible by 2 or 3")

# x = 4
# y = 5
# print(x > y)
# print(not(x > y)) # you can use (not)





# < ---- 6 catch invalid input ---- >
# inp = input('Enter Farenheit Temperature: ')
# fahr = float(inp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)
#
#
# # < ---- 7 try and except --- >
# inp = input('Enter Farenheit Temperature: ')
#
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except ValueError:
#     print('Please enter a number')


#
# # < --- 8 Short-circuit evaluation ---- >
# x = 6
# y = 2
#
# print(x >= 2 and (x / y) > 2)
#
# x = 1
# y = 0
#
# print(x >= 2 and (y / 2) > 2)
#
#
# # x = 6
# # y = 0
# # print(x >= 2 and (y / y) > 2) # !ZeroDivisionError
#
# x = 6
# y = 0
#
# print(x >= 2 and y != 0 and (x / y) > 2)


# < --- Debugging --- >
# When reading the trace back begin near the bottom
# 1) Find the error type, such as ValueError or IndentationError.
# 2) The referenced filename and line number.
# 3) The code on that line.
# 4) The line immediately before it, because the actual mistake may have started earlier.

# Process finished with exit code zero means the program completed successfully.
# Process finished with exit code 1 usually means the program stopped because of an error. 