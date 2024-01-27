## flag_shop

difficulty: 

---

sol:

first approach:

the hint says "Two's compliment can do some weird things when numbers get really big!"
this tells me this task may have something to do with big numbers becoming negative, or vice versa

the program gives us a balance of 1100 to begin, and we have the option to buy two flags

the "definetly not the flag flag" costs 900 each, and gives us the option to buy a desired quantity 
the 1337 flag costs 100000, there is only one in stock

my idea is to buy so many of the first flag that the cost becomes so high that it turns into a negative number and increases the balance

inputting a negative number does not work, because it does not accept the "-"

i started the number at 10000 and increased the number of zeros until it said that the total came to a negative number and my balance increased.

i could then buy the 1337 flag
