def istrcmp(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    return string1 == string2

print (istrcmp('python', 'Python'))
print (istrcmp('LaTeX', 'Latex'))
print (istrcmp('a','b'))