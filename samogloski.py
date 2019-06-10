#Program podaje liczbę samogłosek w zdaniu

#zmienną s wprowadzam z klawiatury:
s = input("Wprowadź dowolny tekst: ")

#Lista samogłosek
samogloski = ['a','ą','e','ę','i','o','ó','u','y']

sam = []

for i in range(len(s)):
    for j in range(len(samogloski)):
        if s[i] == samogloski[j]:
            sam.append(samogloski[j])

print ("Liczba samogłosek w zdaniu: ","'",s,"'"," = ", len(sam))