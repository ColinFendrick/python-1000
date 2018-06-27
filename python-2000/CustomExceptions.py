# try:
# 		pass
# except Exception as ex:
# 		print("error:", ex)
# else:
# 		print("All is well")


class MyError(Exception):
		def __init__(self, value):
				self.value = value

		def __str__(self):
				return self.value

try:
		# raise MyError("tossing it in")
		ss = 12 / 0
		# pass
except Exception as ex:
		# print("Error: ", ex)
		raise
else:
		print("all is well")
