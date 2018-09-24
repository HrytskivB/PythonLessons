#!/usr/bin/env python3

height = int(input("Input height of door: "))
width = int(input("Input width of door: "))
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

if height > a and width > b:
    print("Success")
elif height > a and width > c:
    print("Success")
elif height > b and width > c:
    print("Success")
if height > b and width > a:
    print("Success")
elif height > c and width > a:
    print("Success")
elif height > c and width > b:
    print("Success")
else:
    print("Failure")
