englishWord = input("Type any English Word: \n").lower()
englishWords = englishWord.split()
latinWords = []

vowels = ['a','e','i','o','u']

has_vowel = False
for i in range(len(englishWord)):        
    if englishWord[0] in vowels:
            latinWords.append(englishWord + "way")
            break
    else:     
         if englishWord[i] == "y":
            latinWords.append(englishWord[i:] + englishWord[:i] + "ay")
            has_vowel = True
            break
         if(has_vowel == False and i == len(englishWord)-1):
            latinWords.append(englishWord + "ay")
            break
pig_latin = ' '.join(latinWords)

print(pig_latin)