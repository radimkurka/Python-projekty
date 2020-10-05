# Greet the client
split = "=" * 20
split2 = "-" * 20
DESTINATIONS = ['Praha', 'Vídeň', 'Brno', 'Svitavy', 'Zlin', 'Ostrava']
PRICES = [1000, 1100, 2000, 1500, 2300, 3400]
print(split)
print("We can offer you the following destinations:")
print(split2)
print("""
1 - Prague  | 1000

2 - Wien    | 1100

3 - Brno    | 2000

4 - Svitavy | 1500

5 - Zlin    | 2300

6 - Ostrava | 3400
""")
print(split2)
vyber = int(input("Please enter the destination number to select: "))
vyberIndex = vyber - 1
kamJede = DESTINATIONS[vyberIndex]
kolikToBudeStat = PRICES[vyberIndex]
print(split)
print("REGISTRATION")
print(split2)
print("In order to complete your reservations, please share few details about yourself with us.")
print(split2)
name = input("NAME: ")
print(split)
surname = input("SURNAME: ")
print(split)
year = (input("Year of Birth: "))
print(split)
mail = input("EMAIL: ")
print(split)
pwd = input("PASSWORD: ")
print(split)
print("Thank you", name)
print(f"We have made your reservation to {kamJede}. It will cost you {kolikToBudeStat} money units. Have a nice day.")
