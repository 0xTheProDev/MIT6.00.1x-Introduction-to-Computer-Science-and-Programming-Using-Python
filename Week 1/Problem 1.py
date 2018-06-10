# Find Longest Alphabetical Substring in a given String

s = 'saddnivhfihmicfhndfcgfgv'
c = s[0]
x = ''
for i in range(1, len(s)):
    if(s[i] >= s[i - 1]):
        c += s[i]
    else:
        if(len(c) > len(x)):
            x = c
        c = s[i]
if(len(x) == 0):
    x = c
print(x)
