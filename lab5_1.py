#!/usr/bin/env python3

number = int(input("Input number of power 2: "))

print(number != 0 and ((number & (number - 1)) == 0))
