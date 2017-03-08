#!/usr/bin/env python

file_name = input("Please input file name:")
file_object = open(file_name)
for line in file_object.readlines():
	print(line.decode('utf8'))
file_object.close()

