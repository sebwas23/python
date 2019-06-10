import re
#Program liczy liczbę wyrazów w zdaniu
line = "Dzisiaj gramy mecz. z Izraelem"
policz = len(re.findall(r'\w+', line))
# zapis: "r'\w+'" - oznacza: Wypisz wszystko co znajduje się pomiędzy niealfanumerycznymi
# znakami tj.: ".,_ "
# zapis: "r'^\w+'" - oznacza: weź tylko pierwszy wyraz
print (policz)

spacja = len(re.findall('\s', line)) #liczba spacji w tekście
print (spacja)

spacja1 = len(re.findall('\S', line)) #liczba znaków w tekście (bez spacji)
print (spacja1)

xx = "Nasza edukacja to zabawa"
r1 = re.findall(r"^\w+",xx)
print(r1)