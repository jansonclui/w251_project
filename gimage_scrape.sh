#!/usr/bin/python

import os, sys

file = open("labels.txt", "r")

#grabs the labels 
food = []
for each in file:
	stripped = each.strip('\n').replace(" ", "")
	food.append(stripped.lower())

#food = ['applepie', 'ceviche']
#the insta script automatically creates the directory

number_of_times = int(sys.argv[1])
for each in food:
	os.system('googleimagesdownload -k "%s" -l %d -nn' % (each, number_of_times) ) 



image_tags = []
for each in food:
	names = os.listdir("downloads/%s" % each)
	for name in names:
		image_tags.append((name, each))

print image_tags
