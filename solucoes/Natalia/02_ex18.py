from collections import Counter

file = open("she.txt", "r") # open file
charcount = {} #dictionary to hold char counts
validchars = "abcdefghijklmnopqrstuvwxyz" # only these counted
print(": Letter : Frequency :")

for i in range(97,123): # lowercase range
    c = (chr(i)) # the chars a-z
    charcount[c] = 0 # initialize count

for line in file:
    words = line.split(" ") # line into words
    for word in words:  # words into chars
      chars = list(word) #convert word into a char list
      for c in chars:  # process chars
          if c.isalpha():  # only alpha allowd
              if c.isupper():
                  c = c.lower()  # if char is upper convert to lower
              if c in validchars: # if in valid char set
                  charcount[c] += 1 # increment count
print(charcount) # print list
file.close() # close file
