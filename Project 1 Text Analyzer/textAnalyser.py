# author = Radim Kurka

section = '-' * 60

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

UserList = {"user1": "pass1", "user2": "pass2", "user3": "pass3"}

# Greet or welcome user
print(section)
print("Welcome to the application. Please provide your username and password.")
print(section)
# Ask user for name and pass and check whether registered
loggedIn = False
while not loggedIn:
    try:
        inpUsername = input("Username: ")
        inpPass = input("Password: ")
        makeSense = (inpPass in UserList[inpUsername])
        if makeSense:
            loggedIn = True
        else:
            loggedIn = False
            print("Username or password is wrong")
    except KeyError:
        print("Username or password does not exist")

# Select one text out of 3

numTexts = len(TEXTS)
print(section)
print(f"We have {numTexts} texts to be analyzed.")
haschosenText = False
while not haschosenText:
    userChoice = int(input(
        f"Enter a number between 1 and {numTexts} to select your text: "))
    if userChoice < 0 or userChoice > numTexts:
        print("Index out of range, choose a valid number please.")
        userChoice
    else:
        haschosenText = True

chosenText = TEXTS[userChoice - 1]
chosenTextSplit = chosenText.split()
print(section)
print("This is your chosen text:")
print("")
print(chosenText)
print(section)

# Calculate following - num words total
print(f"There are {len(chosenTextSplit)} words in the selected text.")

# numwordsCapital
countCap = 0
for char in chosenTextSplit:
    if char[0].isupper():
        countCap += 1
    else:
        continue
print(f"There are {countCap} titlecase words in the selected text.")

# numUPPERCASE
countUp = 0
for char in chosenTextSplit:
    if char.isupper():
        countUp += 1
    else:
        continue
print(f"There are {countUp} uppercase words in the selected text.")

#numlowercase
countLow = 0
for char in chosenTextSplit:
    if char.islower():
        countLow += 1
    else:
        continue
print(f"There are {countLow} lowercase words in the selected text.")

#numNumericStrings
count = 0
i = 0
while i < len(chosenTextSplit):
    try:
        char = int(chosenTextSplit[i])
        i += 1
        count += 1
    except ValueError:
        i += 1

print(f"There are {count} numeric words in the selected text.")
print(section)

# create star chart
graphList = []
for word in chosenTextSplit:
    graphList.append(len(word))

#define longest string in given text
longest_string = len(max(chosenTextSplit, key=len))

for star in range(1, longest_string + 1):
    print(f"{star}: {graphList.count(star) * '*'} {graphList.count(star)} occurences")

print(section)

# numNUMER1Conly
valueNumWords = 0
i = 0
while i < len(chosenTextSplit):
    try:
        char = int(chosenTextSplit[i])
        valueNumWords += char
        i += 1
    except ValueError:
        i += 1

print(f"The sum of numeric words in the selected text would be {valueNumWords}.")

print(section)

print(f"Thank you for using the program, {inpUsername}. Have a great day!")