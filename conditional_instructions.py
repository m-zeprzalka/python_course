# if, elif, else
age = input("Podaj swój wiek: ")
age = int(age)
if age >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")

dictionary = {"imię": "Michał", "nazwisko": "Zeprzałka", "wiek": 32}
if "imię" in dictionary:
    print(f"Imię to {dictionary['imię']}")
else:
    print("Brak imienia")

set = {1,2,3,4,5,6}
if 3 in set:
    print("3 jest w zestawie")