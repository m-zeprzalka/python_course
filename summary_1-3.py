# --- Wprowadzenie do zmiennych i typów danych ---

# Definiowanie zmiennych z różnymi typami danych
liczba_calkowita = 10  # int (liczba całkowita)
liczba_zmiennoprzecinkowa = 10.5  # float (liczba zmiennoprzecinkowa)
tekst = "Witaj w Pythonie!"  # str (łańcuch znaków, czyli tekst)
wartosc_logiczna = True  # bool (wartość logiczna: True lub False)

# Wyświetlanie wartości zmiennych
print("Liczba całkowita:", liczba_calkowita)
print("Liczba zmiennoprzecinkowa:", liczba_zmiennoprzecinkowa)
print("Tekst:", tekst)
print("Wartość logiczna:", wartosc_logiczna)

# --- Konwersje typów danych ---

# Konwersja liczby całkowitej na tekst
liczba_jako_tekst = str(liczba_calkowita)
print("Liczba jako tekst:", liczba_jako_tekst)

# Konwersja tekstu na liczbę całkowitą
tekst_jako_liczba = int("123")
print("Tekst jako liczba całkowita:", tekst_jako_liczba)

# Konwersja tekstu na liczbę zmiennoprzecinkową
tekst_jako_float = float("123.45")
print("Tekst jako liczba zmiennoprzecinkowa:", tekst_jako_float)

# --- Operacje na tekstach ---

# Łączenie tekstów (konkatenacja)
imie = "Jan"
nazwisko = "Kowalski"
pelne_imie = imie + " " + nazwisko
print("Pełne imię:", pelne_imie)

# Zliczanie znaków w tekście
dlugosc_tekstu = len(pelne_imie)
print("Długość pełnego imienia:", dlugosc_tekstu)

# Dostęp do konkretnych znaków w tekście
pierwsza_litera = pelne_imie[0]
ostatnia_litera = pelne_imie[-1]
print("Pierwsza litera imienia:", pierwsza_litera)
print("Ostatnia litera imienia:", ostatnia_litera)

# --- Praca z listami ---

# Tworzenie listy z kilkoma elementami
lista_owocow = ["jabłko", "banan", "pomarańcza"]

# Dodawanie nowego elementu do listy
lista_owocow.append("kiwi")
print("Lista owoców po dodaniu kiwi:", lista_owocow)

# Usuwanie elementu z listy
lista_owocow.remove("banan")
print("Lista owoców po usunięciu banana:", lista_owocow)

# Dostęp do elementów listy
pierwszy_owoc = lista_owocow[0]
ostatni_owoc = lista_owocow[-1]
print("Pierwszy owoc:", pierwszy_owoc)
print("Ostatni owoc:", ostatni_owoc)

# --- Praca z krotkami ---

# Tworzenie krotki z kilkoma elementami
krotka_zwierzeta = ("kot", "pies", "zając")

# Dostęp do elementów krotki
pierwsze_zwierze = krotka_zwierzeta[0]
ostatnie_zwierze = krotka_zwierzeta[-1]
print("Pierwsze zwierzę:", pierwsze_zwierze)
print("Ostatnie zwierzę:", ostatnie_zwierze)

# Krotki są niemutowalne, więc nie możemy dodawać/usunąć elementów jak w przypadku list
