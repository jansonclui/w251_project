#!/usr/bin/python

import os, sys

file = open("labels.txt", "r")

#grabs the labels 
food = []
for each in file:
	stripped = each.strip('\n').replace(" ", "")
	food.append(stripped.lower())


#the insta script automatically creates the directory
number_of_times = 1
for each in food:
	os.system('instalooter hashtag %s %s -n %d' % (each, each, number_of_times) ) 

image_tags = []
for each in food:
	names = os.listdir(each)
	for name in names:
		image_tags.append((name, each))

print image_tags
