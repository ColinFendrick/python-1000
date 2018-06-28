import sys

try:
		file = open('myfile.txt')
		line = file.readline()
		ival = int(line.strip())

except IOError as ex:
		print("IOError({0}): {1}".format(ex.errno, ex.strerror))
except ValueError:
		print("Unable to convert line to integer")
except:
		print("Unexpected exception:", sys.exc_info()[0])