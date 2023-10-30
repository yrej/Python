'''
Odsazování v Pythonu (indentation)

Většina programovacích jazyků jako C, C++, Java nebo JavaScript používá k vymezení bloků kódu složené závorky (braces).
V Pythonu se používá odsazování. Blok kódu (např. tělo funkce, cyklu atd.) tedy začíná s odsazením a končí prvním
neodsazeným řádkem.
Počet mezer v odsazení je libovolný, ale musí být konzistentní aspoň v rámci jednoho bloku.
K odsazení musí být použita minimálně jedna mezera.
Obvykle se k odsazování používá tubulátor, který bývá nejčastěji nastaven na 4 mezery.
'''

# Odsazení bloku kódu uvnitř cyklu a podmínky
for i in range(1, 10):
    print(i)
    if i % 2 == 0:
        print('even')
    else:
        print('odd')


'''
Dokumentační řetězce v Pythonu (docstrings)

Víceřádkový řetězec následující hned po záhlaví funkce v Pythonu je nazýván docstring (documentation string neboli 
dokumentační řetězec) a obsahuje stručné vysvětlení toho, co funkce provádí.
Přestože je to nepovinný doplněk programového kódu, je považován za "good programming practice", tedy jednu z dobrých
zásad, které by měl programátor v Pythonu dodržovat.
Docstrings se zapisují mezi trojnásobné uvozovky (tedy podobně jako komentáře).
Tyto dokumentační řetězce jsou přístupné prostřednictvím "magického" __doc__ atributu funkce.    
'''

# Odsazení bloku kódu uvnitř funkce a použití docstring
def greet(name):
    """
    This function greets to the person
    passed in as a parameter
    """
    print("Ahoj, " + name + "!")

# Vypíše docstring spojený s funkcí greet
print(greet.__doc__)
# Vyvolá funkci greet s parametrem 'Hilda'
greet('Hilda')

"""
Cvičení 2:

Vytvořte libovolně pojmenovanou vlastní funkci s minimálně jedním parametrem, v níž využijete cyklus for, 
aspoň jednu podmínku if a funkci print(). Dodržte správné odsazování kódu a opatřete funkci stručnou dokumentací.
Do konzole vypište nejprve docstring vaší funkce a potom zavolejte funkci samotnou.   
"""

# Netflix logo pomoci turtle

from turtle import *

bgcolor("black")
color("maroon")


def place(x, y):
    up()
    setx(x)
    sety(y)
    down()


place(-50, 150)

begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(150)
    right(90)

end_fill()

place(50, 0)

begin_fill()

for i in range(2):
    left(90)
    forward(150)
    left(90)
    forward(30)

end_fill()

color("red")

begin_fill()
goto(-20, 150)
left(180)
forward(30)
goto(20, 0)
right(180)
forward(30)
end_fill()


done()
