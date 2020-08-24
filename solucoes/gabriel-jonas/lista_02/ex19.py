
def getAnagrams(words):

    anagrams = []


    while len(words) > 0:
        word = words.pop(0)
        #print ("Input")
        #print (word)
        anagrama = [word]
        count = 0
        #print ("While")

        while count < len(words):
            next_word = words[count]
            #print (next_word)
            if sorted(list(word)) == sorted(list(next_word)):
                #print (next_word)
                words.remove(next_word)
                anagrama.append(next_word)
            else:
                count += 1

            
        #print (anagrama)
        anagrams.append(anagrama)
        #print (words)
        
    return (anagrams)

words = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
print (getAnagrams(words))