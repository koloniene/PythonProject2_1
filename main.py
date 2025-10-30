import random

name = 'Zana'
surname = 'Koloniene'
age = 38
curr_year = 2025
print(name,surname,age,curr_year)


# Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus). Parašykite kodą, kuris pagal gimimo metus paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį :
# "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".
b_year = 1987
print(b_year)
current_year = 2025
print(curr_year)
curr_year = current_year - b_year
print(curr_year)
print('Aš esu ' + name + ' ' + surname +' . ' + 'Man yra' ,curr_year, 'metų')

# Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x)
# jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.

rnd_num = random.randint (0,4)
rnd_num1 = random.randint (0,4)
print(rnd_num, rnd_num1)

if rnd_num > rnd_num1:
    print(rnd_num / rnd_num1)
else:
    print(rnd_num / rnd_num1)

# Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x)
# jiems priskirkite atsitiktines reikšmes nuo 0 iki 25.
# Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

rnd_num = random.randint (20,30)
rnd_num2 = random.randint (20,30)
rnd_num3 = random.randint (20,30)
print(rnd_num, rnd_num2, rnd_num3)
import random
rnd_num = random.randint (0,25)
rnd_num2 = random.randint (0,25)
rnd_num3 = random.randint (0,25)
print(rnd_num, rnd_num2, rnd_num3)
a = 9
b = 7
c = 5

skaicius = [a,b,c]
skaicius.sort()
v_reiksme = skaicius[1]
print("vidurine reiksme", v_reiksme)

# Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji
# (naudokite ​random.randint(x,x)​ funkciją nuo 1 iki 10).
# Parašykite Python programą, kuri nustatytų,
# ar galima sudaryti trikampį ir atsakymą atspausdintų.
import random
a = random.randint (1, 12)
b = random.randint (1, 12)
c = random.randint (1, 12)


# Sukurti du kintamuosius. Jiems priskirti savo
# mylimo aktoriaus vardą ir pavardę kaip stringus
# (Jonas Jonaitis). Atspausdinti trumpesnį stringą.


vardas = "Dwayne"
pavarde = "Johnson"

if len(vardas) < len(pavarde):
    print(vardas)
elif len(pavarde) < len(vardas):
    print(pavarde)
else:
    print("Abu stringai yra vienodo ilgio.")

# Sukurti
# du kintamuosius.Jiems priskirti savo mylimo aktoriaus vardą ir pavardę
# kaip stringus.Vardą atspausdinti tik didžiosiom raidėm, o pavardętik
# mažosioms.(LEONARDO dicaprio)
vardas = "Dwayne"
pavarde = "Johnson"
print(vardas.upper())
print(pavarde.lower())

# Sukurti du kintamuosius.
# Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės
# kintamųjų reikšmių raidžių. Jį atspausdinti. (LD)
vardas = "Dwayne"
pavarde = "Johnson"
inicialai = vardas[0] + pavarde[0]
inicialai = (vardas[0] + pavarde[0]).upper()
print(inicialai)

# Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo
# ir pavardės kintamųjų raidžių.
# Jį atspausdinti.
vardas = "Dwayne"
pavarde = "Johnson"
paskutines_3_raides = vardas[-3:] + pavarde[-3:]
print(paskutines_3_raides)
paskutines_3_raides = vardas[-3:] + " " + pavarde[-3:]

# Sukurti kintamąjį su stringu: "An American in Paris".
# Jame vis`as “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.
tekstas = "An American in Paris"
rezultatas = tekstas.replace('a', '*').replace('A', '*')
print(rezultatas)

# Sukurti kintamąjį su stringu: "An American in Paris".
# Jame ištrinti visas balses. Rezultatą atspausdinti.
# Kodą pakartoti su stringais: "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".

def pasalinti_balses(tekstas):
    balses = "aeiouAEIOU"
    return ''.join(raide for raide in tekstas if raide not in balses)
tekstai = [
    "An American in Paris",
    "Breakfast at Tiffany's",
    "2001: A Space Odyssey",
    "It's a Wonderful Life"
]
for tekstas in tekstai:
    rezultatas = pasalinti_balses(tekstas)
    print(rezultatas)

for i in range(10):
    print("labas")


# Sukurk stringą su žodžiu.
# Atspausdink „Sutampa“, jei pirmoji ir paskutinė raidė vienoda
# (naudok word[0] ir word[-1]), kitaip „Nesutampa“.
word = "GIRL"
if word[0].lower() == word[-1].lower():
    print("Sutampa")
else:
    print("Nesutampa")

# Sukurk kintamąjį su bet kokiu žodžiu.
#  Atspausdink tą patį žodį, bet visos raidės išskyrus pirmą ir paskutinę turi būti pakeistos į _.
#  Pvz. Python → P____n.

word = "Home"
if len(word) <= 2:
    result = word
else:
 vidurys = "_" * (len(word) - 2)
 result = word[0] + vidurys + word[-1]
print(result)

# Stringe, kurį generuoja toks kodas:
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# Surasti ir atspausdinti epizodo numerį.

# Sukurk kintamąjį text = "Man 24 metai". Patikrink, ar stringe yra bent vienas skaitmuo
# (naudok in '0123456789' logiką be ciklų). Jei yra – išvesk „Yra skaičių“, jei ne – „Tik raidės“.

for i in range(10):
    print("labas")

for i in range(10):
    print(i)

# Sukurkite
# masyvą
# iš
# dešimties
# augalų
# pavadinimų.

medziai = [ "Ąžuolas",
    "Beržas",
    "Pušis",
    "Eglė",
    "Klevas",
    "Liepa",
    "Uosis",
    "Obelis",
    "Kriaušė",
    "Gluosnis"
]
for medis in medziai:
    print(medis)

for medis in medziai:
    print(medis)

medziai = [
    "Ąžuolas",
    "Beržas",
    "Pušis",
    "Eglė",
    "Klevas",
    "Liepa",
    "Uosis",
    "Obelis",
    "Kriaušė",
    "Gluosnis"
]


for medis in reversed(medziai):
    print(medis)

for i in range(10, 51, 2):
    print(i)

for i in range(10, 51, 2):
    if i % 10 == 0:
        continue
    print(i)

    for number in range(10, 51, 2):  # kas antras skaičius nuo 10
        if number % 10 == 0:  # jei dalinasi iš 10 be liekanos
            continue  # praleidžiame šį skaičių
        print(number)
    medziai = [
        "Ąžuolas",
        "Beržas",
        "Pušis",
        "Eglė",
        "Klevas",
        "Liepa",
        "Uosis",
        "Obelis",
        "Kriaušė",
        "Gluosnis"
    ]

    trumpesni_5 = 0  # žodžių trumpesnių nei 5 simboliai
    ilgesni_7 = 0  # žodžių ilgesnių nei 7 simboliai

    for medis in medziai:
        ilgis = len(medis)
    if ilgis < 5:
        trumpesni_5 += 1
    if ilgis > 7:
        ilgesni_7 += 1

    print("Žodžių trumpesnių nei 5 simboliai:", trumpesni_5)
    print("Žodžių ilgesnių nei 7 simboliai:", ilgesni_7)

    medziai = [
        "Ąžuolas",
        "Beržas",
        "Pušis",
        "Eglė",
        "Klevas",
        "Liepa",
        "Uosis",
        "Obelis",
        "Kriaušė",
        "Gluosnis"
    ]

    trees = [
        "Ąžuolas",
        "Beržas",
        "Pušis",
        "Eglė",
        "Klevas",
        "Liepa",
        "Uosis",
        "Obelis",
        "Kriaušė",
        "Gluosnis"
    ]


    count = sum(1 for tree in trees if 5 < len(tree) < 10)

    selected_trees = [tree for tree in trees if 5 < len(tree) < 10]

    print("Skaičius:", count)
    print("Medžiai, kurių ilgis tarp 5 ir 10 simbolių:", selected_trees)


import random
numbers = [random.randint(0, 300) for _ in range(300)]
count_over_150 = 0
for num in numbers:
    if num > 150:
        count_over_150 += 1
    if num > 275:
        print(f"[{num}]", end=" ")
    else:
        print(num, end=" ")

print("\nSkaičių didesnių nei 150:", count_over_150)



