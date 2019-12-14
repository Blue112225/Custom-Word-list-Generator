word = str(input("Your word (if none, hit enter): "))
words = []

while word != "":
    words.append(word)
    if word.lower() != word:
        words.append(word.lower())
    if word.upper() != word:
        words.append(word.upper())
    word = str(input("Your word (if none, hit enter): "))
    
passwords = []
for w in words:
    passwords.append(w)
    for i in range(1000):
        passwords.append(w+str(i))

for i in range(0,len(words)):
    for j in range(0,len(words)):
        if i != j:
            passwords.append(words[i]+words[j])
            for k in range(10):
                passwords.append(words[i]+str(k)+words[j])

if input("Would you like to use special characters (y/n)? ").lower() == "y":
    spCh = list("`¬!\"£$%^&*()-_=+[]{};:'@#~\\|,<.>/? ")
    for i in range(0,len(words)):
        for j in range(0,len(words)):
            if i != j:
                for k in spCh:
                    for l in spCh:
                        passwords.append(words[i]+k+words[j]+l)

if input("Would you like to use 1337 (y/n)? ").lower() == "y":
    leetL = list("48cd3f9h1jklmn0pqrs7uvwxy2")
    leetU = list("48CD3F9H1JKLMN0PQRS7UVWXY2")
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for w in words:
        word = ""
        for c in list(w):
            if c.lower() == c and (c in alphabet):
                word = word + leetL[ord(c)-97]
            elif c.lower() in alphabet:
                word = word + leetU[ord(c)-65]
            else:
                word = word + c
        passwords.append(word)

wordList = ""
for i in passwords:
    wordList = wordList + str(i) + "\n"

file = input("Name of file to save to: ")
with open(file,"w+") as fil:
    fil.write(wordList)
