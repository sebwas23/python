# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 21:44:16 2017

@author: s.wasiolka
"""

print("Znak a ma kod = ",ord('a'))
print("Znak z ma kod = ",ord('z'))
print("Znak 97 to = ",chr(97))
print(chr(ord('a') + 3))

d = "potrzeba pasji i zaangażowania, żeby naprawdę dogłębnie coś zrozumieć, przeżyć, a nie tylko szybko przełknąć. wiekszość ludzi nie poświęca na to czasu"
z = str(input("Podaj tekst do zakodowania: "))

#ROT - n
n = int(input("Podaj kod przesunięcia: "))

#Generuję znaki od 97 do 122
lista=''

for i in range(97,123):
    lista += chr(i)

print("Oryginalna lista = ",lista)


lista_n = ''
j=97
for i in range(97,123):
    if i+n<123:
        lista_n += chr(i+n)
    else:
        lista_n += chr(j)
        j+=1

print("Lista zakodowana = ", lista_n)

kod = z.maketrans(lista, lista_n)
zakodowane = z.translate(kod)

print ("Zakodowane = ", zakodowane)

dekod = zakodowane.maketrans(lista_n, lista)
odkodowane = zakodowane.translate(dekod)
print ("Odkodowane = ", odkodowane)