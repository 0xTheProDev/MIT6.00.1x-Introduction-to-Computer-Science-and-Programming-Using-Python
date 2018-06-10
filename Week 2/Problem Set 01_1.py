# Counting vowel for a given string

s = str(raw_input("Enter the sentence: "))
vowel = 'aeiou'
count = 0
for char in vowel:
    count+=s.count(char)
print count
