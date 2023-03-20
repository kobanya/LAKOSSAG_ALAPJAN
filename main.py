'''
Lakosság
NB- 2023.03.20
'''
from random import *

varos_neve = input("Adja meg a város nevét:  ")
lakosok = randrange(100,150000+1)

if lakosok < 5000:
    print(f"{varos_neve} LAKOSSÁGA : {lakosok}- kisváros")
elif 5000<lakosok< 20000:
    print(f"{varos_neve} LAKOSSÁGA : {lakosok} - járásközpont")
elif 20000 < lakosok < 50000:
    print(f"{varos_neve} LAKOSSÁGA : {lakosok} - nagyváros")
elif 50000< lakosok :
    print(f"{varos_neve} LAKOSSÁGA : {lakosok} - vármegyeszékhely")