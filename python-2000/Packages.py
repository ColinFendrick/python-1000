from collections import OrderedDict
import sys

bog = OrderedDict(foo="bar", foo2="bar2")
# for ref in sys.path:
# 		print(ref)

for index, node in enumerate(sys.modules):
		print(index, node)