#6/6/2019
#Sakar Michel
#Problem: The Challenge
#Given a string S and a set of words D, find the longest word in D that is a subsequence of S.
#Link to the problem: https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/#!

stringOrder = 'abpplee'
firstWord = ['able' ,'ale','apple', 'bale', 'kangaroo']
theLongestWordInCorrectOrder = ''
goodWord = True;
for eachWord in firstWord:
    
    for i in range(len(eachWord)):
    
        
        CharacterInFirstWord = eachWord[i]
        if (CharacterInFirstWord in stringOrder[i:]):
            #characters are in the right order
            continue
        else:
            print('The charcters in first word are not in the correct order')
            print('The character at index', str(i), 'in eachWord is', CharacterInFirstWord)
            print('The characters at index', str(i), 'in stringOrder is', stringOrder[i])
            goodWord = False;
            break
    
    if(goodWord):  
        
        if (len(theLongestWordInCorrectOrder) < len(eachWord)):
            theLongestWordInCorrectOrder = eachWord
    else:
        goodWord = True;
print(theLongestWordInCorrectOrder)
