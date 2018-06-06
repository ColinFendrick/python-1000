#!/usr/bin/env python3
name = input("What is your name? ")
print("Hello '", name, "'")
try:
		age = input("What is your age? ")
		zage = int(age)
		print("%s is %d years old!" % (name, zage))
except ValueError:
		print("Sorry, that age is not numeric!")
