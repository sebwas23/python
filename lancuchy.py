# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import random

s = "Nowy napis do przećwiczenia"

print (s)
print ("drugi znak to: ", s[2],"\n")
print ('długosc łańcucha s = ', len(s),"\n")
print ("Znaki od 2 do 14 to: ",s[1:13],"\n")
print ("Wypisz co drugi znak: ", s[0:len(s):2], "\n")
print ("Napisz znaki od tyłu: ",s[::-1], "\n")
print ("Ostatni znak to: ",s[-1],"\n")

lista = [1,2,3,4,5,6,7,8,9]

print ("\n Pierwszy na liscie: ", lista[0])
los = random.choice(lista)

print ("\n Losowy element to: ", los)

a = 10
b = round (math.sqrt(a),2)
print ("\n Zaokraglanie w górę (3.2): ", math.ceil(3.2))
print ("\n Zaokrąglanie w dół (3.7): ", math.floor(3.7))
print (b)

print (5/2)
print ("Częsć całkowita z dzielenia 5/2: ", 5//2)
print ("Reszta z dzielenia 5/2: ", 5%2)

l1 = ['a','b','c','d','e','f','g','h','i','j','u','y']
l2 = ['k','l','ł','m','n','o','p','r','s','t','w','z']
l3 = []

if "a" in l1:
    print ("Znalazłem a :-) na pozycji: ",l1.index("a")) 
else: 
    print ("Nie ma tutaj a")

#kod = input("Wprowadź tekst do zakodowania: \n")
#kod = "Mój tajemniczy napis"

def zakoduj (kod):
    l1 = ['a','b','c','d','e','f','g','h','i','j','u','y']
    l2 = ['k','l','ł','m','n','o','p','r','s','t','w','z']
    l3 = []
    
    for i in range(0,len(kod)):
        if kod[i] in l1:
            poz = l1.index(kod[i])
            zmiana = l2[poz]
            l3.append(zmiana)
        elif kod[i] in l2:
            poz = l2.index(kod[i])
            zmiana = l1[poz]
            l3.append(zmiana)
        elif kod[i] == " ":
            l3.append(" ")
        else:
            l3.append(kod[i])

    zakodowane = ','.join(l3)
    wynik = zakodowane.replace(",","")
    return wynik


wprowadz = input("Wprowadź tekst do zakodowania: \n")
print ("Zakodowany tekst: ",zakoduj(wprowadz))



    


