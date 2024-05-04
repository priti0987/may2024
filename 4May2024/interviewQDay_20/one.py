# 1( Write a Python program to calculate the area of a
# rectangle given its length and width
# def areaOfRectangle(leng,width):
#     return leng*width
#
# leng = int(input("Enter the lenght of rectangle : "))
# width = int(input("Enter the width of rectangle : "))
#
# print("Area of given rectangle is ",areaOfRectangle(leng,width))
# ***********************************************

# 2 Create a program that takes a user's name and age as
# input and prints a greeting message
# name=input("Enter your name : ")
# age = input("Enter your age : ")
# print(F"Hello {name}..!, You are {age} old")


# 3 Write a program to check if a number is even or odd
# try:
#     myNumber = int(input("Enter a number = "))
#
#     if myNumber % 2 == 0:
#         print(f"Given number {myNumber} is even")
#     else:
#         print(f"Given number {myNumber} is odd")
#
# except:
#     print("Please Enter Proper Number..!")

# 4Given a list of numbers, find the maximum and minimum
# values

# mylist = [1,55,23,45,89,5,600,-1,8522]
# max = mylist[0]
# min = mylist[0]
# for i in mylist:
#     if i > max:
#         max = i
#     elif i < min :
#         min = i
#
# print(f"maximum number in list i {max}")
# print(f"minimum number in list i {min}")


# 5Create a Python function to check if a given string is a
# palindrome

# mystring = input("Enter a string : ")
# revv = mystring[::-1]
# if revv == mystring:
#
#     print("Given string is palindrome ..!")
# else:
#     print("Given string is not palindrome..!")

# 6 Calculate the compound interest for a given principal
# amount, interest rate, and time period

# pAmount = int(input("Enter principle amount : "))
# interestRate = int(input("Enter interest rate : "))
# timePeriod = int(input("Enter time period : "))
#
# compoundAmount = pAmount * interestRate * timePeriod // 100
#
# print(f"Compound amount is {compoundAmount}")
# 7Write a program that converts a given number of days
# into years, weeks, and days
#
# days = int(input("Enter number of days : "))
# years = days//365
# weeks = days//53
# print("Years = ",years)
# print("weeks = ",weeks)

# 8 Given a list of integers, find the sum of all positive
# numbers
# sum = 0
# myList = [2,1,5,3,4,-5,-2,-4,-7]
# for i in myList:
#     if i >0:
#         sum = sum +i
#
# print(sum)
# 9Create a program that takes a sentence as input and
# counts the number of words in it

# mystring = "My name is priti and I am a QA"
# numberofwords = 0
# for i in mystring:
#     if i != " ":
#         numberofwords = numberofwords+1
#
# print(numberofwords)

# 10 Implement a program that swaps the values of two
# variables.
var1 = "priti"
var2 = "priya"
print("var1", var1)
print("var2", var2)

def swap(str1, str2):
    myvar = str2
    str2 = str1
    str1 = myvar
    return print(str1, str2)

swap(var2, var1)
