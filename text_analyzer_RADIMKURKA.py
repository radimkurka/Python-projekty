'''
author = Radim Kurka
'''
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
garpike and stingray are also present.''',
]

#userpass pairs
registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

delimiter = "=" * 50

#password check
def pass_check():
    logged_in = False
    while not logged_in:
        username = input("What is your username? ")
        password = input("What is your password? ")
        if registered.get(username) == password:
            logged_in = True
        else:
            print("Username or password is wrong!")
    print("Permission granted!")

def choose_text(texts=TEXTS):
    has_chosen = False
    while not has_chosen:
        choice = input(f"There are {len(texts)} in total, which one would you like to see? ")
        if not choice.isnumeric():
            print("Only numbers allowed!")
        elif int(choice) > len(texts) or int(choice) <= 0:
            print("Index out of range!")
        else:
            chosen_text = texts[int(choice) - 1]
            output_string = """ You have chosen text number {0}
             
            {1}
            """
            print(output_string.format(choice, chosen_text))
            has_chosen = True
            return chosen_text

def strip_to_words(chosen_text):
    formatted_text = []
    for word in chosen_text.split():
        formatted_text.append(word.strip(",.!?"))
    return formatted_text

def count_words(formatted_text):
    counts = {
        "total": len(formatted_text),
        "title": 0,
        "upper": 0,
        "lower": 0,
        "numeric": 0,
        "word_lengths": [],
        "sum_numeric": 0
    }

    for word in formatted_text:
        counts["word_lengths"].append(len(word))
        if word.istitle():
            counts["title"] += 1
        elif word.isupper():
            counts["upper"] += 1
        elif word.islower():
            counts["lower"] += 1
        elif word.isnumeric():
            counts["numeric"] += 1
            counts["sum_numeric"] += int(word)
    return counts

def star_chart(counts):
    ini_set = set(counts["word_lengths"])
    res = dict.fromkeys(ini_set, 0)
    for length in counts["word_lengths"]:
        res[length] += 1
    for key, value in res.items():
        string = f"{key} {'*' * value} {value} "
        print(string)

def main():
    print(delimiter)
    print("Welcome to the app, please log in: ")
    pass_check()
    print(delimiter)
    chosen_text = choose_text()
    formatted_text = strip_to_words(chosen_text)
    print(delimiter)
    counts = count_words(formatted_text)
    results = f"""
    There are {counts["total"]} words in the selected text.
    There are {counts["title"]} titlecase words.
    There are {counts["upper"]} uppercase words.
    There are {counts["lower"]} lowercase words.
    There are {counts["numeric"]} numeric strings.
    """
    print(results)
    print(delimiter)
    star_chart(counts)
    print(delimiter)
    print(f"If we summed all the words in the text, we would get {counts['sum_numeric']}.")

main()