---
Utworzono: 2024-11-23T22:24:00
Zmodyfikowano: 2024-11-24T15:05:00
Źródło: udemy
tags:
---

GitHub [Repo](https://github.com/pythonforeveryonetraining/objectorientedpirates/tree/main)


# Sekcja 1. 
## 1. [Course Introduction](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189306#overview)
# Sekcja 2
## 2 [Introduction](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189382#overview)
 
 **Pirates and Object Oriented Programming**
 
 ransom - okup
 loot - okup
 days go by - mijają dni
 week go by - mija tydzień

**Task: to build loot sharing system**

## 3. [First version]()

disclaimer - ostrzeżenie
payroll - list płac
pirat rank - stopień pirata

Project name: **Pirat Payroll**

## 4. [Tuples](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189392#overview)

1. Dodaliśmy nowego pirata do listy, ale nie dodaliśmy go do żadnego z if-ów
2.  dodajemy pirata do if-ów, ale to wymaga zmiany kodu w 3 miejscach. Jeśli cos wymaga zmiany w kilku miejscach to mamy do czynienia z ```fragile code```
3.  Usuwamy pirata Moragana z listy, znowu musimy zmienić kod w 3 miejscach. Program działa ale kod jest ```fragile```. - czyli ==kruche oprogramowaie== lub ==kruchy kod==.
4. Problem: Pirat  jego rank nie są połączone w systemie. Każdy pirat, powinien być kombinacją imienia i jego stopnia (rank)

## 5. [Pirate union](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189394#overview)

1. Dodajemy 3 piratów do listy
2. zaokrąglenie wyświetlanych liczb do dwóch miejsc po przecinku - f string formatting
3.  Problem: niewiadomo jak obliczany jest stopień pirata, czyli wielkość proporcji przy podziale łupu.
4.  There are rules for roles and ranks on a ship!
5. Musimy dodać role title do krotki i zaktualizować stopień pirata
6. Aktualizacja -> 2 zadania
	1. dodać nazwę funkcji (role title) do krotki dla każdego pirata
	2. I zaktualizować stopień pirata (rank) według otrzymanej listy
7. Usprawnienie:
	1. ==The tuple organizes the data, but does not give semantic meaning to its element==
	2. Patrząc na krotkę musimy się domyślać (to guess) co znaczy kolejny element w krotce
	3. Gdy przypadkowo pominiemy jakiś element krotki, to pojawi się błąd w rozpakowaniu krotki, ale nie będzie wiadomo o co chodzi dokładnie i gdzie jest błąd (w definicji którego pirata)
	4. Potrzebujemy struktury danych, która dokładnie opisze znaczenie poszczególnych elementów, a także wymusi ich obecność -> ```Klasa```
8. Zamieniamy ```non descriptive tuple``` na ```Class```.

a mutiny - bunt
mutinies - bunty
to oversee - nadzorować
a crook - oszust
to avert - zapobiec
# Sekcja 3: Classes and objects
## 6. [Classes and objects](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189402#overview)

1. We will replace the tuples with classes and objects
2. Objects group data that belongs together

![[udemy-Loek-OOPirates-6-1.png]]
![[udemy-Loek-OOPirates-6-2.png]]

3. Each element of ```pirates``` list is a class instance.
4. Dodajemy nowego pirata: Lady Joice - Gunner -6
5. Z wykorzystaniem klas, teraz jest jasne co oznacza wartość którą wpisujemy podczas tworzenia obiektu : imię, rolę i stopień (rank)
6. Nie jest możliwe utworzenie obiektu z pominięciem jakiegokolwiek z trzech koniecznych wartości podawanych do konstruktora

## 7. [UML](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189404#overview)
1. We can share design of our system with our colleges.
2. UML - Unified Modeling Language - visual language do document and share software design: 
	1. class diagrams
	2. Initialize has name of the Class, not dunder init ( __init__)

| ![[udemy-Loek-OOPirates-7-1.png]] | ![[udemy-Loek-OOPirates-7-2.png]] |
| --------------------------------- | --------------------------------- |
|                                   |                                   |

# Sekcja 4: Inheritance

## 8. [Inheritance](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189412#overview)

1.  Pirat union decided to rename some pirate role titles
	1. Gunner -> Cannon Operator
	2. Mate -> Officer
2. Mamy zmienić nazwy w kodzie
3. Zmienlśsmy 2 rzeczy, ale w 4 liniach kodu -> nasz problem to DUPLICATE CODE

| ![[udemy-Loek-OOPirates-8-1.png]] | ![[udemy-Loek-OOPirates-8-2.png]] |
| --------------------------------- | --------------------------------- |
![[udemy-Loek-OOPirates-8-3.png]]

4. Możemy stworzyć 4 klasy w których na sztywno będą wpisane rola i stopień pirata. Jednak wszystkie te klasy będą miały taki sam kod dotyczący konstruktora, zatem będzie to DUPLICATE CODE!!!! I to jet miejsce na dziedziczenie, gdzie część kodu jest ogólna (taka sama), a część kodu jest szczególna, specyficzna dla poszczególnych podklas.

| ![[udemy-Loek-OOPirates-8-5.png]]    | ![[udemy-Loek-OOPirates-8-4.png]]                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Dziedziczenie: otwarty grot strzałki | Klasa dziedzicząca nie ma swojego konstruktor. Konstruktor jest dziedziczony z klasy nadrzędnej. |

5. Tworzymy podklasy dla każdego stanowiska pirata

![[udemy-Loek-OOPirates-8-6.png]]

6. The code is growing, so my must start thinking about splitting it up

## 9. [Refactoring](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189414#overview)

1. Refactoring is a big part of software engineering
2. Change is the only constant in our work 
3. Program can be divided into 3 parts
   
   ![[udemy-Loek-OOPirates-9-1.png]]
   
4. The easiest part to start with refactoring is to extract classes.
5. We create a new ```module``` that contains the pirate classes
6. We create ```the link``` from the main module to the pirates module, and it is done by ```import``` statement
7. UWAGA: The ```Pirate``` class does not have to be imported, as it is not instantiated in the main module. (!!!!)
   ![[udemy-Loek-OOPirates-9-2.png]]
   
8. It shows which modules imports other modules. 
9. pirates.py module is responsible for Pirate classes
10. We can extract more: data creation part -> to new module called data.py
11. instead of copying the list, we will create a new class
12. Now it is really understand what main.py does:
    ![[udemy-Loek-OOPirates-9-3.png]]
    
    
13.  Let's update the dependency diagram:
    
| ![[udemy-Loek-OOPirates-9-4.png]] | ![[udemy-Loek-OOPirates-9-5.png]] |
| --------------------------------- | --------------------------------- |
|                                   |                                   |

14. From now on, the changes to the system will be focused on specific modules instead of requiring changes to the whole system.
15. Modules and classes should have a single responsibility -> SINGLE RESPONSIBILITY PRINCIPLE
    
    ![[udemy-Loek-OOPirates-9-6.png]]
    
16.  Class dependency.
	 ![[udemy-Loek-OOPirates-9-7.png]]   
 
# Sekcja 5: Polymorphism

## 10. [Extra Officer and Cannon Operator](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189418#overview)

1. Add an Extra Officer and Cannon Operator to the crew
2. Problem: reczne aktualizowanie listy załogi na każdą misję
3. Cel: Zautomatyzowanie wczytywania załogi np z pliku

## 11. [Importing JSON](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189424#overview)

1. Zautomatyzowanie wczytywania listy z członkami załogi z pliku JSON
2. JSON - JavaScript Object Notation
3. Dodajemy nową klasę DataLoader
4. Polimorfizm - w nowej klasie tworzymy funkcje load_pirates() - taka sama nazwa juz istnieje w klasie poprzedniej DataLoader()
5. Zrobiłem plika data.json z danymi
6. zroblismy nową klasę JSONDataLoader
7. tworzymy obiekt loader, raz DataLoader() a innym razem JSONDataLoader() komentując instancje niewykorzystywanej (drugiej) klasy - i wszystko dziala. bo to jest POLIMORFIZM - obie klasy mają funkcję o tej samej nazwie. Ale obie funkcje wewnątrz mają różne (inne) implementacje, czyli działają inaczej i robią inne rzeczy np. tworzenie danych w funkcji vs. wczytanie ich z pliku data.json.
   
   ![[udemy-Loek-OOPirates-11-1.png]]
   
8.  Polymorphism is the key to adhering to the ```open-close principle``` ->
	1. Open for extension
	2. Closed for modification
	   
	  
   ahering  - przyleganie
   
   ![[udemy-Loek-OOPirates-11-2.png]]![[udemy-Loek-OOPirates-11-3.png]]
  ![[udemy-Loek-OOPirates-11-4.png]]
![[udemy-Loek-OOPirates-11-5.png]]

9. Nie skasujemy jeszcze starej wersji klasy ```DataLoader()``` bo ona nam się jeszcze przyda w przyszłości.
10. Cały czas jest problem:
    
    ![[udemy-Loek-OOPirates-11-6.png]]
    
11. Problem ten zobaczymy za chwile, oraz jego rozwiązanie

## 12. [Add Cook and Deck Scrubber](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189426#overview)

1. 

