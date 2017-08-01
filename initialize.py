import os
from lecturelists import *

# Initialize directories
directories = ['data/course', 'data/user', 'data/parsed']
for x in directories:
	if not os.path.exists(x):
		os.makedirs(x)

# Initialize lecture subscription lists
for x in lecturelist_all_rev.keys():
	if not os.path.exists('data/course/%s.txt' % x):
		with open('data/course/%s.txt' % x,'w') as f:
			f.write('.')
	if not os.path.exists('data/parsed/%s.txt' % x):
		with open('data/parsed/%s.txt' % x,'w') as f:
			f.write('.')
