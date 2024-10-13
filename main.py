'''
Przykład otrzymania wartości wprowadzonej przy użyciu funkcji input().
wyraz=input()

W celu poprawnego działania kodu w ramach GitHub Classroom warto dodatkowo użyć funkcję strip()
To pozwoli na usunięcie spacji oraz innych "spacjopodobnych" znaków (tabulacja \t', przejście do nowej linii '\n' lub '\r' etc.) z "głowy" i "ogona" (lewej i prawej części wyrazu).
wyraz=wyraz.strip()

Wydruk na ekranie (w konsoli)
print ('Ten wyraz został wprowadzony:', wyraz)
'''


from collections import defaultdict
import string
import re

n = int(input("Podaj liczbę dokumentów: ").strip())
dokumenty = [input("Dokument: ").strip().lower() for _ in range(n)]
m = int(input("Ile wyrazów do wyszukania?: ").strip())
wyrazy = [input("Wyrazy: ").strip().lower() for _ in range(m)]

#Znaki specjalne
tlumacz = str.maketrans('', '', string.punctuation)
dokumenty = [' '.join(re.split(r'\s+', dokument.translate(tlumacz))) for dokument in dokumenty]


licznik = [defaultdict(int) for _ in range(n)]

for i, dokument in enumerate(dokumenty):
    for slowo in dokument.split():
        licznik[i][slowo] += 1

for zapytanie in wyrazy:
    wynik = []

    for i in range(n):
        if zapytanie in licznik[i]:
            wynik.append((licznik[i][zapytanie], i))

    wynik.sort(key=lambda x: (-x[0], x[1]))
    wyjście = [indeks_dok for liczba, indeks_dok in wynik]

    print(wyjście)

