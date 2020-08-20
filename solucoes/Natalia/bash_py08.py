import numpy as np

l= []
with open('Random.txt') as fh:
    sum = 0 # initialize here, outside the loop
    count = 0 # and a line counter
    for line in fh:
        count += 1 # increment the counter
        sum += int((line.split(' ')[-1])) # add here, not in a nested loop
    average = sum / count

    print (average)
