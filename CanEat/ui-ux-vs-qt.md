---
Utworzono: 2024-11-23
Zmodyfikowano: 2024-11-23
tags:
---

Rozróżnienie między pracą projektanta UI/UX a tworzeniem projektów w Qt opiera się na podziale obowiązków i narzędzi w procesie tworzenia aplikacji. Zacznijmy od wyjaśnienia, czym zajmuje się projektant UI/UX i jak różnią się ich zadania od pracy w Qt.

---

## **Kim jest projektant UI/UX?**

### **Projektant UI (User Interface – interfejsu użytkownika):**

- **Czym się zajmuje?** Projektant UI odpowiada za **wygląd interfejsu użytkownika**. Tworzy wizualną stronę aplikacji, dbając o to, aby była estetyczna, spójna i zgodna z brandingiem firmy.
- **Przykładowe zadania:**
    - Tworzenie przycisków, ikon, czcionek, kolorystyki i layoutów.
    - Projektowanie ekranów aplikacji tak, aby były intuicyjne i atrakcyjne wizualnie.
    - Zapewnienie responsywności (dostosowanie interfejsu do różnych urządzeń i ekranów).
- **Przykład UI:**
    - Atrakcyjne menu aplikacji na telefonie.
    - Interfejs Spotify, gdzie każdy element (przyciski, lista odtwarzania, kontrolki odtwarzania) jest starannie zaprojektowany.

---

### **Projektant UX (User Experience – doświadczenia użytkownika):**

- **Czym się zajmuje?** Projektant UX koncentruje się na tym, aby **użytkownik mógł łatwo i przyjemnie korzystać z aplikacji**. Analizuje potrzeby użytkownika, projektuje procesy nawigacyjne i testuje ich skuteczność.
- **Przykładowe zadania:**
    - Opracowanie ścieżek użytkownika (np. jak użytkownik kupi produkt w aplikacji e-commerce).
    - Testowanie prototypów i poprawianie błędów w doświadczeniu użytkownika.
    - Tworzenie makiet (wireframes) i prototypów dla projektantów UI.
- **Przykład UX:**
    - Czy aplikacja jest łatwa w obsłudze, np. Amazon – gdzie kupno produktu wymaga tylko kilku kliknięć.
    - Wyszukiwarka Google, która natychmiast pokazuje wyniki w intuicyjnym układzie.

---

### **Czym jest projekt UI/UX?**

- **Projekt UI/UX:** Dokumentacja, wizualizacje i prototypy, które pokazują **jak aplikacja powinna wyglądać i działać**, zanim ktokolwiek zacznie pisać kod. Narzędzia takie jak Figma służą do przygotowywania takich projektów.
- **Zawartość projektu UI/UX:**
    - Makiety niskiej szczegółowości (wireframes) pokazujące układ ekranu.
    - Prototypy z interaktywnymi elementami (np. przyciskami).
    - Dokumentacja określająca kolory, czcionki, style.

---

## **Czym różni się projekt UI/UX od projektu w Qt?**

|**Cecha**|**Projekt UI/UX**|**Projekt w Qt**|
|---|---|---|
|**Cel**|Wizualizacja i optymalizacja doświadczenia|Stworzenie działającej aplikacji|
|**Etap w procesie**|Etap projektowania (przed kodowaniem)|Etap wdrożenia i programowania|
|**Narzędzia**|Figma, Adobe XD, Sketch|Qt Creator, C++, QML|
|**Udział programowania**|Brak – skupia się na wyglądzie i użyteczności|Wymaga kodowania logiki aplikacji i funkcji|
|**Efekt końcowy**|Prototyp, wizualizacja|Działająca aplikacja|

---

## **Przykłady projektów UI/UX:**

1. **Strona sklepu internetowego:**
    
    - **UI:** Projekt wyglądu strony głównej z sekcją produktów, menu, kolorystyką i czcionkami.
    - **UX:** Zaplanowanie prostego procesu zakupu, od wyboru produktu do płatności.
2. **Aplikacja mobilna fitness:**
    
    - **UI:** Ekran z planem treningowym, statystykami i animacjami osiągnięć.
    - **UX:** Ułatwienie ustawienia treningu w kilku krokach.
3. **System bankowości internetowej:**
    
    - **UI:** Przyjazny i minimalistyczny układ ekranu, np. pokazanie salda i ostatnich transakcji.
    - **UX:** Umożliwienie przelewu w 3 prostych krokach z opcją zapisania odbiorcy.

---

## **Które narzędzie do czego służy?**

- **Figma (UI/UX):**
    
    - Służy projektantom do stworzenia wizji aplikacji.
    - Daje możliwość testowania wyglądu i interakcji **bez pisania kodu.**
- **Qt (projektowanie i wdrażanie):**
    
    - Pozwala programistom zaimplementować zaprojektowany interfejs i dodać do niego logikę oraz funkcje.

---

## **Podsumowanie różnic:**

1. **UI/UX to etap kreatywny i badawczy.** Jego celem jest zrozumienie użytkownika, zaplanowanie interakcji i zaprojektowanie estetycznego interfejsu. To wizualizacja, która nie działa jeszcze jak gotowa aplikacja.
2. **Qt to etap implementacji.** Wykorzystuje projekt UI/UX, aby stworzyć działającą aplikację. Odpowiada za połączenie interfejsu z funkcjami i logiką biznesową.