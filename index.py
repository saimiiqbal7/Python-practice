

"""sally = "sally sells sea shells by the sea shore"
characters = {}
best_char = None
freq = 0

for c in sally:
    if c in characters:
        characters[c] = characters[c] +1
    else:
        characters[c] = 1

for key in characters.keys():
    if characters[key] > freq:
        freq = characters[key]
        best_char = key
    
    

print(characters)
print(best_char)"""


"""
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

strArr = str1.split()

freq_words = {}

for word in strArr:
    if word in freq_words:
        freq_words[word] =freq_words[word]+1
    else:
        freq_words[word] = 1

print(freq_words)"""


"""str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for char in str1:

    if char in freq:
        freq[char] = freq[char]+1
    else:
        freq[char] = 1


print(freq)
"""


"""Junior = {
    "SI 206": 4,
    "SI 310": 4,
    "BL 300": 3,
    "TO 313": 3,
    "BCOM 350": 1,
    "MO 300": 3,
}
credits = 0
for value in Junior.values():
    credits += value

print(credits)"""
