#!/usr/bin/env python
import sys
print sys.path

sys.path.append("/home/roger/WorkSpace/python/import/model/")
import a
a.t.a = 9

print a.t.a
# print a.test()


import a
print a.t.a
# print a.t