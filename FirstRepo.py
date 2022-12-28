# CURS 1

#-------Hello World si comentarii ---------
print("Hello World")

print("Acesta este un curs de python")
print('Acesta este un curs de python')

#comentarii
"""
acesta este
un comentariu
pe mai multe linii
"""

# acesta este
# un comentariu
# pe mai multe linii

#TIPS: Pentru a comenta sau a scoate comentariile de pe o portiune mai mare de cod, selectati bucata de cod ce o vreti comentata si
#apasati CTRL + / (pentru Windows) SAU CMD + / (pentru Mac OS)


#---------variabile si tipuri de date -----------

a = 5  # aceasta este o variabila de tip int
b = 24 # aceasta este o variabila de tip int
c = "mama"  # aceasta este o variabila de tip string
d = 1.25  # aceasta este o variabila de tip float
imiPlacePython = True # aceasta este o variabila de tip bool
vreau_sa_muncesc_mult = False #aceasta este o variabila de tip bool

#ii atribuim lui a valoarea lui b
a = b

print(f"Valoarea lui a este {a}")

b = d # ii atribui lui b valoarea lui d
a = b = c # ii atribuim lui a valoarea lui b si apoi lui c. Valoarea finala a variabilei a va fi valoarea lui c.

print("Valoarea finala a lui a este: ")
print(a)
print(c) #valoarea lui c ramane aceeasi


# ------- Functia type() ------------
mama = "Maria" # string
tata = "Ionel" # string
varsta = 49 # int
salariu = 15500 #int
eficienta = 8.5 #float
suntAcasa = True #bool


print(type(mama)) # afisam tipul variabilei mama
print(type(tata)) # afisam tipul variabilei tata
print("Tipul variabilei varsta este: ")
print(type(varsta)) # afisam tipul variabilei varsta
print("Tipul variabilei salariu este: ")
print(type(salariu)) # # afisam tipul variabilei salariu
print("Tipul variabilei suntAcasa este: ")
print(type(suntAcasa)) # # afisam tipul variabilei suntAcasa
print("Tipul variabilei eficienta este: ")
print(type(eficienta)) # afisam tipul variabilei eficienta

# ------Functia type() si casting

varsta = 29 # variabila tip int
print("Tipul variabilei varsta este: ")
print(type(varsta)) # afisam tipul variabilei varsta
print("Acum variabila varsta este de tip: ")
print(type(str(varsta))) # afisam tipul variabilei varsta care este convertit in string
print(type(float(varsta))) # # afisam tipul variabilei varsta care este convertit in float

# -----------Concatenarea ---------------
##### OBS! Nu se pot concatena stringuri cu alte tipuri de variabile (exemplu: string + int )

# exemplul 1
fructe = "mere, pere si portocale " # var tip string
shopping = "Eu am cumparat astazi " # var tip string
pret = 25 # var tip int

str_concat = shopping + fructe # str_concat este o variabila care va contine variabila shopping concatenata cu var fructe
print(str_concat) # printam valoarea variabilei str_concat

pret = str(pret) # convertim variabila pret care era de tip int, in tip string
str2_concat = fructe + pret # concatenam var fructe cu var pret care este acum de tip string, deci string cu string
print(str2_concat) # afisam valoarea variabilei str2_concat

#exemplu 2
# avem urmatoarele variabile:
actiune = "Am cumparat " #string
obiect = "un dulap la " #string
pret = 100 # int

#Vrem sa concatenam toate stringurile intr-o singura variabila so sa obtinem:
# Am cumparat un dulap la 100 lei

#in urmatorul cod vom primi eroare
fraza = actiune + obiect + pret # incercam sa concatenam 2 stringuri cu int
print(fraza) # afisam valoarea variabilei fraza
# la rularea acestui cod vom primi urmatoarea eroare:
#TypeError: can only concatenate str (not "int") to str

# ca sa nu primim eroare, mai intai trebuie sa convertim variabila pret in string, astfel incat sa avem doar stringuri
fraza = actiune + obiect + str(pret) # concatenam cele 2 stringuri cu variabila pret care este convertita in string
print(fraza)

# exemplul 3

#concatenam mai multe stringuri in print, printre care si " " care inseamna spatiu
print("Astazi am mancat" + " " + "multe mere" + " " + "si nu ma simt bine")
#acest print va afisa "Astazi am mancat multe mere si nu ma simt bine"


# --------- Functia print()  -  formatare ------------------

# in print folosim litera f sau F inainte de a deschide ghilimele, iar unde vrem sa se afiseze valoarea variabilei
# vom pune {variabila}. printul va avea aceasta forma: print(f"ceva ceva {variabila} ceva")

#avem urmatoarele variabile
fructe = "struguri, banane, capsuni" # string
shopping2 = "Eu am luat din supermarket" # string
pret = 35 #int

#Vrem sa afisam Eu am luat din supermarket struguri banane capsuni la pretul de 35 de lei
print(f"{shopping2}:{fructe} la pretul de {pret} de lei")


## exercitiul 2
data = "25/10/2022" # string
ora = "19:53" # string

# Eu astazi la data de 25/10/2022 am inceput primul curs de python, iar la ora 19:53 am pus prima intrebare
print(f"Eu astazi la data de {data} am inceput primul curs de python, iar la ora {ora} am pus prima intrebare")

## exercitiul 3

#Astazi fratele meu Mihai a inscris 2 goluri
frate = "Mihai"
nr_goluri = 2

print(f"Astazi fratele meu {frate} a inscris {nr_goluri} goluri")

# ------------ assertion ------------------
# syntaxa: assert expression, assertion message

# avem urmatoarea variabila de tip int
varsta = 29

# comparam valoarea variabilei varsta cu 30, daca valoarea nu este 30, atunci se afiseaza mesajul de eroare, iar codul nu curge mai
# departe
assert varsta == 30, f"Ma astept sa am 30 de ani, dar se pare ca varsta mea este de, {varsta}"
a = 2
b = 5
print(a+b)

# inlocuieste acum varsta = 29, cu varsta = 30. codul va curge mai departe si se va executa printul cu a + b


####ex 2

nr_placinte = 3
# Trebuia sa mananc 3 placinte, dar se pare ca am mancat x placinte
assert nr_placinte == 3, f"Trebuia sa mananca 3 placinte, dar se pare ca am mancat {nr_placinte}"
print("Am trecut testul")

#### ex 3
mama = "Maria"

assert mama == "Maria", f"Pe mama mea o cheama Maria, dar se pare ca s-a incurcat si acum e {mama}"
print("Am gasit-o pe mama!")

# ------------Functia input() ----------------

# functia input cere utilizatorului sa introduca ceva de la tastatura
# ## OBS!! orice valoare ar introduce utilizatorul de la tastatura, aceasta va fi mereu de tip string

## ex 1:
# utilizatorul va introduce de la tastatura un numar intreg care se va salva in variabila utilizator_input
utilizator_input = input("Introduceti de la tastatura un numar intreg")
print(utilizator_input) # afisam valoarea care s-a stocat in utilizator_input

## ex 2:
# utilizatorul va introduce de la tastura un numar intreg pe care il vom aduna cu valoarea variabilei b
# din moment ce orice va introduce utilizatorul este de tip string, valoarea trebuie convertita in int pt a o putea aduna
# la val lui b
# Avem 2 variante:

# varianta 1
b = 73 # int
# stocam in variabila a inputul de la utilizator
# convertim inputul de la utilizator in int inainte de a-l asigna variabilei a
a = int(input("Te rog sa introduci un numar intreg: "))
print(type(a)) # tipul va fi int
c = b+a
print(f"valoarea variabilei {c} este: ")

# varianta 2
b = 73 # int
# stocam in variabila a inputul de la utilizator fix asa cum vine el
a = input("Te rog sa introduci un numar intreg: ")
print(type(a)) # tipul va fi string
#cand cream variabila c si ii asignam cele 2 valori adunate ale lui a si b, convertim var a in int
c = b+int(a)
print(f"valoarea variabilei {c} este: ")


#### ----- functii string ------------

###  functia len() - afiseaza numarul de caractere dintr-un string
# syntaxa: len(variabila)
c = "Vreau acasa" # string
lungime = len(c) # am creat variabila lungime in care stocam outputul functiei len(c), adica numarul de caractere din stringul
                # "vreau acasa"
print(f"Lungimea stringului c este: {lungime}")
# daca nu vrem sa folosim variabila lungime putem printa astfel:
print(len(c))


### index
# indexul reprezinta pozitia pe care se afla un caracter
# numerotarea incepe de la 0
# exemplu
# p e r e
# 0 1 2 3
myString = "ciuperca" # variabila myString de tip string
poz = myString[4] # avem variabila poz careia ii asignam litera care se afla de pe pozitia 4
print(f"Pe pozitia 4 este litera {poz}")
# c i u p e r c a
# 0 1 2 3 4 5 6 7
# deci caracterul de pe pozitia 4 este e
# daca voiam sa aflam care este prima litera, am fi avut myString[0]

#### slicing
# prin slicing obtinem portiuni (felii) din stringuri
# syntaxa my_str[start:end:step]
# start - integer care specifica punctul de plecare. Optional
# stop - integer care specifica punctul de oprire
# step - este default 1, e optional

#exemplu:
myString = "cosmonaut"

# vrem sa obtinem cuvantul cosmo
new_string = myString[:5] # feliem incepand cu caracterul de pe pozitia 0 (c) pana la pozitia 5 (n)
# ATENTIE: punctul de oprire nu se ia in seama. pe pozitia 5 avem litera n, dar practic el s-a oprit la o
print(new_string) # va afisa cosmo

# vrem sa afisam naut
# varianta 1
new_string2 = myString[5:] # incepand cu caracterul 5 n, pana la final
print(new_string2)

# varianta 2
# specificam si punctul de inceput si punctul de sfarsit
# atentie, desi pozitia 9 nu exista, vom merge pana la 9 ca sa se ia in calcul ultimul caracter (pozitia 8)
new_string2 = myString[5:9]
print(new_string2)

#### cum parcurgem un string in sens invers cu slice?
# syntaxa: my_str[::-1] adica parcurgem tot stringul de la coada la cap (pas = -1)
my_var = "viteza"
print(my_var[::-1]) # ne va afisa azetiv


########## alte functii string ########
# myStr.upper() - converteste tot stringul in litere mari
myStr = "ana"
print(myStr.upper())  # va afisa ANA
# myStr.isupper() - returneaza True sau False. Verifica daca stringul e scris cu caractere mari
print(myStr.isupper())

"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
O variabila reprezinta un spatiu din memoria unui calculator, care contine mai multe date.

2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string
- int
- float
- bool
"""
culoare = "rosu" #string
an = 2010 #int
pret = 256.93 #float
nu_este_nou = True #bool

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
type(culoare)
print(type(culoare))
type(an)
print(type(an))
type(pret)
print(type(pret))
type(nu_este_nou)
print(type(nu_este_nou))

"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
"""
pret = round(256.93)
print(pret)
print(type(pret))
"""
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""
print(f"Am cumparat un trening {culoare}")
print(f"Masina mea este din anul {an}")
print(f"Am facut cumparaturi in valoare de {pret} lei")
assert nu_este_nou == True
print("Telefonul pe care l-am cumparat nu este unul nou")

"""
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""
numele = input("Alege un nume")
prenumele = input("Alege un prenume")
total = "numele+prenumele"
len("total")
print(f"Numele complet are {len(total)} caractere")

"""
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
"""
lungimea = int(input("Precizeaza lungimea"))
latimea = int(input("Precizeaza latimea"))
aria = lungimea * latimea
print(f"Aria dreptunghiului este {aria}")

"""
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
"""
x = "Coral is either the stupidest animal or the smartest rock"
numar = x.split()
print(numar.count("the"))

"""
9. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
"""
string = "Coral is either the stupidest animal or the smartest rock"
assert string.isnumeric() == True
print("String-ul nu este numeric")

"""
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
"""
string = input("Cuvant impar ")
poz = string[len(string)//2]
print(poz)

# 2. Folosind assert, verifică dacă un string este palindrom.

word = input("Introdu un string: ")
assert str(word) == str(word)[::-1]
print("Palindrom")
assert str(word) != str(word)[::-1]
print("Nu este palindrom")

"""
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
"""
string1 = input()
string2 = input()
print(f"{string1}\n{string2}")

"""
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
"""
name = input() #alabala portocala
name_modified = name[0] +name[1:-1].replace(name[0],name[0].upper()) + name[-1]
print(name_modified)

# CURS 2

############ STRING METHODS #############

#### .capitalize( ) ####
# modifica stringul astfel incat prima litera va fi mare si restul literelor vor fi mici
# syntax: str.capitalize()
myStr = "casa mea este Mica"
print(myStr.capitalize())

#### .endswith() ####
# verifica daca un string se termina cu litera data ca argument
# syntax: str.endswith("something")
myStr = "casa mea este Mica"
print(myStr.endswith("ca"))


#### .find( ) ####

# cauta un substring si returneaza indexul unde se gaseste
# este safe - nu returneaza o eroare daca ii dam un substring nonexistent ca parametru, cu -1
# functioneaza numai cu stringuri - nu incercati sa o aplicati pe alte secvente

## find() with one parameter ##
# syntax: str.find("substring")
my_string = "invat python"
print(my_string.find("at"))

## find() with 2 parameters ##
# if you want to search the substring starting with a certain index
# syntax: str.find("substring", poz)
my_string = "astazi nu vreau sa invat"
print(my_string.find("zi", 2))
fructe = "mere pere caise"
print(fructe.find("er"))

## find() with 3 parameters
# al treilea argument pointeaza catre primul index care nu va fi luat in considerare in cautare
# syntax: str.find("substring", poz, poz_end_search)
nume = "Maria Ioana Angelica Ion"
print(nume.find("Angelica", 0, 20))

#### .isalnum() ####
# verifica daca un string contine numai litere si cifre. Returneaza un bool -> True / False
mother = "Cristina10"
print(mother.isalnum())


#### .isalpha() ####
# verifica daca un string este format numai din litere si returneaza True / False
# syntax: str.isalpha()
# spatiile nu sunt considerate litere, sunt considerate caractere
my_string = "Am ani"
print(my_string.isalpha())


#### .isdigit() ####
# verifica daca un string este format numai din numere
# syntax: str.isdigit()
varsta = "28"
print(varsta.isdigit())


#### .islower() ####
# verifica daca un string este format numai din litere mici si returneaza True / False
# syntax: str.islower()
litera_mica = "am plEcat in vacanta"
print(litera_mica.islower())

#### .isspace() ####
# verifica daca stringul este format numai din spatii goale si returneaza True / False
# syntax: str.isspace()
spatiu = "am plecat"
spatiu2 = "   "
print(spatiu.isspace())
print(spatiu2.isspace())


#### .isupper() ####
# verifica daca un string este format numai din litere mari si returneaza True / False
# syntax: str.isupper()


#### .lower() ####
# face o copie a stringului original si inlocuieste toate literele mari din string cu litere mici si returneaza noul string ca rezultat
# the original string remains untouched.
# syntax: str.lower()


#### .upper() ####
# face o copie a stringului original si inlocuieste toate literele mici din string cu litere mari si returneaza noul string ca rezultat
# the original string remains untouched.
# syntax: str.upper()


#### replace() ####
# retruneaza o copie a stringului original in care toate aparitiile primului argument au fost inlocuite cu al doilea argument
# syntax: str.replace(arg1, arg2)

my_str = "cainele ma musca"
print(my_str.replace("cainele", "pisica"))

## exercitiu: ce returneaza urmatorul cod

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)
#Answer:


#### split() ####
# aceasta metoda considera ca stringurile sunt delimitate de spatii albe
# syntax str.split()
# example: print("phi       chi\npsi".split()) -> ['phi', 'chi', 'psi']
ex = "bujori flori trandafiri"
print(ex.split())


#### strip() ####
# returneaza un nou string fara spatii albe
# syntax: str.strip()


## exercitiu: ce returneaza urmatorul cod?

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
print(s2[-2])
#Answer: of

##ex 2
a = "Tomorrow I will leave my home"
b = a.split()
print(b)
print(b[-4])

#### swapcase() ####
# returneaza un nou string in care tipul de litere este inversat. litere mici -> litere mari , viceversa

s = "i WaS a BaD CaT"
print(s.swapcase())

############ OPERATORI ARITMETICI ###############


# Addition
a = 5
b = 275
c = 1985

print(a+b+c)

# Substraction

print(c - a + b)

# Multiplication
print(a * b)

# Division
a = 20
b = 10
print(a/b)

# Modulus
a = 5
b = 2
print(a%b)

# Exponentiation
a = 2
b = 3
print(a**b)

############ OPERATORI DE ATRIBUIRE #############

# " = "

a = 5
b = 888

# " += "
a = 6
a += 5 # a = a + 5 => a = 6 + 5
print(a)


# " -= "
b = 110
b -= 10 # => b = 110 - 10
print(b)

# " *= "
c = 3
c *= 2 # =>c = 3 * 2
print(c)

# " /= "
d = 22
d /= 11 # d = 22 /11
print(d)

d = 11
d /= 7
print(round(d))


############ OPERATORI LOGICI #############

# "and"
# returns TRUE if both statements are true
a = 0
b = 1
print(a and b)

# "or"
# returns true if one of the statements is true
c = 0
d = 0
print(c or d)

# "not"
e = 1
b = 6
print(not(b<e))
n = 10
s = 12
x = 2
print(not(n*2 < s and s < 15)) # => not( 20 < 12  and 12 < 15) => not( False and True ) => not (False) => True


############ OPERATORI DE COMPARARE #############
# string comparison is always case-sensitive --> upper-case letters are taken as lesser than lower-case letters.
# OBS! - nu comparam 2 tipuri diferite de date cu comparatorii <, > <=, >=, primim eroare "TypeError "


# " == "
a = 12
c = 10
print(a==c)


# " != "
print(a!=c)

# " > "
print(a > c)

# " < "
a = 12
c = 10
print(a < c)

# " >= "
s = 199
n = 200
print(n>=s)

# " <= "
print(n<=s)

##### if statament #####

# condition not fullfieled
a = 70
b = 10
c = a * b
if c > 1000:
    print("Yay valoarea lui c este mai mare decat 1000")
print(f"c are valoarea {c}")

# condition fullfilled
if c < 1000:
    print("valoarea lui c este mai mica decat 1000")
print(f"{c}")


#### if..else statements ####

a = "mama"
b = "Mama"

if a == b:
    print("Mama si cu tata merg la restaurant")
else:
    print("Mama sta acasa")

#### if else if statements ####

a = 12
b = 3
c = 3
s = b % c

if s == 0:
    print("s is an even number")
elif s < 2:
    print("S este mai mic decat 2")
elif b > c:
    print("b este mai mare decat c")
else:
    print("s este numar impar")
print("Se continua codul")


## ex 2
fruct1 = "pere"
fruct2 = "Pere"
alt_str = "tanculete"

if fruct1 == fruct2:
    print("Facem dulceata de pere")
elif fruct1 != alt_str:
    print("Nu mai facem dulceata")
else:
    print("I don't care")
print("Ai ajuns aici")


#### nested if else statements ####

nr1 = 24
nr2 = 25
s1 = "mama"
s2 = "mama"

if nr1 > nr2:
    if s1 == s2:
        print("conditia s-a indeplinit")
    else:
        print("Nu s-a indeplinit conditia")
else:
    print("Am intrat pe else clause")

"""
1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
In cazul unei propozitii adevarate, atribuite lui if, pyhton va rula conditia precizata in cadrul functiei if.
In caz contrar, codul va merge mai departe, ruland in consola printul atribuit functiei else.

2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
daca este numar intreg mai mare ca 0)
"""
x = input("Numar ")
if x.isnumeric():
    print("X este numar natural")
else:
    print("X nu este numar natural")

# 3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = int(input("Introdu un numar"))
if x > 0:
    print("Numarul este pozitiv")
elif x < 0:
    print("Numarul este negativ")
else:
    print("Numar neutru")

# 4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = int(input("Numar "))
if x in range(-2, 14):
    print("Da")
else:
    print("Nu")

"""
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs
"""
x = int(input("Numar "))
y = int(input("Numar "))
if abs(x-y) < 5:
    print("Diferenta este mai mica decat 5")
else:
    print("Diferenta este mai mare decat 5")

# 6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)

x = int(input("Numar "))
if x not in range(5, 27):
    print("X nu este intre 5 si 27")
else:
    print("X este intre 5 si 27")

# 7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare

x = int(input("Numar "))
y = int(input("Numar "))
if x == y:
    print("Numerele sunt egale")
elif x > y:
    print(x)
else:
    print(y)

"""
8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).
"""
x = int(input("Numar "))
y = int(input("Numar "))
z = int(input("Numar "))
if x == y == z:
    print("Triunghi echilateral")
elif x != y and y != z and x != z:
    print("Triunghi oarecare")
else:
    print("Triunghi isoscel")

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = input("Introdu o litera ")
lista_vocale = ["a","e","i","o","u"]
if litera.lower() in lista_vocale:
    print("Vocala")
else:
    print("Consoana")

"""
10. Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F
"""
nota = input("Nota ")
if nota > "9":
    print("A")
elif nota > "8" or nota == "9":
    print("B")
elif nota > "7" or nota == "8":
    print("C")
elif nota > "6" or nota == "7":
    print("D")
elif nota > "4" or nota == "6":
    print("E")
else:
    print("F")

# 1. Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

x = int(input("Numar "))
if x.bit_count() >= 4:
    print("yes")
else:
    print("no")

# 2. Verifica daca x are exact 6 cifre

x = input("Numar ")
if len(x) == 6:
    print("Yes")
else:
    print("No")

# 3. Verifica daca x este numar par sau impar

x = int(input("Numar "))
if x % 2 == 0:
    print("Numar par")
else:
    print("Numar impar")

# 4. Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre
# ele

x = int(input("Numar "))
y = int(input("Numar "))
z = int(input("Numar "))
lista = [x, y, z]
print(max(lista))

"""
5. Presupunand ca x, y, z - reprezinta unghiurile unui triunghi, verifica si afiseaza daca
triunghiul este valid sau nu (un triunghi este valid daca suma tuturor unghiurilor este de
180 de grade sau daca suma lungimilor a oricare doua laturi este mai mare decat
lungimea celei de-a treia laturi)
"""
x = int(input("Numar "))
y = int(input("Numar "))
z = int(input("Numar "))
if x+y+z == 180:
    print("Triunghi valid")
else:
    print("Triunghiul nu este valid")

"""
6. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' citește de
la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. ex: dacă
ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the
smarte'
"""
str = "Coral is either the stupidest animal or the smartest rock"
x = int(input("Numar "))
print(str[:-x])

"""
7. Folosindu-te de același string de la exercițiul 6, declara un string nou care sa fie format
din primele 5 caractere + ultimele 5
"""
str = "Coral is either the stupidest animal or the smartest rock"
new_str = str[:5] + str[-5:]
print(new_str)

"""
8. Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza
indexul de start al cuvântului rock - adică poziția in string la care începe cuvântul rock
(hint: este o funcție care te ajuta sa faci asta). Folosind aceasta variabila + slicing,
afișează tot stringul pana la acest cuvant. Output asteptat: 'Coral is either the stupidest
animal or the smartest '
"""
str = "Coral is either the stupidest animal or the smartest rock"
index = str.find("rock")
print(index)
print(str[:index])

"""
9. Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel. Se
va folosi un assert. Atentie: se dorește ca programul sa fie case insensitive, adica 'apA'
e acceptat ca un string in care primul si ultimul caracter este la fel (hint, te poti folosi de o
functie pentru a face string-ul case insensitive)
"""
str = "Coral is either the stupidest animal or the smartest rock"
first_character = str[0]
last_character = str[-1]
assert first_character.lower() == last_character.lower()
print("Yes")

# 10. Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)

str = "0123456789"
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nos = [num for num in list1 if num % 2 == 0]
print(even_nos)
odd_nos = [num for num in list1 if num % 2 != 0]
print(odd_nos)

"""
1. Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l cu toate
variantele care crezi ca ar trebui testate. Genereaza scenarii de testare cu expected results si
apoi ruleaza codul pentru a verifica daca expected results sunt egale cu actual results.
Exemple:
1. Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
2. Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
"""
varsta = int(input("Introdu varsta: "))
insotit_de_mama = input("Insotit de mama:Yes or not: ")
insotit_de_tata = input("Insotit de tata:Yes or not: ")
pasaport = input("Pasaport:Yes or not: " )
act_permisiune_mama = input("Permisiunea mama:Yes or not: ")
act_permisiune_tata = input("Permisiune tata:Yes or not: ")
if varsta >= 18 and pasaport == "yes":
    print("Persoana se poate imbarca")
elif varsta <= 18 and pasaport == "yes" and insotit_de_tata == "yes" and insotit_de_mama == "yes":
    print("Persoana se poate imbarca")
elif varsta <= 18 and pasaport == "yes" and insotit_de_mama or insotit_de_tata == "yes" and act_permisiune_tata or act_permisiune_mama == "yes":
    print("Persoana se poate imbarca")
else:
    print("Imbarcarea nepermisa")

# persoana are 20 ani si are pasaport => "Persoana se poate imbarca"
# persoana are 15 ani, are pasaport si e insotita doar de mama => "Imbarcare nepermisa"
# persoana are 12 ani, are pasaport, e insotita de mama si are permisiunea tatalui => "Persoana se poate imbarca"

"""
2. Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y
"""

import random
zar=[1,2,3,4,5,6]
dice_roll = random.choice(zar)
print(dice_roll)
nr_ghicit = int(input("Numar "))
if nr_ghicit < dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {nr_ghicit} dar a fost {dice_roll}")
elif nr_ghicit > dice_roll:
    print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {nr_ghicit} dar a fost {dice_roll}")
else:
    print(f"Ai ghicit. Felicitari! Ai ales {nr_ghicit} si zarul a fost {dice_roll}")


#### Exercitiul 1 ####
# Creaza 2 variabile de tip string, primua cu valoarea "veni vidi vici" si a doua cu valoarea "alea iacta est"
# a) Afiseaza cate caractere are primul string
# b) Afiseaza cate caractere are al doilea string
# c) Elimina spatiile albe din primul string

str1 = "veni vidi vici"
str2 = "alea iacta est"
print(len(str1))
print(len(str2))
print(str1.split())

#### Exercitiul 2 ####
# Creaza variabila s1 de tip string si asigneaza-i valoarea "veni vidi vici"
# a) Foloseste o metoda string astfel incat sa se afiseze veni, vidi, vici
# b) Creeaza o noua variabila de tip string in care sa stochezi numarul de "i" care apar in s1 si afiseaza-i valoarea.
# c) Inlocuieste in s1 litera "v" cu litera "a"

s1 = "veni vidi vici"
s2 = s1.count("i", 0, 14)
print(s2)
print(s1.replace("v", "a"))

#### Exercitiul 3 ####
# Citeste un string format din 6 litere de la tastatura si afiseaza litera de pe pozitia 4.

s1 = input("Introdu un cuvant format din 6 litere ")
print(s1[4])

#### Exercitiul 4 ####
# Avem variabila x = "astazi am avut o sedinta lunga si obositoare"
# Foloseste o metoda string astfel incat propozitia sa inceapa cu litera mare.

x = "astazi am avut o sedinta lunga si obositoare"
print(x.capitalize())

#### Exercitiul 5 ####
# Citeste de la tastatura un string format din 3 cuvinte (exemplu: am plecat azi)
# a) Afiseaza o parte din string care sa contina ultimile 2 litere din al doilea cuvant si prima litera din al treilea cuvant, fara sa contina spatii albe intre ele
# b) Transforma stringul obtinut la punctul a) intr-un string care contine numai litere mari

str = input("Introdu o propozitie din 3 cuvinte ")
print(str.upper())

#### Exercitiul 6 ####
# Creeaza cate o variabila tip string pentru fiecare zi a saptamanii (exemplu: day02="Tuesday")
# a) Afiseaza toate zilele saptamanii pe un singur rand cu virgula intre ele.
# b) salveaza stringul obtinut la punctul b) intr-o variabila
# c) Afiseaza pe ce pozitie se regaseste prima litera din Sunday
# d) Afiseaza cate litere are Sunday

d1 = "Monday"
d2 = "Tuesday"
d3 = "Wednesday"
d4 = "Thursday"
d5 = "Friday"
d6 = "Saturday"
d7 = "Sunday"
saptamana = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
print(saptamana)
print(saptamana.find("Sunday"))
print(len("Sunday"))


#### Exercitiul 1 ####
# Afisati in consola rezultatul expresiei:  10 * 100 - (2**3 + 6 ** 2) - 290

a = 10 * 100 - (2**3 + 6 ** 2) - 290
print(a)

#### Exercitiul 2 ####
# Afiseaza in consola rezultatul lui 24 la puterea a 3-a (i.e Rezultatul lui 24 la puterea a 3-a este: ). Folositi un output formatat.

x = 24 ** 3
print(f"Rezultatul lui 24 la puterea a 3-a este {x}")

#### Exercitiul 3 ####
# Sa se calculeze si sa se afiseze in consola n la puterea 7, unde n este citit de la tastatura.

n = int(input("Introdu un numar "))
print(n**7)

#### Exercitiul 4 ####
# Avem 2 numere intregi citite de la tastatura. Daca valoarea primului numar este mai mare decat valoarea celei de-al doilea, atunci sa se afiseze
# in consola "I have a dog". Daca nu este mai mare, atunci sa se afiseze "I have a cat".

a = int(input("Numar "))
b = int(input("Numar "))
if a > b:
    print("I have a dog")
else:
    print("I have a cat")

#### Exercitiul 5 ####
# Avem 2 numere intregi citite de la tastatura.
# Creeaza variabila x si asigneaza-i valoarea 3.
# Aduna numerele introduse de la tastatura si rezultatul afiseaza-l ridicat la puterea valorii lui x.

a = int(input("Numar "))
b = int(input("Numar "))
x = 3
y = a + b
print(y**x)

#### Exercitiul 6 ####
# Avem a = 0, b = 1, c = 0, d = 1
# Afiseaza ce returneaza urmatoarea operatie not(a or b and c or d)

a = 0
b = 1
c = 0
d = 1
print(not(a or b and c or d)) #=> False

#### Exercitiul 7 ####
# Avem s = 1 si x = 0
# Ce operator/i punem intre s si x daca vrem sa obtinem True? - 2 modalitati.

s = 1
x = 0
print((s or x))
print(not(s and x))


#### Exercitiul 1 ####
# a) Sa se citeasca de la tastatura un cuvant.
# b) Sa se verifice daca cuvantul introdus de la tastatura are toate literele mari. Daca nu are toate literele mari, atunci sa se converteasca cuvantul in litere mari.

str = input("Introdu un cuvant ")
print(str.isupper())
print(str.upper())

#### Exercitiul 2 ####
# a) Sa se citeasca de la tastatura 3 numere.
# b) Sa se determine daca cele 3 numere sunt pare. Daca cele 3 numere sunt pare, atunci sa se afiseze "Toate numerele sunt pare"
# Daca fie si unul dintre numere este impar, atunci sa se afiseze "Nu toate numerele sunt pare"

a = int(input("Numar "))
b = int(input("Numar "))
c = int(input("Numar "))
if a%2==0 and b%2==0 and c%2==0:
    print("Toate numerele sunt pare")
else:
    print("Nu toate numerele sunt pare")

#### Exercitiul 3 ####
# a) Sa se citeasca de la tastatura un string
# b) Sa se determine daca numarul caracterelor stringului citit de la tastatura este mai mare de 6. Daca numarul este mai mare decat 6,
# atunci sa se afiseze "Numarul de caractere este mai mare decat 6", altfel "Numarul este mai mic decat 6".

my_str = input("scrie ceva ")
if len(my_str) > 6:
    print("Numarul de caractere este mai mare decat 6")
else:
    print("Numarul este mai mic decat 6")


#### Exercitiul 4 ####
# a) Sa se creeze un log in cu username si parola introduse de la tastatura
# b) Sa se compare valorile. Pentru fiecare caz afisam urmatoarele:
# Caz1: user corect - parola gresita -> "Wrong password"
# Caz2: user gresit - parola corecta -> "Wrong username"
# Caz3: user gresit - parola gresita -> "Wrong username and password"
# Caz4: user si parola corecte -> "Logged in"

user = "Madalina"
user1 = input("Introdu user-ul: ")
parola = "Madalina"
parola1 = input("Introdu parola: ")
if user1 == user and parola1 != parola:
    print("Wrong password")
elif user1 != user and parola1 == parola:
    print("Wrong username")
elif user1 != user and parola1 != parola:
    print("Wrong username and password")
else:
    print("Logged in")


# CURS 3

# lista goala
myList = []
print(myList)

#lista cu elemente mixte

myList1 = ["mama", 13, True, 13.5, True, False, "miau"]

# elementul de pe pozitia 2
print(myList1[2])

# de cate ori apare True in myList1
print(myList1.count(True))
myList1[2] = "corect"
print(myList1)

# extindem o lista
ls1 = [1,2,3,4]
ls2 = ["tata", "mama", "max"]
ls1.extend(ls2)
print(ls1)

# adaugam un element cu append() la lista
ls3 = [1,2,3,4]
ls4 = ["tata", "mama", "max"]
ls3.append(ls4)
print(ls3)
print(len(ls3))
print(len(ls1))

######### tuple ##########

# cream o tupla cu string
myTuple = ("mama", "unu", "portocala")

# afisam elem de pe pozitia 0
print(myTuple[0])

# verificam daca elementul "unu" este in tupla - returneaza True sau False
print("unu" in myTuple)

### exercitii

# avem o lista. sa se afle elemntul de pe pozitia 1.
# sa se inlocuiasca elemntul de pe pozitia 1 cu "bingo"
# daca valoarea veche a elementului de pe pozitia 1 este in lista, atunci vom afisa "I am here"

lt = [12, 5, "tata", True, False, "gaina"]
poz1 = lt[1]
lt[1] = "bingo"
if poz1 in lt:
    print("I am here")


###### seturi ########

# definim un set
ms = {"iarna", "toamna", "primavara", "vara"}

# printam lungimea setului
print(len(ms))

# adaugam cu add() elemente in lista
ms.add("frig")
ms.add("cald")
ms.add("rece")
ms.add("fierbinte")
print(ms)

# adaugam o tupla la set
ms.add((1,2, False))
print(ms)
# definim o tupla
tp = ("n", 2, 5)
ms.add(tp)
print(ms)

# remove element from set
ms.remove("frig")
print(ms)
ms.discard("fierbinte")
print(ms)

# remove an element that doesn't exists that doesn't exist
# renove - returnes an error, discard ignores it.
ms.remove("ciorap")
ms.discard("ciorap")



######## dictionare ##########

dict1 = {"a": 2, "b":3, "c":4}

# afisam valoarea lui b
print(dict1["b"])

dt = {"tip_carte": "roman", "editura": "Corint",
      "Autor": "Agatha Christie", "nr_pag": 250,
      "carti": ["Cu cartile pe fata", "Oglinda", "Crima in Orient Expres"]}

# din cheia carti vrem sa obtinem cartea 2
cartea2 = dt["carti"][1]
print(cartea2)


# daca numele cartii 2 este "Cianura" atunci afisam "Nu am citit", altfel
# "Am citit"
if cartea2 == "Cianura":
    print("Nu am citit")
else:
    print("Am citit")

# sa se numere caracterele valorii cheii 2. Daca lungimea este mai mare
# decat 7 si primul caracter este litera mica, sa se afiseze "Great"

# aflam valoarea cheii editura
val = dt["editura"]
print(val)
lungime = len(val)
print(len(val))
val1 = val[0]
if lungime > 7 and val1.islower():
    print("Great")
else:
    print("first letter is not lower")

tpl1 = (1, 6, 8)
print(list(tpl1))

print(tuple(tpl1))
print(set(tpl1))

tuple()
set()
list()


"""
1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
"""
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale2 = note_muzicale[::-1]
print(note_muzicale2)
note_muzicale2.reverse()
print(note_muzicale2)

# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.

note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale.count("do"))

# 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

# Metoda 1:
lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
lst1.append(lst2)
print(lst1)

# Metoda 2:
lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
lst1.extend(lst2)
print(lst1)

# 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
# folosind o functie si apoi afiseaza din nou lista

lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
lst1.extend(lst2)
lst1.sort()
lst1.remove(0)
print(lst1)

"""
5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)
"""
lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
lst1.extend(lst2)
if lst1 == []:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# 6. Foloseste o functie care sa goleasca lista de la exercitiul 3

lst1.clear()
print(lst1)

# 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
# afiseze ca lista e goala

if lst1 == []:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
# afisezi Elevii (cheile)

dict1 = {"Ana": 8, "Gigel": 10, "Dorel": 5}
print(dict1.keys())

"""
9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie
"""
nota1 = dict1["Ana"]
nota2 = dict1["Gigel"]
nota3 = dict1["Dorel"]
print(f"Ana a luat nota {nota1}.")
print(f"Gigel a luat nota {nota2}.")
print(f"Dorel a luat nota {nota3}.")

"""
10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
- Modifica nota lui Dorel in 6
- Printeaza nota lui dupa modificare
"""
dict1["Dorel"] = 6
print(dict1["Dorel"])

"""
11. Imagineaza-ti ca Gigel se transfera din clasa.
- Cauta o functie care sa il stearga
Vine un coleg nou.
- Adaugati-l in lista pe Ionica, cu nota 9
- Printati dictionarul cu noii elevi
"""
del dict1["Gigel"]
dict1["Ionica"] = 9
print(dict1)

"""
12. Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
"""
zile_sapt = {"luni", "marți", "miercuri", "joi", "vineri", "sâmbăta", "duminică"}
weekend = {"sâmbăta", "duminică"}
zile_sapt.add("luni")
print(zile_sapt)

"""
13. Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean
"""
if weekend.issubset(zile_sapt):
    print("Weekend este un subset al zilelor din săptămânii")
else:
    print("Weekend nu este un subset al zilelor din săptămânii")


# 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# sunt in weekend si invers)

print(zile_sapt.difference(weekend))

# 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
# ambele seturi). Hint: Va puteti folosi de o functie

print(zile_sapt.intersection(weekend))


# CURS 4

import time
###### loops #####

# exercitiu

# write a program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd
# The program terminates when zero is entered

# What we need?
# var - odd numbers
# var - even numbers
# input()

# we declare 2 vars for odd number and even numbers and we set it to 0
odd_numbers = 0
even_numbers = 0

#read the number first
number = int(input("Enter a number or type 0 to stop: "))
# # 0 terminates the execution
while number != 0:
    # Check if the number is odd
    if number % 2 == 1:
        # Increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increse the even_numbers counter
        even_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))

print("Too bad, user entered 0")
print("Odd numbers count: ", odd_numbers)
print("Even numbers count: ", even_numbers)


### exercitiul 2
# make a counter that counts the last 10 seconds until new year
# after the last second print "Happy new year"

# avem nevoie de o variabila counter

counter = 10
while counter:
    print(counter, "seconds left")
    #se scade o secunda
    counter -=1
    time.sleep(1)
print("Happy new year!!!!!!!!", counter)

############## for #####

###exercitiul 1

# write a for loop that counts to five.
# body of the loop - print the loop iteration number and the word "Mississippi"
# use time.sleep1(1)
# write a print function with the final message

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
print("I will search you and I'll find you!")


#### exercitiul 2

# Define a new list with 7 elements.
# We want to calculate the sum of all the numbers inside the list

#We need: o lista, variabile sum.

my_list = [5, 7, 1, 3, 10, 20, 30]
sum = 0 # we start with a counter that we initialize with 0 (we haven't added any number yet)

for i in my_list:
    print(f"Adding {i} to {sum}")
    sum += i #as long as we haven't reached the end of the list we will
            # add the current element to the previous total
    print(f"Current sum is {sum}")
else:
    print("We are done with the sum")
print(f"The sum of the elements in the list is : {sum}")

######## break ########

print("The break instruction: ")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop")

# ###### continue #######

print("The continue instruction")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop")


########for each ########

# avem o lista cu 6 animale
# # parcurgem lista cu cele 6 animale si printam "I love this animal"
#
animals = ["zebra","tigru","maimuta", "iepure", "dinozaur", "pantera", "tapir"]

for animal in animals:
    print(f"I love this animal --> {animal}")

######## exercices ########

# a junior magician has picked a secret number
# he has hiddent it in avariable named secret_number
#he want everyone to run his program to play Guess the secret number
#if the user doesn't guess the number he will be stuck in the loop
# if he guessed the number, then magician will let him out

secret_number = 200

print ("====Welcome to my game human!====")

user_nr = int(input("Enter a number: "))

while user_nr != secret_number:
    print("You are stuck in my loop, ha ha ha!")
    user_nr = int(input("Enter the number again: "))
print(secret_number, "Well done human! You are free now!")

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""
# for
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)):
    print("Masina mea preferata este", masina2)
    time.sleep(1)

# for each
for masina in masini:
    print("Masina mea preferata este", masina)
    time.sleep(1)

# while
x = 0
while x < len(masini):
    print(f'WHIE: Masina mea preferata este: {masini[x]}')
    x = x + 1

"""
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
"""
for masina in range(1, len(masini)-1):
    masini[masina] = masini[masina].upper()
print(masini)

"""
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
for x in masini:
    if x == "Mercedes":
        print("Am gasit masina dorita de dvs")
        break
    else:
        print(f"Am gasit masina {x}. Mai cautam")

"""
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""
for x in masini:
    if x == "Trabant" or x == "Lastun":
        continue
        print(f"S-ar putea sa va placa masina {x}")

"""
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
"""
masini = ["Audi", "Volvo", "BMW", "Mercedes", "Aston Martin", "Lastun",
          "Fiat", "Trabant", "Opel"]
masini_vechi = []
for i in masini:
    if i == "Lastun" or i == "Trabant":
        masini_vechi.append(i)
        print(masini_vechi)

for i in range(len(masini)):
    if masini[i] == "Trabant" or masini[i] == "Lastun":
        masini[i] = "Tesla"
        print(masini)
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")

"""
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
"""
pret_masini = {'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000}
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de pana in {buget} euro puteti alege masina: {masina}')

"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

x = 0
for numar in numere:
    if numar == 3:
        x = x + 1
print(f'Numarul 3 apare de {x} ori in lista de numere')

"""
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
total = 0
for x in range(len(numere)):
    total = total + numere[x]
print("Suma listei este: ", total)

"""
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere.sort()
for x in numere:
    print(f"Numarul cel mai mare este {numere[-1]}")

"""
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_neg = []
for numar in numere:
    if numar > 0:
        numar = numar - numar*2
        #numar = -(abs(numar)) # alta solutie
    lista_neg.append(numar)
print(f'Lista a devenit: {lista_neg}')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
"""
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar >= 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print("Numerele pare sunt: ", numere_pare)
print("Numerele impare sunt: ", numere_impare)
print("Numerele pozitive sunt: ", numere_pozitive)
print("Numerele negative sunt: ", numere_negative)

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)

"""
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""
import random
numar_secret = random.randint(1,30)
numar_ghicit = None
print(numar_secret)
user_nr = int(input("Numar "))
while user_nr < numar_secret:
    print("Nr secret e mai mare")
if user_nr > numar_secret:
    print("Nr secret e mai mic")
if user_nr == numar_secret:
    print("Felicitari! Ai ghicit!")

"""
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
"""
nr = int(input("Scrie un numar: "))
i = 1
while i <= nr:
    print(' ')
    for j in range(i):
        j = i
        print(j, end='')
        j = j + 1
    i = i + 1

"""
5. tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
"""
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')


# CURS 5

###### Turn this snipet into a function

print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

### define the function

def get_value():
    print("Enter a value: ")


print("We start here")
get_value()
print("We end here")


##### positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


introduction("Luke", "Skywalker")
introduction("Clark", "Kent")
introduction("Jessie", "J")
introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")


#### functie cu parametru predefinit

def introduction_a(first_name, last_name = "Smith"):
    print("Hello, my name is", first_name, last_name)


introduction_a("Diana")

##### return fara argumente ####


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy new year")


happy_new_year()


##### functie cu un argument gresit

def introduction_b(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction_b("Luke")

##### return cu argumente - folosit
def boring_function():
    a = 345
    return a

x = boring_function()
print("The boring_function has returned its result. It's: ", x)


#### nu folosim ce returneaza

def boring_function_a():
    print("'Boredom Mode' ON.")
    return 123

print("This is quite interesting!")
boring_function_a()
print("This lesson is boring...")

#### invocam functie cu lista

def list_sum(my_list):
    s = 0

    for item in my_list:
        s += item
    return s

print(list_sum([10, 20, 30]))
print(list_sum(6))


##### function that returns a list #######
########## exercitiu pt tema - explica functia si insertul   ###

def my_strange_list(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(2, i)

    return strange_list

print(my_strange_list(5))

########## functie -> valoarea absoluta a unui numar


def absolute_value(num):
    """
    This function returns the absolute value of the entered number
    :param num:
    """
    if num >=0:
        return num
    else:
        return -num


print(absolute_value(int(input("Introduceti un numar: "))))
print(absolute_value(-4))


#### functia cu un nr necunoscut de argumente

def multiple_args(*fruits):
    print(f"I really like {len(fruits)} fruits, they are: {fruits}")

multiple_args("mar", "cireasa", "banana", "piersica")


def multiple_args(**name):
    print((name["fam_name"] + " " + name["first_name"]))

def main():
    multiple_args(fam_name="Barbu",
                  first_name="Georgiana")

main()


# 1.Funcție care să calculeze și să returneze suma a două numere

def sum():
    a = int(input("Introdu un numar "))
    b = int(input("Introdu un numar "))
    return a+b
print(sum())

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def number():
    x = float(input("Introdu un numar "))
    if x % 2 == 0:
        return True
    else:
        return False
print(number())

#3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def introduction(first_name, middle_name, last_name):
    return len(first_name+last_name+middle_name)
print(introduction("Madalina", "Iuliana", "Nica"))

# 4. Funcție care returnează aria dreptunghiului

def aria_dreptunghiului():
    a = int(input("Introdu lungimea dreptunghiului "))
    b = int(input("Introdu latimea dreptunghiului "))
    return a*b
x = aria_dreptunghiului()
print("Aria dreptunghiului este ", x)

# 5. Funcție care returnează aria cercului

def aria_cercului():
    pi = 3.14
    r = float(input("Introdu raza cercului "))
    return pi*r*r
x = aria_cercului()
print("Aria cercului este", x)

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.

def string():
    x = input("Caracter ")
    my_str = input("String ")
    if x in my_str:
        return True
    else:
        return False
print(string())

"""
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""
import re
def string():
    x = input("Introdu un string cu litere mari si mici: ")
    upper_case = re.findall(r"[A-Z]", x)
    lower_case = re.findall(r"[a-z]",x)
    print("Uppercase character count: ", len(upper_case))
    print("Lowercase character count: ", len(lower_case))
string()

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

lista_numere = [1, -4, 78, -5, 0, 85, 4, -10, -2]
def numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive
print(numere_pozitive(lista_numere))

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale.
"""
def nothing():
    x = int(input("Numar "))
    y = int(input("Numar "))
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
    elif x < y:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print("Numerele sunt egale")
nothing()

"""
10. Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""
set_numere_input = {2, 5, 8, 78, -8, 45}
set_numere_input = {2, 5, 8, 78, -8, 45}
def adaugare_numar(set_numere, numar_nou):
    if numar_nou in set_numere:
        print(f'nu am adaugat numarul {numar_nou} in set, exista deja')
        return False
    else:
        set_numere.add(numar_nou)
        print(f'am adaugat numarul {numar_nou} in set')
        return True
print(adaugare_numar(set_numere_input, 78))
print(adaugare_numar(set_numere_input, 75))

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna
from calendar import monthrange
def number():
    year = 2022
    month = int(input("Introdu luna: "))
    return monthrange(year, month)[1]
print(number(year="", month=""))

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.

def calculator():
    x = int(input("Nr: "))
    y = int(input("Nr: "))
    a = x+y
    b = x - y
    c = x * y
    d = x / y
    return a,b,c,d
a,b,c,d = calculator(10,2)
print("Suma:", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

"""
3. Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1}
"""
lista1 = [1, 1, 2, 7, 7, 7]
def count(lista):
    cnt = {0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0}
    for i in cnt.keys():
        for j in lista:
            if i == j:
                cnt[i] = cnt[i] + 1
    return cnt
print(count(lista1))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def maxim():
    x = int(input("Nr: "))
    y = int(input("Nr: "))
    z = int(input("Nr: "))
    print("Valoarea maxima este: ")
    return max(x,y,z)
print(maxim())

"""
5. Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
"""
def suma_num(a):
    suma = 0
    for i in range(0, a + 1):
        suma = suma + i
    return suma
print(suma_num(3))

"""
1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
def comun(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return a_set & b_set
a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 1]
print(comun(a, b))

"""
2. Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
"""
def reducere_preturi(price, sale):
    if sale > 100 or sale < 0:
        return 'reducere invalida'
    new_price = price - (sale / 100) * price
    return new_price
print(reducere_preturi(100, 10))
print(reducere_preturi(100, -1))
print(reducere_preturi(100, 101))

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

from datetime import datetime
def data_ora():
    date_time = datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and Time: ", dt_string)
data_ora()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)

def amr_xmas(year):
    christmas_day = date(year=year, month=12, day=25)
    days_til_christmas = (christmas_day - date.today()).days
    return days_til_christmas
print(amr_xmas(2022))


# CURS 6

class Student:
  numar_studenti = 0 # atribut, apartine clasei Student =? variabila de clasa

  def __init__(self, nume, prenume, medie):
    self.nume = nume # variabila care apartine obiectului => var de instanta/obiect
    self.prenume = prenume # variabila care apartine obiectului => var de instanta/obiect
    self.medie = medie # variabila care apartine obiectului => var de instanta/obiect

   # Referirea la variabila de instanță nume se face cu notația self.nume în metodele acelui obiect
    print("Initializare studenti: ",self.nume,self.prenume)
    # Referirea la variabila de clasă numar_studenti se face cu notaţia Student.numar_studenti şi nu cu self.numar_studenti
    Student.numar_studenti += 1

  def test_bursier(self):

   if self.medie>=9.50:
    print("Bursa de merit")
   elif 8.50<=self.medie<9.50:
    print("Bursa studiu")

# O variabilă de obiect cu același nume ca o variabilă de clasă, va ascunde variabila de clasă faţă de metodele clasei!
# Metoda nr_studenti este în fapt o metodă  a clasei şi nu a instanţei. Asta înseamnă că trebuie să o definim cu declaraţia static method.

  def nr_studenti():
    print("Exista",Student.numar_studenti,"instante.")
  nr_studenti = staticmethod(nr_studenti)

student1 = Student('Bucur','Tudor',10)
student1.test_bursier()
Student.nr_studenti()
student2 = Student('Enache','Stefan',9)
student2.test_bursier()
Student.nr_studenti()

"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""
class Cerc:
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        return f"Culoarea cercului este {self.culoare},"\
               f"iar raza este {self.raza}"

    def aria(self):
        a = 3.14 * self.raza * self.raza
        return a

    def diametru(self):
        d = 2 * self.raza
        return d

    def circumferinta(self):
        c = 2 * 3.14 * self.raza
        return c

cerc1 = Cerc(int(input("Introdu raza: ")), input("Introdu culoarea: "))
print(cerc1.descrie_cerc())
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

"""
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""
class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return f"Lungimea dreptunghiului este: {self.lungime}," \
               f"latimea este: {self.latime}, iar culoarea este: " \
               f"{self.culoare}"

    def aria(self):
        a = self.latime * self.lungime
        return a

    def perimetru(self):
        p = 2 * (self.latime + self.lungime)
        return p

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        return self.culoare

dreptunghi1 = Dreptunghi(12, 8, "rosu")
print(dreptunghi1.descrie())
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
print(dreptunghi1.schimba_culoarea("verde"))

"""
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return f"Angajatu este {self.prenume} si are un salariu de " \
               f"{self.salariu} lei"

    def nume_complet(self):
        return f"Numele sau complet este: {self.nume} {self.prenume}"

    def salariu_lunar(self, s_lunar):
        self.s_lunar = s_lunar
        return f"Salariu lunar al lui {self.prenume} este de " \
               f"{s_lunar} lei"

    def salariu_anual(self, s_anual):
        self.s_anual = s_anual
        return f"Salariu anual al lui {self.prenume} este de " \
               f"{s_anual} lei"

    def marire_salariu(procent):
        Angajat.salariu += 10
        return f"Salariu sau se va mari cu {Angajat.salariu}%"


angajat1 = Angajat("Popovici", "Andrei", 4698)
print(angajat1.descrie())
print(angajat1.nume_complet())
print(angajat1.salariu_lunar(2658))
print(angajat1.salariu_anual(12589))
print(angajat1.marire_salariu())

"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""
class Cont:
    iban = 0
    titular_cont = None
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return f"Titularul {self.titular_cont} are in contul" \
               f"{self.iban} suma de {self.sold} lei"

    def debitare_cont(suma):
        Cont.sold = 1256
        sold_nou = suma.sold - Cont.sold
        return f"Suma ramasa in cont dupa debitarea cu {Cont.sold} " \
               f"lei, este de {sold_nou} lei"

    def creditare_cont(suma):
        Cont.sold = 895
        sold_nou = suma.sold + Cont.sold
        return f"Dupa creditarea cu {Cont.sold} lei, clientul are " \
               f"in cont {sold_nou} lei"

cont1 = Cont("RO25BTRL1234567899874563", "Popovici Andrei", 3654)
print(cont1.afisare_sold())
print(cont1.debitare_cont())
print(cont1.creditare_cont())

"""
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
"""

from tabulate import tabulate
from datetime import date


class Factura:
    seria = "XYZ"
    numar = 0
    nume_produs = None
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(cantitate):
        Factura.cantitate = 2
        cantitate.cantitate = Factura.cantitate
        return f"Noua cantitate va fi: {cantitate.cantitate} bucati"

    def schimba_pretul(pret):
        Factura.pret_buc = 8
        pret.pret_buc = Factura.pret_buc
        return f"Pretul pe bucata este acum de: {pret.pret_buc} lei"

    def schimba_nume_produs(nume):
        Factura.nume_produs = "Toffifee"
        nume.nume_produs = Factura.nume_produs
        return f"Produsul se numeste: {nume.nume_produs}"

    def genereaza_factura(self):
        a = Factura.cantitate * Factura.pret_buc
        d = [["Toffifee", 2, 8, a]]
        return tabulate(d, headers=["Produs", "Cantiate",
                                    "Pret bucata", "Total"])


factura1 = Factura(1234, "Milka", 4, 5)
print(factura1.schimba_cantitatea())
print(factura1.schimba_pretul())
print(factura1.schimba_nume_produs())
print(f"Factura seria {Factura.seria} numar {factura1.numar}")
print(date.today())
print(factura1.genereaza_factura())

"""
2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0
"""
class Masina:
    marca = 'Dacia'
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = ['rosu', 'verde', 'alb', 'albastru', 'portocaliu', 'negru', 'galben']
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masinii este: {self.marca}')
        print(f'Modelul masinii este: {self.model}')
        print(f'Viteza maxima a masinii este: {self.viteza_maxima}')
        print(f'Viteza actuala a masinii este: {self.viteza_actuala}')
        print(f'Culoarea masinii este: {self.culoare}')
        print(f'Masina este inamtriculata: {self.inmatriculata}')

    def inmatriculare(self):
        self.inmatriculata = True
        return self.inmatriculata

    def vopseste_masina(self, noua_culoare):
        if noua_culoare in self.culori_disponibile:
            self.culoare = noua_culoare
            print(f'Noua culoare a masinii este: {self.culoare}')
        else:
            print('Culoarea aleasa de dvs nu este in paletarul nostru.')

    def accelereaza(self, viteza_dorita):
        if viteza_dorita < 0:
            print('EROARE!')
        elif viteza_dorita >= self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza_dorita
        print(f'Viteza actuala este: {self.viteza_actuala}')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Viteza actuala este: {self.viteza_actuala}. Am oprit masina.')

"""
3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
dict
"""
class ToDoList:
    dict = {}

    def adauga_task(self, nume_task, descriere_task):
        self.dict[nume_task] = descriere_task
        print('Am adaugat taskul cu succes')

    def finalizeaza_task(self, nume_task):
        del self.dict[nume_task]

    def afiseaza_todo_list(self):
        print(f'Task-urile din TODO sunt: {self.dict.keys()}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.dict:
            print(f'Detalii pt taskul {nume_task}: {self.dict[nume_task]}')
        else:
            print('Nu am gasit taskul dorit')
            raspuns = input('Vrei sa adaugi task ul in lista?')
            if raspuns.lower() == 'da':
                descriere_task = input('Introdu descrierea pentru noul task: ')
                self.dict[nume_task] = descriere_task
                print('Am adaugat taskul cu succes')
            elif raspuns.lower() == 'nu':
                print('La revedere!')


# CURS 7

# Mostenirea
# mostenirea se foloseste cand avem 2 sau mai multe clase similare

# cream clasele Cat and Dog

# cream o clasa generala numita Pets

# clasa parinte
class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what sounds I make")

#clasa copil
class Cat(Pets):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # def speak(self):
    #     print("Meeeeow")

# clasa copil
class Dog(Pets):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def speak(self):
        print("Bark")

# class child Fox mosteneste class parinte Pets
class Fox(Pets):
    pass


fox = Fox("Snow", 1)
fox.speak()

# create an object that belongs to Cat class
cat = Cat("Billy",3, "blue")

# create an object that belongs to Dog class
dog = Dog("Black", 5, "Shnautzer")
#
# cat.speak()
# dog.speak()

pet = Pets("Mike", 19) # cream o instanta a clasei Pet
pet.speak()
cat.speak()

class Person:
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

# cream o noua persoana (o instanta a clasei Person)
# putem accesa atributele clasei si sa le folosim la persoana pe care vrem sa o cream,

user = Person(25, 65, 150, "Akihkio", "Takayama")
print(user.height) # ne arata

print(type("hello"))

# avem functia

def greetings():
    print("Hello there human!")

print(type(greetings))##### de verificat

s = 2
n = "string"
print(s + n)


## methods
mystring = "yellow there"
print(mystring.upper()) #--. metoda care actioneaza asupra unui obiect
#print(s.upper())

# create classes

# cream o clasa Dog si scriem atributele clasei Dog
# definim o clasa Dog folosing cuvantul cheie class

class Dog:
    ####
    def __init__(self, name, age):
        # trebuie sa accesam numele undeva pt a fi accesar mai tarziu
        self.name = name
        self.age = age

    def bark(self):
        print("Ham ham!")

    def sad(self):
        print("I am sad")

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

d = Dog("Billy", 5)
print(type(d)) # returneaza <class '__main__.Dog'> este un obiect al clasei Dog
            # avem __ pt a ne arata in ce modul clasa a fost definita.
            # by default modulul pe care l-ai rulat este modulul prinicpal
            # de unde si denumirea __main__

d.bark() # utilizam o metoda pe o instanta a clasei dog

# aplicam metoda sad pe obiectul d
d.sad()
print(d.get_name())

d2 = Dog("Oreo", 12)
print(d2.get_name())
d2.set_age(2)
d.set_age(2)

# mai sus am facut un blueprint pentru clasa dog

# avem un sistem de gestiune universiar

# CURS 8

# Encapsulare = este o metoda prin care putem sa atribuim un anumit nivel de acces unor variabile sau metode
# niveluri de acces:
# - public - sunt vizibile de oriunde din program
# - protected (_) -> se pot folosi doar in aceeasi clasa sau si in clasa
# - private (__)-> se pot folosi doar in interiorul clasei curente

# restrictionarea accesului
# information hiding - ascundem anumite aspecte despre codul nostru pentru cei din exterior
# prezinta in schimb o interfata pe care ceilalti o pot folosi, fara a stii ce face codul intern

## Toti membrii intr-o clasa Python sunt public by default
## Orice membru poate fi accesat de oriunde din program

##### Private members #####
# __(dubllu underscore) este prefixul pentru variabile private
# nu trebuie foloiste in afara clasei.

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self.__wheel = wheel  # private class atribute
        self.__speed = speed  # private class atribute
        self.__color = color  # private class atribute

    def __print_me(self):
        print("I am a private method")


renault = Car("right", 180, "green")
# print(renault.__color)
# Orice incercare de a folosi atributul in afara clasei va rezulta intr-o eroare --> AttributeError
# print(renault.__print())

# python face o modificare a variabilelor private.
# Fiecare membru cu __ o sa fie schimbat in _object.class_variable --> poate fi accesat in afara clasei
# DAR NU TREBUIE SA FACEM ASTA
# print(dir(renault))

# Cum se acceseaza - REFRAIN FROM DOING SO
print(renault._Car__speed)
renault._Car__speed = 500
print(renault._Car__speed)

### Python nu are  un mecanism care sa restrictioneze accessul pe metode sau variabile
# Pur si simplu exista conventia de a folosi _ si __ care sa simuleze comportamentul de protected si private
# Ramane la latitudinea dezvoltatorului sa inteleaga acest lucru.

######## Protected members ##########
# protected members - sunt accesibili in interiorul clasei cat si in subclase. Nu pot fi accesati din oriuce alta parte
# instance variable protected --> _var_name (single underscore). Folosind underscore, previne sa fie accesat, mai putin daca
#e accesat dintr-o subclasa

# Transformam clasa Car

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self._wheel = wheel  # protected class atribute
        self._speed = speed  # protected class atribute
        self._color = color  # protected class atribute

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_wheel(self):
        return self._wheel

    # set a new color
    def set_color(self, value):
        self._color = value

    def set_speed(self, value):
        self._speed = value

# daca scrie in felul asta, nu previne variabilele instantei sa acceseze sau sa modifice instanta


peugeot = Car("right", 240, "white")  # nu ne da eroare cand scriem valorile
# print("peugeot color: ", peugeot.color)
print("peugeot color:", peugeot._color)

# Daca vrem sa modificam culoarea
peugeot.color = "black" # nu schimba culoarea
peugeot._color = "black"
print(peugeot._color)

# Daca o variabila jeste scrisa cu underscore(este protected), programatorul se va ABTINE sa o modifice in afara clasei

# setam culoarea apeland metoda de setare a culorii
peugeot.set_color("Black")
print(peugeot.get_color())

# Avem un exemplu cu clasa Car cu toate atributele publice. Putem accesa si modifica valorile oricand

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self.wheel = wheel
        self.speed = speed
        self.color = color

#Accesam atributele publice


kia = Car("right", 200, "white")  # cream o instanta/obiect al clasei Car folosindu-ne de atribute
ford = Car("left", 180, "blue")  # cream o instanta/obiect al clasei Car folosindu-ne de atribute
mitsubishi = Car("right", 240, "cameleon")  # cream o instanta/obiect al clasei Car folosindu-ne de atribute

print(f"Viteza maxima a masinii Mitusbishi este {mitsubishi.speed}")

# putem modifica valoarea vitezei masinii Mitsubishi
mitsubishi.speed = 220

print(f"Viteza maxima a masinii Mitsubishi este acum de {mitsubishi.speed}")

# number = int(input("Enter a number: "))
# print(number)
# value = 15/0

# try ...catch
try:  # we put our code here
    number = int(input("Enter a number: "))
    print(number)
    print(number / 0)

except ValueError as err_input:  # what happens if it breaks
    print("Invalid input")

except ZeroDivisionError:
    print("Division to 0 is impossible")
# try:  # we put our code here
#     value = 15 / 0
# except ZeroDivisionError:
#     print("Division to 0 is impossible")

from abc import ABC, abstractmethod

###### abstrtact classes and abstract methods #######

# abstract method = a method that must be implemented in a subclass
# Clasele abstracte sunt create din meta Clasa ABC, care apartine modulului abc(Abstract base class)

## Abstract method in python
# ca sa definim o metoda abstracta in Python, aceasta trebuie decorata cu decoratorul @abstractmethod.
# Trebuie importat din modulul abc, abstractmethod

class MyClass(ABC):

    @abstractmethod
    def mymethod(self):
        pass

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    # def perimeter(self):
    #     return self.side * 4



square = Square(2)
import random
# game with dictionary
# quizz with european capitals

# de ce avem nevoie?:
# - dictionar cu tari si  capitale
# random choice- ca sa selecteze o tara din dictionar
# input de la user
# variabia in care stocam inputul de la user
# functie care face verificarea
# counter care ii spune cate raspunsuri corecte are din nr total

def get_europe_capitals():
    europe_capitals = {
        "Romania": "Bucharest",
        "Spain": "Madrid",
        "Turkey": "Ankara",
        "Russia": "Moscow",
        "Bulgary": "Sofia",
        "Hungary": "Budaphest",
        "Germany": "Berlin",
        "Belgium": "Brixelles"
    }
    return europe_capitals

def main():
    europeCapitals = get_europe_capitals()
    print("Welcome! Input the correct capital for each country!")
    correct_answers = 0

    while len(europeCapitals) != 0:
        # get a random country
        country = random.choice(tuple(europeCapitals.keys()))
        capital = europeCapitals[country]

        # remove from dictionary the selected country
        del europeCapitals[country]

        # get answer from user
        answer = input(f"What is the capital of {country}?: ")

        # verificam raspunsul utilizatorului
        if answer == capital:
            correct_answers += 1
            if len(europeCapitals) != 1:
                print("That's correct! Good luck with the next one!")
            else:
                print("That's correct")
        else:
            print("Incorrect")
            continue
    print(f"GAME OVER!! {correct_answers} correct answers from 8")

main()

###### Polymorphism ####

### cream clase cu limbi straine

class Japanese:
    # avem o functie care saluta in japoneza
    def say_hello(self):
        print("Konnichi wa")


class Chinese:
    def say_hello(self):
        print("Ni hao")


class French:
    def say_hello(self):
        print("Bonjour")


def greetings(language):
   language.say_hello()


# cream o instanta a clasei Japanese
Takumi = Japanese()

# cream o instanta a clasei Chinese
Lee = Chinese()

# cream o instanta a clasei French
Paul = French()

greetings(Takumi)
greetings(Lee)
greetings(Paul)

## conventii
# verificam daca o variabila este None sau nu, cu is None, is not None. nu folosim ==
#
# a = None
# if a is None:
#     print("something")
#
# if a is not None:
#     print("something")
#
# ### cum se face unpacking ###
# # vrem sa facem unpack la o colectie si sa asignam fiecare valoare unei variabile
#
# tup = (10, 12, 1, 5, 0)
# a, b, c, d, e = tup
# print(a, b, c, d, e)
#
# my_dict = {"name": "Madalina", "age": 29, "language": "romanian"}
# val_a, val_b, val_c = my_dict.values()
# print(f"val_a este {val_a}, val_b este {val_b}, val_c este {val_c}")
# s, n, x = my_dict
# print(s,n,x)
#
# # vrem sa obtinem si cheile si valorile. obtinem tuple
# g, f, j = my_dict.items()
# print(g, f, j)
#
# #### multiple assignement --> switch ####
# a, b = 10, 100
# a, b = b, a
# print(a, b)

##### ternar condition (inline) ####

# if 2*5 > 1*3:
#     d = 10
# else:
#     d = 0

# folosim conditie ternara
# d = 10 if 2*5 > 1*3 else 0
# asigneaza lui d valorea 10
# conditie
# daca nu, asigneaza-i 0

#### zip function - combina colectii de date impreuna ca sa putem itera prin toate odata

fruits = ["mango", "strawberry", "apple", "watermelon"]
kilos = [1, 3, 1, 10]
color = ["orange", "red", "yellow", "green"]

# print(list(zip(fruits, kilos, color)))

# for fruits, kilos, color in zip(fruits, kilos, color):
#     if color == "green":
#         print(fruits)
#     print(kilos)

####### *args, **kwargs #####
# *args = positional arguments -> este un argument in care pozitia conteaza
# **kwargs = keywords arguments -> putem apela o functie cu ce poz vrem, atata timp cat le trecem

# positional
#
# def my_function(ar1, ar2, ar3):
#     print(ar1, ar2, ar3)
#
# def my_function1(ar1=None, ar2=None, ar3=None):
#     print(ar1, ar2, ar3)

#### dac ca argumente unei functii liste si dictionare
# args = [2, 5, 7]
# kwargs = {"ar1": 2, "ar2": 3, "ar3": 4}
#
# my_function(*args)
#
# # cu dictionare
# my_function1(**kwargs)

###### sort by key #########

# l = [[1, 2], [10, 1], [13, 2], [0, 6]]

# folosim functia sort() care o sa sorteze dupa primul elemnt din fiecare nested list
# l.sort()
# print(l)


# l.sort(reverse=True)
# print(l)

# vrem sa sortam dupa al doilea element

# l.sort(key=lambda x: x[1]) # x este parametrul pt functie si returnam x[1] adica al doilea element din fiecare nested list
# print(l)

# vrem sa ssortam dupa suma elementelor din fiecare nested list
# l.sort(key=lambda x: x[0] + x[1])
# print(l)
#
# def sort_func(x):
#     return x[0] + x[1]
#
# l.sort(key=sort_func())
# print(l)

# create a function that takes a variable number of arguments

# def multiply(x, y):
#     return x * y

# print(multiply(2, 5))

# multiply(2, 5, 10, 12) - too many arguments, error returned

def multiply(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print(multiply(2, 5, 12, 30, 100, 1, 3, 15))

### we want a function that saves information


def save_info(**info_user): ## folosim keyword arguments
    for key, value in info_user.items():
        print(key, value)


save_info(name="Luther", age=50, e_mail="luther.king@gmail.com")

# static attributes
# self was referint to the instance
# class attributes are attributes specific to the class

class Person:
    number_of_people = 0 # this is a class attribute
                        # it's not a regular attribute, it's not defined inside a method
                        # it doesn't have any access to an instance of a class
                        # is defined for the entire class
                        # it will not change for every person
                        # the value will be the same

    def __init__(self, name):
        self.name = name

person1 = Person("Lina")
person2 = Person("Tom")

Person.number_of_people = 8 # scriem Person. pt ca este specific clasei, nu instantei
print(person2.number_of_people)

Person.number_of_people = 3
print(person1.number_of_people)

print(Person.number_of_people)


####
x = 5.5
print(round(x))

class Math:
    @staticmethod # inseamna ca nu se schimba. metodele statice tin mai mult de organizare.
    def add10(num):
        return num + 10

print(Math.add10(20))