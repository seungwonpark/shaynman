import os
from lecturelists import *

# Initialize directories
directories = ['data/course', 'data/user']
for x in directories:
	if not os.path.exists(x):
		os.makedirs(x)

# Initialize lecture subscription lists
for x in lecturelist_all_rev.keys():
	with open('data/course/%s.txt' % x,'w') as f:
		f.write('.')
