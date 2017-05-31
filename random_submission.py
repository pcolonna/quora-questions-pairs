# Create a random submission.
# Gives us a baseline.

import random

def create_random_submission():

	line_nb = 0

	with open('submission.csv','w') as f:
		f.write('test_id,is_duplicate')
		f.write('\n')

		"""with open('test.csv','r') as t:
			for line in t:
				f.write(str(line_nb)+ ',' + str(random.getrandbits(1))+'\n')
				#f.write()
				line_nb += 1
		"""
		for i in range(2345796):
				f.write(str(i)+ ',' + str(random.getrandbits(1))+'\n')

def sum_duplicate():
	result = 0
	with open('train.csv','r') as t:
			for line in t:
				if line[0] == '1':
					result += 1
	print(result)

if __name__ == "__main__":
	#create_random_submission()
	sum_duplicate()
