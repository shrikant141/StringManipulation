# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:21:24 2021

@author: User
"""
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

##### 1.	Create a string “Grow Gratitude”.

Str1 = "Grow Gratitude"
print(Str1)

##### Code for the following tasks:
##### a)	How do you access the letter “G” of “Growth”?

letter = Str1[0]

print(letter)

letter = Str1[5]

print(letter)

##### b)	How do you find the length of the string?

len(Str1)

##### c)	Count how many times “G” is in the string.

print(Str1.count('G'))


##### 2.	Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”

Str2 = "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."
print(Str2)

##### Code for the following
##### a)	Count the number of characters in the string.

print(Str2.count(''))





##### 3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
##### Code for the following tasks:

Str3 = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

print(Str3)

##### a)	get one char of the word

print (Str3[0:1]) 

##### b)	get the first three char

print (Str3[0:3]) 

##### c)	get the last three char

print (Str3[-3:])


##### 4.	create a string "stay positive and optimistic". Now write a code to split on whitespace.
##### Write a code to find if:

Str4 = "stay positive and optimistic"

x = Str4.split(' ')
x   
type(x)

#### a)	The string starts with “H”

Str4.startswith("H")

#### b)	The string ends with “d”

Str4.endswith("d")

#### c)	The string ends with “c”

Str4.endswith("c")


##### 5.	Write a code to print " 🪐 " one hundred and eight times. (only in python)

print(" 🪐 "* 108 )

##### 7.	Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”

Str5 = "Grow Gratitude"

Str5.replace("Grow", "Growth of")

##### 8.	A story was printed in a pdf, which isn’t making any sense.
##### the story is printed in a reversed order. 
##### Rectify the same and write a code to print the same story in a correct order.

Str6 = ".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”"

print (''.join(reversed(Str6)))
