# Create a random submission.
# Gives us a baseline.

import random

# create random, 50/50, submission
def create_random_submission():

	line_nb = 0

	with open('submission.csv','w') as f:
		f.write('test_id,is_duplicate')
		f.write('\n')
		#wrong number of line in my test file somehow.
		"""with open('test.csv','r') as t:
			for line in t:
				f.write(str(line_nb)+ ',' + str(random.getrandbits(1))+'\n')
				#f.write()
				line_nb += 1
		"""
		#wanted number of prediction.
		for i in range(2345796):											
				f.write(str(i)+ ',' + str(random.getrandbits(1))+'\n')

# find number of duplicate in the file.
def sum_duplicate():
	result = 0
	with open('train.csv','r') as t:
			for line in t:
				#print(line[-3])
				if line[-3] == '1':
					result += 1
	
	return result

# create random submission.
# respect probability to find a duplicate, according to training set.
def create_random_submission_biased():

	line_nb = 0
	proba   = sum_duplicate() / 2345796

	with open('submission.csv','w') as f:
		f.write('test_id,is_duplicate')
		f.write('\n')
		for i in range(2345796):
				prediction = int(random.random() < proba)
				f.write(str(i)+ ',' + str(prediction)+'\n')

if __name__ == "__main__":
	create_random_submission_biased()
	
