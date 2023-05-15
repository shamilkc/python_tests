
vowels = 'aeiou'
s = 'Hello, have you tried our tutorial section yet?'

count = {}.fromkeys(vowels,0)


for char in s:
   if char in count:
       count[char] += 1

print(count)