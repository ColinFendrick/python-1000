#!/usr/bin/env python3
name = input("What is your name? ")
print("Hello '", name, "'")
try:
		age = input("What is your age? ")
		zage = int(age)
		print("%s is %d years old!" % (name, zage))
except ValueError:
		print("Sorry, that age is not numeric!")


#! Running this while true

name = input("What is your name? ")
print("Hello '", name, "'")
while True:
		try:
				age = input("What is your age? ")
				zage = int(age)
				print("%s is %d years old!" % (name, zage))
				break
		except ValueError:
				print("Sorry, that age is not numeric!")
				raise #! this raises ValueError as Exception
		else:
				print("What else happens")
				break
		finally:
				print("data entry completed")


#! Custom Exceptions
class MyError(Exception):
		def __init__(self, value):
				self.value = value
		def __str__(self):
				return self.value