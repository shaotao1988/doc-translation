#!/usr/bin/env python

file_name = raw_input('Please input file name:')
file_object = open(file_name)
for line in file_object.readlines():
	print(line)
file_object.close()

