str1 = 'aaab'
str2 = 'aaa'

count = 0

while count < len(str1) and count < len(str2) and str1[count] == str2[count] :
    count += 1

print (count)