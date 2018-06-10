# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

s = str(raw_input("Enter the sentence: "))
word = "bob"
count = 0
l = len(word)
for i in range(len(s)-1):
        if s[i: i + l] == word:
            count+=1
print "Number of times bob occurs is: " + str(count)
