---
Utworzono: 2024-10-03T16:20:00
Zmodyfikowano: 2024-10-03T20:46:00
tags:
  - Tworzenie-mojej-strony-www
---
Notatki z kursy HTML na podstawie strony: Mozilla MDM web docs: [Getting started with the web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web)

If you are a new to web development, you should start small. Let's make our simple website online. 

# [Potrzebne narzędzia](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Installing_basic_software)

Znakomita lista potrzebnych narzędzi, które będą potrzebne została zamieszczone tutaj: [What tools do I actually need?](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Installing_basic_software) Spis zawiera sugerowane przeglądarki internetowe, edytory tekstu, narzędzia graficzne.

# [Planowanie strony](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/What_will_your_website_look_like)

Zanim zaczniemy tworzyć stronę, powinniśmy zrobić jej plan. Przemyśleć to **jak ta strona ma wyglądać**: jakiego koloru ma być tło, jakie obrazki ma zawierać, jaką treść tam zamieścimy, jakie będą podstrony. To wszystko trzeba przemyśleć. 

Pytania które warto sobie zadać zanim zaczniemy tworzyć stronę:
1. Jak ta strona ma wyglądać?
2. Jakie informacje ma oferować?
3. Jakie ma być tło? Jaka ma być czcionka?
4. Co ta strona ma *robić*? 

#### Krok pierwszy: planowanie strony

Musimy się zastanowić nad tym *co ta strona ma robić*? Ponieważ zaczynamy pisać strony, zatem pamiętajmy aby na razie postawione zadanie było proste. Na pierwszy ogień zróbmy stronę, która ma tylko kilka elementów:
1. Nagłówek
2. Obrazek
3. Kilka paragrafów z tekstem.

Pytania na które musimy sobie odpowiedzieć?
1. **O czym jest ta strona?**
    Czy lubię psy? Nowy Jork? Czy Pac-mana?
2. **Jakie informacje dotyczące tematu strony chcę tam zamieścić?**
    Powinienem się nad tym zastanowić i napisać następujące rzeczy:
	1. tytuł
	2. kilka paragrafów z tekstem, który ma się tam pojawić
	3. zastanowić się nad obrazkami, które chcę tam zamieścić
3. **Jak strona ma wyglądać?** 
   Na to pytanie powinienem odpowiedzieć w kilku słowach na ogólnym poziomie opisu.
	   1. Jakiego koloru będzie tło?
	   2. Jaki rodzaj czcionki chcę zastosować: formalny, rysunkowy, tłusty, krzykliwy, subtelny? 
	  Zagadnienia te są bardzo ważne i noszą nazwę systemu projektowego, przewodnika projektowego czy *brand book*. Więcej można poczytać o tym tutaj: [Firefox Acorn Design System](https://acorn.firefox.com/latest)
	
#### Krok drugi: Szkic strony

Dobrze jest wykonać ręczny szkic strony. Jako, e to jest pierwszy szkic, symboliczny i poglądowy nie musi on być dobry ani kompletny. Ważne jest aby był, aby zawierał symboliczne przedstawienie wszystkich elementów strony. Ważne jest aby **szkicowanie strony weszło nam w nawyk.** 


![[moja-strona-www-szkic.jpeg]]

Profesjonalne strony również zazwyczaj są zaczynane do odręcznego szkicu. W dalszym etapie mogą być projektowane przez grafika komputerowego i projektanta UX, który odpowiada za wrażenia użytkowania i interakcji ze stroną www. 

#### Krok 3: Wybór zasobów

##### Text
Powinniśmy mieć już przygotowane (we wcześniejszym etapie) zarówno tytuł strony jak i tekst zamieszczony w paragrafach. 

##### Kolory strony
Do tego celu możemy zastosować odpowiednie narzędzie  [the Color Picker](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_colors/Color_picker_tool) i doświadczalnie wybrać kolor jaki nam się podoba.

##### Obrazy
Możemy wyszukać obraz z sieci stosując wyszukiwarkę [Google Images](https://www.google.com/imghp). Należy jednak pamiętać o zachowaniu praw autorskich. Należy znaleźć obrazy które są powszechnie dostępne. Oto instrukcja:
		
		Click on the Tools button, then on the resulting Usage rights option that appears below. You should choose the option Creative Commons licenses.

##### Czcionki
Czcionki podobnie jak obrazy mogą być chronione prawami licencyjnymi. Dostęp do wielu czcionek zapewni [Google Fonts](https://developers.google.com/fonts). Gdy wybierzemy czcionkę aby jej używać powinniśmy:
1. Dodać referencje w naszym kodzie aby ją pobrać ze strony Google
2. Pobrać czcionkę z serwera na dysk lokalny, a następnie użyć jej kopii na serwerze www.

Istnieją też *bezpieczne czcionki* ([safe web fonts](https://web.mit.edu/jmorzins/www/fonts.html)) takie jak Arial, Times New Roman czy Courier New. 

# [Zarządzanie plikami ](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files)

Strona www składa się z wielu typów plików:
1. plików zawierających treść strony
2. plików z kodem,
3. plików ze stylem,
4. plików zawierających media
5.  oraz innych typów.

Aby strona www działała poprawnie, wszystkie te pliki muszą ze sobą współpracować, a zatem muszą "się widzieć" na wzajem, czyli muszą mieć do siebie dostęp za pomocą odpowiednich ścieżek. Zatem strona www musi mieć odpowiednią strukturę, aby  zbudować cały działający mechanizm.

Gdy strona www jest w trakcie budowy, na lokalnym komputerze, powinna być przechowywana w jednym katalogu. Zawartość katalogu powinna mieć taką samą zawartość zatem i strukturę (powinna być kopią) strony, która zostanie umieszczona na serwerze. Zapewnia to sprawdzenie przed przesłaniem do serwera czy strona działa odpowiednio na maszynie lokalnej. 

### [Kwestia nazewnictwa ](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files#an_aside_on_casing_and_spacing) 

Jest to ważna kwestia jako że przy złym nazewnictwie może powodować sporo niepotrzebnych problemów. Zatem:
1. wszystkie nazwy piszemy małą literą
2. nie używamy polskich znaków
3. zamiast podkreślnika stosujemy myślnik 
4. nie używamy spacji  (Niektóre serwery zamieniają spację an znak "%20")


### [Struktura strony www](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files#what_structure_should_your_website_have)

Każda strona www zawiera plik **index.html**, do tego znajdują się tam katalogi ze zdjęciami, skryptami oraz z plikami odpowiadającymi za wygląd (styl) strony. 

1. index.html  - ten plik w zasadzie zawiera całą zawartość strony www. Jest on widziany jako pierwszy przez wszystkie osoby, które odwiedzają naszą stronę. 
2. images - katalog z obrazami
3. styles - katalog z plikami CSS aby określić wygląd wybranych elementów np tekst i kolor tła.
4. scripts - katalog ze skryptami. Zawiera skrypty Java Script w których jest zdefiniowana interaktywne zachowanie naszej strony, np. przyciski.

### [Ścieżki dostępu](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files#file_paths)

Aby zapewnić poprawne funkcjonowanie strony, wszystkie katalogi i pliki muszą się "widzieć" nawzajem. W tym celu musimy zdefiniować zestaw odpowiednich ścieżek dostępu aby każdy plik "wiedział" gdzie znajduje się inny plik. 

Napiszmy teraz pierwszy kod, który między innymi wyświetla obrazek.

```html
<!doctype html>
​￼<html lang="en-US">
  ​￼<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>My test page</title>
  </head>
  ​￼<body>
    <img src="" alt="My test image" />
  </body>
</html>
```
