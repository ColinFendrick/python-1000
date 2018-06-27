name = input("What's your name? ")
print("Hello ", name)
while True:
		try:
				age = input("How old are you? ")
				zage = int(age)
				print("%s is %d years old" % (name, zage))
				break
		except ValueError as exception:
				print("Age must be a number")
				raise Exception(exception)
		finally:
				print("We're done!")

