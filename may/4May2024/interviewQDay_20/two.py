# #Q 1: Create variables for storing a person's name, age, and  
# # average test score.
# name = input("Enter name : ")
# age = int(input("Enter age : "))
# avgScore = int(input("Enter average test score : "))
#
# #
# # Q 2: Concatenate two strings and print the result.
# string1 =" priti"
# string2 = " fuse"
#
# concString = string1 + string2
# print(concString.upper())
# #
# # Q 3: Create a list of fruits and access elements using  
# #  indexing.
# fruitsList = ["mango","apple","chiku","jackfruit","banana"]
# for i in range(len(fruitsList)):
#     print("index = ",i)
#     print(fruitsList[i])
#
# #  Given a list of numbers, find the sum and average'
# myList = [1,22,33,-1,456]
# sum = 0
# avg = 0
# for i in myList:
#     sum = sum+i
#
# avg = sum // len(myList)
# print("Sum of numbers in list ",sum)
#
# print("average of numbers in list ",avg)
#
# #  Create ,a program that takes a temperature in Celsius and
# # converts it to Kelvin'
# #Celsius +273.15 = Kelvin
#
# temp_celsius = float(input("Enter temperature : "))
# Kelvin= temp_celsius + 273.15
#
# print(f"temperature in Celsius {temp_celsius} is equal to {Kelvin} temperature in kelvin")
#
# #  Implement a program that checks if a given string is a
# # palindrome'
#
# mystring = input("Enter a string : ")
# if mystring == mystring[::-1]:
#     print("Given string is palindrom")
# else:
#     print("Given string is not palindrome")
#
# #  Create a function to reverse a given string'
#
# mystring = "abcde"
# revString =mystring[:: -1]
# print("reverse string",revString)
#
# #another method
# revVstring = ""
# for i in mystring:
#     revVstring = i+revVstring
#
# print("reverse string ...",revVstring)
#
# # # Given a list of names, concatenate them into a single
# # string separated by spaces'
# sentn = ""
# myList1 = ["priti","bhavika","pratap","shria","neel"]
# for i  in myList1:
#     sentn = sentn +i + " "
# print(sentn)
# #  Write a Python program to check if a given string is a
# # pangram (contains all letters of the alphabet)'
#
import string

strr = "The quick brown fox jumps over the lazy dog"
alphabt = set(string.ascii_lowercase)
print(set(strr.lower())>= alphabt)
#
# #  Calculate the area and circumference of a circle given its
# # radius'
# radius = int(input("Enter radius of circle : "))
# area = radius * radius *22 //7
# circumference = radius *  2 * 22 // 7
#
# print("Area of given cirle is ",area)
# print("Circumference of given circle is ",circumference)
#
# # & Implement a program that converts a given number of
# # minutes into hours and minutes'
#
# myNumber = int(input("Enter a number to be converted into time as hour and minutes : "))
#
# hour = myNumber // 60
# min = myNumber % 60
#
# print(f"Given time from number {myNumber} minutes is equal to {hour} hour and {min} min")