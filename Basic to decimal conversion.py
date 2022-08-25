#Basic to decimal conversion algorithm
print('Zamiana liczby z dowolnego systemu na system decymalny')


#funkcja "cyfra" sprawdza czy wporwadzona przez użytkownika wartość nie jest literą aby sprawdzić czy wartość nie pochodzi z sys. 16
def cyfra(n):
    if n==str(n):
        s=int(n,16) #w przypadku wystąpienia wartości z systemu 16 łatwo możemy ją zamienić na wart. w sys. decymalnym dzięki funkcji wbudowanej
        return s
    if n>=0 and n<10:
        return n        #zwróć n zrzutowane na typ liczbowy

def zamiana_kazdego_na_decymalny(liczba,system_liczby):
    liczba = str(liczba)
    potega=0
    nowa_wartosc=0 #przechowuje końcową wartość w systemie decymalnym

    k=len(liczba)
    for i in range(k-1,-1,-1):
        #wprowadzoną przez użytkownika liczbę uznajemy za wart. str w celu jej indeksowania (każda wartość str w pythonie uznawana jest za listę)
        #potęgi indeksów rosną liniowo od końca tym samym będziemy przechodzili przez naszą wartość od tyłu
        nowa_wartosc = nowa_wartosc + cyfra((liczba[i]))*system_liczby**potega
        #analogicznie poszczególne indeksy musimy przemnożyć przez system podniesiony do odpowiedniej potęgi
        potega+=1
    return nowa_wartosc

print('wartość 100011 (system 2) w systemie decymalnym:',zamiana_kazdego_na_decymalny(100011,2))
print('wartość 1001111 (system 2) w systemie decymalnym:',zamiana_kazdego_na_decymalny('1001111',2))
print('wartość 61 (system 8) w systemie decymalnym:',zamiana_kazdego_na_decymalny(61,8))
print('wartość 8D (system 16) w systemie decymalnym:',zamiana_kazdego_na_decymalny('8D',16))#jeżeli wprowadzona liczba została zapisana w sys. 16
#domyślnie musimy wprowadzić ją jako str nie int ponieważ jest to błąd składni
print('wartość 321 (system 4) w systemie decymalnym:',zamiana_kazdego_na_decymalny('321',4))

print('\nZadanie z wykorzystaniem niewbudowanej funkcji potęgowania')
#Zadanie

def potęgowanie(liczba,potęga):
    if potęga==0:
        return 1
    elif potęga==1:
        return liczba
    else:
        return liczba*potęgowanie(liczba,potęga-1)
#rekurencyjna funkcja potęgowania danej liczby (funkcja zwraca mnożenia danej cyfry aż do dojedzie do base case'a po czym je zlicza)
#przykład potęgowanie(4,4)=4*potęgowanie(4,3)=4*4*potęgowanie(4,2)=4*4*4*potęgowanie(4,1)=4*4*4*4=256


#reszta funkcji jest niezmienna poza zmiananmi niektórych nazw zmiennych
def cyrfa(n):
    if n==str(n):
        s=int(n,16)
        return s
    if n>=0 and n<10:
        return n

def dowolny_na_decymalny(dowolna_liczba,system_liczby):
    przetrzymywana=0
    potęga=0
    dowolna_liczba=str(dowolna_liczba)
    dl_licz=len(dowolna_liczba)

    for i in range(dl_licz-1,-1,-1):
        przetrzymywana=przetrzymywana+cyrfa(dowolna_liczba[i])*potęgowanie(system_liczby,potęga)
        potęga+=1
    return przetrzymywana

print('wartość 100011011 (system 2) w systemie decymalnym:',dowolny_na_decymalny(100011011,2))
print('wartość 1111 (system 2) w systemie decymalnym:',dowolny_na_decymalny(1111,2))
print('wartość 93 (system 8) w systemie decymalnym:',dowolny_na_decymalny(93,8))
print('wartość 8DAC (system 16) w systemie decymalnym:',dowolny_na_decymalny('8DAC',16))
print('wartość 321231 (system 4) w systemie decymalnym:',dowolny_na_decymalny(321231,4))

