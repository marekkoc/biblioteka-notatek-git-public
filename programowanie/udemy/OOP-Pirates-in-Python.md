---
Utworzono: 2024-11-23T22:24:00
Zmodyfikowano: 2024-11-25T08:34:00
Źródło: udemy
tags:
---

GitHub [Repo](https://github.com/pythonforeveryonetraining/objectorientedpirates/tree/main)


# Sekcja 1. Course Introduction 
## 1. [Course Introduction](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189306#overview)
# Sekcja 2 Introduction
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

1. Dodajemy dwóch członków załogi: Cook and Deck Scrubber
	   ![[udemy-Loek-OOPirates-12-1.png]]
2. Dodajemy piratów do danych, czyli do pliku JSON
3. Dodajemy ich do switcha w funkcji JSONDataLoader 
4. Dodajemy importy nowo zdefiniowanych subclass do modulu data.py
5. Aktualizujemy wartość zdobytego łupu
6. ==Single responsibility== -> code needs to be changed in as few places as possible (!!!) 
7. Still, there is a problem with OPEN-CLOSE PRINCIPLE violation (!!!) in JSONDalaLoader method. There is a switch, that based on PIRATE TITLE to create instances of classes. We don't know the exact number of pirate titles. Pirate titles can be created and added in the future too. In such a case a new subclasses need to be created and the switch need to be changed. -> in other words: code needs to be changed in a few places. This is an  ```LIMITATION OF INHERITANCE```. The code is not flexible enough, and it is time to introduce a new concept: ==FAVOR COMPOSITION OVER INHERITANCE==

	![[udemy-Loek-OOPirates-12-2.png]]
# Sekcja 6: Composition

## 13. [Composition over Inheritance](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189432#overview)

1. W sekcji 3 stworzyliśmy dodatkowe klasy za pomocą dziedziczenia, aby uniknąć powtarzania kodu (duplicate code). Przenieśliśmy wtedy część kodu szczególną dla poszczególnych klas (funkcja, oraz stopień) do klas podrzędnych a konstruktor i imię pozostały w klasie nadrzędnej. W ten sposób zmniejszyliśmy ilość kodu pisanego podczas tworzenia nowych obiektów, do konstruktora danej klasy podawaliśmy tylko imię pirata, a stopień i funkcja była automatycznie wywoływana w danej klasie.
   ![[udemy-Loek-OOPirates-13-1.png]]
   Jednak liczba klas zaczęła szybko wzrastać wraz z pojawieniem się nowych piratów w załodze, a także ze wzrostem liczby funkcji nowych piratów trzeba było pisać nowe klasy dla nowych zawodów oraz aktualizować funkcję JSONDataLoader w zależności od zawodu. 
2. Ale od tamtego czasu nastąpiła zasadnicza zmiana!!! Listę piratów wczytujemy z pliku JSON, tam jest wszystko podane, imię, funkcja i stopień pirata, zatem już nie ma potrzeby powtarzania tego wszystkiego w osobnych funkcjach określonych dla każdego zawodu osobno. To usuwa problem wpisywania imienia, funkcji i stopnia każdego pirata ręcznie    ![[udemy-Loek-OOPirates-13-2.png]]
3. Jednak cały czas musimy zmieniać inne części kodu, takie jak JSONDataLoader
   ![[udemy-Loek-OOPirates-13-3.png]]
4. Teraz chcemy to zmienić. Nadal chcemy aby funkcja pirata była powiązana z jego stopniem (przy podziale łupu) ale nie chcemy już mieć tylu podklas związanych z każdym zawodem osobno. Zamiast podklasy, utworzymy nową klasę ```Role``` związaną z funkcją i stopniem i połączoną z klasą nadrzędną - Pirat. 
5. Tą nowo utworzoną klasę będziemy przekazywać jako argument podczas tworzenia obiektu Pirat! Obiekt ```Role``` będzie zachowywany jako atrybut klasy ```Pirat```. Dzięki temu możemy ```skasować wszystkie klasy dziedziczące!!!```
6. Teraz przechodzimy do funkcji JSONDataLodader(). Usuwamy całą dużą część związaną ze ```switchem``` i ze sprawdzeniem roli pirata. Zastępujemy to z użyciem parametru ```role```. Wystarczy jedna linia kodu (!!!)
7. Role class is instantiated and pass to each Pirate object. Zatem każdy pirat ma Role a Role ma title and rank.
8. Dlatego musimy zmienić funkcję main.py w 3 miejscach
9. To sie nazywa ==Kompozycja - Composition==
10. Association line is drown between two classes. When the Pirate object is deleted, the Role object is deleted too. As the Pirate object is the ==owner== of the Role object and this is indicated with a ==black diamond==.
    ![[udemy-Loek-OOPirates-13-4.png]]
11. A Pirate object is ```composed of``` a name and role. It is known as a ==has relationship==. ==A Pirate has a role==
12. Aby zapobiec duplicate code zaczęliśmy od dziedziczenie, wtedy była to najlepsza decyzja. Ale liczba klas dziedziczących szybko rosła i powodowała zmiany w kodzie gdy pojawiał się pirat z nową rolą.
13. Ważną rolą SOFTWARE ENGINEERING jest to aby wiedzieć kiedy należy zmienić budowę systemu jako że kompozycja teraz jest już lepszym rozwiązaniem.
    ![[udemy-Loek-OOPirates-13-5.png]]
14. Dzięki tej zmianie usunęliśmy sporo kodu który trzeba cały czas modyfikować gdy pojawia się nowa rola pirata. Dzięki temu system stał się znacznie łatwiejszy w obsłudze i elastyczny.
    ![[udemy-Loek-OOPirates-13-6.png]]
15.  Dodajemy nowego członka załogi: Doc  Bone; Doctor; 5 do pliku json.dat, aktualizujemy łup do 1610 dukatów.
16. Oto zaktualizowany diagram klas UML
    ![[udemy-Loek-OOPirates-13-7.png]]
17. Usunięcie klas dziedziczących spowodowało wzrost przejrzystości diagramu i zwiększyło "lekkość" projektu.
18. Co zrobić ze starą klasą DataLoader() -> o tym w następnej części.

## 14 [Test with Test DataLoader](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189436#overview)

1. DataLoader() - faliste linie wskazuję na problemy w kodzie.
		
		wiggly lines - linie faliste
2.  Zmieniamy JSONDataLoader na DataLoader() w main.py
3. Mamy nowy JSONDataLoader(), czy powinniśmy skasować starty DataLoader()?
4. NIE! Zamienimy cel DataLoader aby teraz był ```Test Data Loader``` Dlaczego to nam się przyda??? Poniewaz:
	1. Gdy baza danych lub sieć internetowa będzie miała awarie to nie będziemy mogli wczytać/pobrać pliku z danymi ```data.json``` A to jest bardzo frustrujące, gdy nie możemy rozwijać kodu ze względu na brak danych. Jeśli będziemy mieć dane testowe wpisane na sztywno (hard coded) zawsze będziemy mogli testować i rozwijać nasz program.
	2. Dane wpisane na sztywno (hard coded) są bardzo dobre do testowania, ponieważ ZAWSZE POWINNY DAĆ TEN SAM ZNANY/PRZEWIDZIANY WYNIK. Dobrze jest zastosować w danych testowych ROZPOZNAWALNE NAZWY I ŁATWE DO OBLICZEŃ WARTOŚCI 
	   ![[udemy-Loek-OOPirates-14-1.png]]
5.  Zatem teraz przerobimy stertą funkcję DataLoader() do nowych celów.
6. DataLoader() -> TestDataLoader() w kilu miejscach
7. ducates = 100
8. Sprawdzamy ponownie czy JSONDataLoader() nadal działa? -> TAK!
9. Ponownie przełączamy się do TestDataLoader() i sprawdzamy czy działa? -> Tak!
10. To jest super! Przełączanie się pomiędzy danymi testowymi i danym JSON jest bardzo łatwe ponieważ wystarczy utworzyć obiekt innej klasy!!!!
    ![[udemy-Loek-OOPirates-14-2.png]]
11.  Obie klasy z danymi zawierają funkcję o tej samej nazwie (współdzielą nazwę funkcji)
    ![[udemy-Loek-OOPirates-14-3.png]] co jest kluczem do ==POLIMORFIZMU==.

12. Nazwy w danych testowych, są fejkowe, znane i łatwe do zapamiętania. Zawsze należy wybrać takie nazwy np bohaterów z filmów, z bajek gdy prezentujemy działanie naszego kodu kolegom z grupy. To automatycznie wskaże im, że mają przed sobą projekt który jest w toku, który nadal jest rozwijany, dzięki czemu powstrzymają się nad krytyką pewnych części kodu/ projektu które wymagają jeszcze dopracowania.
13. Zobaczmy teraz diagram zależności w aktualnym stanie naszego kodu:
    ![[udemy-Loek-OOPirates-14-4.png]]
14. A jak wygląda diagram UML?
	![[udemy-Loek-OOPirates-14-5.png]]
15. Aby uprościć diagram  zamieniamy obie klasy w jedną klasę DataLoader() (tylko na diagramie), kod pozostaje ten sam. Robimy tak bo obie klasy mają wspólny interfejs (funkcję o tej samej nazwie). To jest tylko po to aby uprościć diagram UML.
    ![[udemy-Loek-OOPirates-14-6.png]]
    

# Sekcja 7. Payroll
## 15. [Payroll](https://www.udemy.com/course/object-oriented-programming-adventure-in-python/learn/lecture/40189442#overview)
1. 