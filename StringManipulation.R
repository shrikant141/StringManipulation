
library(stringr)
library(stringi)
?stringr

##### 1.	Create a string "Grow Gratitude".

str1 <- "Grow Gratitude"
str1

##### Code for the following tasks:
#####  a)	How do you access the letter "G" of "Growth"

substr(str1, 1, 1)
substr(str1, 6, 6)

#####  b)	How do you find the length of the string?

str_length(str1)

#####  c)	Count how many times "G" is in the string.

str_count(str1, "[G]")

##### 2.	Create a string "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."

str2 <- "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."

#####  Code for the following
##### a)	Count the number of characters in the string.

print(nchar(str2))

##### 3.	Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
##### Code for the following tasks:

str3 <- "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"

print(str3)
#### a)	get one char of the word

substr(str3, 1, 1)                           

#### b)	get the first three char

substr(str3, 1, 3)                      

#### c)	get the last three char

str_sub(str3, - 3, - 1) 

##### 4.	create a string "stay positive and optimistic". Now write a code to split on whitespace.
####  Write a code to find if:

str4 <- "stay positive and optimistic"

print(str4)

strsplit(str4, " ")

##### a)	The string starts with "H"

startsWith("str4", "H")

##### b)	The string ends with "d"

endsWith("str4","d")

##### c)	The string ends with "c"

endsWith('str4', 'c')

##### 6.	Write a code to print " o " one hundred and eight times. (only in R)

print(strrep(" o ", 108))

##### 7.	Create a string "Grow Gratitude" and write a code to replace "Grow" with "Growth of"

str6 <- "Grow Gratitude"

print(str6)

str_replace(str6, "Grow", "Growth of") 

str6

##### 8.	A story was printed in a pdf, which isn't making any sense.
##### the story is printed in a reversed order. 
##### Rectify the same and write a code to print the same story in a correct order.

str7 <- ".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs'esuomeht ta dehgualnoilehT ".emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I" .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s'noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A""

stri_reverse(str7)

str7
