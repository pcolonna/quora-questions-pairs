# Create a random submission.
# Gives us a baseline.

import random

def create_random_submission():

    with open('submission.csv','w') as f:
        f.write('test_id,is_duplicate')
        f.write('\n')
        for i in range(2345796):
                f.write(str(i)+ ',' + str(float("{0:.1f}".format(random.random()))) + '\n')  # add a random probability

# create a random submission, 50/50 ones or zeros
def create_random_submission_1_0():

    line_nb = 0

    with open('submission.csv','w') as f:
        f.write('test_id,is_duplicate')
        f.write('\n')

        # wrong number of line in my test file somehow.
        """with open('test.csv','r') as t:
            for line in t:
                f.write(str(line_nb)+ ',' + str(random.getrandbits(1))+'\n')
                #f.write()
                line_nb += 1
        """
        # expected number of prediction.
        for i in range(2345796):                                            
                f.write(str(i)+ ',' + str(random.getrandbits(1))+'\n')

# create random submission.
# respect probability to find a duplicate, according to training set.
def create_random_submission_1_0_biased():

    proba   = sum_duplicate() / 2345796

    with open('submission.csv','w') as f:
        f.write('test_id,is_duplicate')
        f.write('\n')
        for i in range(2345796):
                prediction = int(random.random() < proba)
                f.write(str(i)+ ',' + str(prediction)+'\n')



# find number of duplicate in the file.
def sum_duplicate():
    result = 0
    
    with open('train.csv','r') as t:
            for line in t:
                if line[-3] == '1':
                    result += 1
    
    return result

if __name__ == "__main__":
    create_random_submission_biased()
    #sum_duplicate()
    
