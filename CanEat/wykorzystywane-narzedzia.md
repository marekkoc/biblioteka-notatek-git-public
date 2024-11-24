---
Utworzono: 2024-11-23
Zmodyfikowano: 2024-11-23
tags:
---

Te trzy platformy pełnią różne role w cyklu tworzenia i wdrażania aplikacji mobilnych. Oto ich zadania, odpowiedzialności, zastosowania oraz sposób współdziałania:

---

### **1. React Native (reactnative.dev)**

**Zadania i odpowiedzialności:**

- **React Native** to framework umożliwiający tworzenie aplikacji mobilnych przy użyciu języka JavaScript i React.
- Odpowiada za **frontend aplikacji mobilnej**, czyli interfejs użytkownika oraz logikę, która jest realizowana na urządzeniu użytkownika.
- Umożliwia tworzenie aplikacji działających na systemach **iOS** i **Android** przy użyciu wspólnego kodu, co znacznie redukuje czas i koszty związane z rozwojem aplikacji.

**Zastosowania:**

- Tworzenie **interaktywnych interfejsów użytkownika**.
- Obsługa logiki związanej z zachowaniem aplikacji (np. nawigacja między ekranami, animacje, przetwarzanie danych wejściowych).
- Komunikacja z backendem (np. zapytania do API).

---

### **2. Firebase (firebase.google.com)**

**Zadania i odpowiedzialności:**

- **Firebase** to platforma Google zapewniająca różne narzędzia backendowe.
- Odpowiada za **backend aplikacji**, czyli funkcjonalności działające po stronie serwera.
- Zawiera wiele modułów, takich jak:
    - **Firestore/Realtime Database** - bazy danych do przechowywania danych aplikacji.
    - **Authentication** - zarządzanie logowaniem i rejestracją użytkowników.
    - **Hosting** - hosting dla statycznych i dynamicznych zasobów aplikacji.
    - **Cloud Functions** - uruchamianie funkcji backendowych w odpowiedzi na zdarzenia (serverless).
    - **Push Notifications** - obsługa powiadomień push.

**Zastosowania:**

- Przechowywanie danych użytkowników w czasie rzeczywistym.
- Obsługa logowania (np. przez Google, Facebook, e-mail).
- Zarządzanie analizą użytkowania aplikacji (Firebase Analytics).
- Wysyłanie powiadomień push lub automatyczne skalowanie funkcji backendowych.

---

### **3. Figma (figma.com)**

**Zadania i odpowiedzialności:**

- **Figma** to narzędzie do projektowania interfejsów użytkownika (UI/UX).
- Odpowiada za fazę **projektowania i prototypowania** aplikacji przed jej implementacją.
- Umożliwia współpracę zespołów projektantów i programistów w czasie rzeczywistym.

**Zastosowania:**

- Tworzenie wizualnego projektu aplikacji (np. wygląd ekranów, przycisków, ikon).
- Tworzenie interaktywnych prototypów, które pokazują, jak użytkownik będzie poruszał się po aplikacji.
- Udostępnianie zasobów graficznych programistom (eksport ikon, kolorów, stylów, a także kodu CSS).

---

### **Przepływ informacji między systemami:**

1. **Figma → React Native:**
    
    - Projektanci przygotowują wizualne projekty aplikacji w Figmie (UI/UX).
    - Programiści eksportują projekty z Figmy (np. układ ekranów, style, grafiki) i implementują je w kodzie przy użyciu React Native.
2. **React Native → Firebase:**
    
    - Aplikacja napisana w React Native komunikuje się z Firebase za pomocą jego SDK (Software Development Kit).
    - Dane mogą być wysyłane i pobierane w czasie rzeczywistym z bazy danych Firebase (np. zapisywanie profilu użytkownika, pobieranie listy produktów).
    - Firebase może dostarczać dodatkowe funkcjonalności, takie jak obsługa logowania czy powiadomień push, które aplikacja React Native integruje.
3. **Firebase → React Native/Figma:**
    
    - Firebase gromadzi dane użytkowników i analizy. Na podstawie tych danych zespół projektowy może dostosowywać projekt w Figmie (np. poprawiając UX).
    - Powiadomienia push wysyłane przez Firebase są wyświetlane w aplikacji stworzonej w React Native.

---

### **Podsumowanie przepływu ról i danych:**

- **Figma**: Tworzenie wizualnego projektu → programiści wykorzystują te zasoby w React Native.
- **React Native**: Tworzenie aplikacji mobilnej → aplikacja łączy się z backendem Firebase.
- **Firebase**: Backend dla danych, logowania i innych funkcji → dane są wykorzystywane w aplikacji React Native.
- Informacje przepływają między systemami w sposób płynny, zapewniając spójność między fazami projektowania, implementacji i działania aplikacji.



# wersja 2 odpowiedzi

Omówmy zadania, role i sposób współdziałania podanych narzędzi w procesie tworzenia aplikacji internetowej lub mobilnej:

---

### **1. [React Native (reactnative.dev)]**
**Za co odpowiada?**
React Native to framework służący do tworzenia **aplikacji mobilnych** działających na różnych platformach (iOS, Android) przy użyciu jednego kodu w języku JavaScript. Dzięki temu możliwe jest jednoczesne tworzenie aplikacji na różne urządzenia, co redukuje czas i koszty dewelopmentu.

**Rola w systemie:**
- **Frontend aplikacji mobilnej** – React Native odpowiada za wygląd i działanie interfejsu użytkownika (UI) oraz interakcje użytkownika z aplikacją.
- Generuje natywne komponenty interfejsu użytkownika (np. przyciski, listy, formularze), które są renderowane na urządzeniach mobilnych.

**Jak współdziała z innymi systemami?**
- Komunikuje się z backendem (np. Firebase) w celu pobierania lub zapisywania danych (np. zapytania HTTP/REST lub WebSocket).
- Może korzystać z narzędzi do prototypowania (np. Figma) jako wzoru przy projektowaniu UI.

---

### **2. [Firebase (firebase.google.com)]**
**Za co odpowiada?**
Firebase to platforma od Google dostarczająca zestaw narzędzi backendowych i usług chmurowych, które wspierają rozwój aplikacji.

**Rola w systemie:**
- **Backend aplikacji** – Firebase zajmuje się przechowywaniem danych, autentykacją użytkowników, wysyłaniem powiadomień oraz analityką.
- Najważniejsze usługi:
  - **Firestore / Realtime Database:** Bazy danych w czasie rzeczywistym do przechowywania danych aplikacji.
  - **Authentication:** Obsługa rejestracji i logowania użytkowników.
  - **Hosting:** Możliwość hostowania aplikacji webowych (strony WWW).
  - **Cloud Functions:** Wykonywanie kodu backendowego w odpowiedzi na zdarzenia (np. zapis danych w bazie).
  - **Push Notifications:** Wysyłanie powiadomień push do urządzeń.

**Jak współdziała z innymi systemami?**
- React Native komunikuje się z Firebase w celu wymiany danych (np. pobierania użytkownika zalogowanego, zapisywania wyników użytkownika do bazy danych).
- Firebase może także dostarczać zasoby i dane niezbędne dla komponentów aplikacji projektowanych w React Native.
- Może hostować stronę WWW, która jest częścią systemu (np. wersja desktopowa aplikacji).

---

### **3. [Figma (figma.com)]**
**Za co odpowiada?**
Figma to narzędzie do projektowania interfejsów użytkownika (UI) oraz tworzenia prototypów aplikacji i stron WWW.

**Rola w systemie:**
- **Projektowanie interfejsu użytkownika (UI):** Tworzenie wizualnych projektów aplikacji mobilnych i stron WWW.
- **Prototypowanie:** Figma umożliwia symulowanie działania interfejsu (np. nawigacja między ekranami) bez kodowania.
- **Współpraca zespołowa:** Dzięki narzędziom współdzielenia projektów, programiści i projektanci mogą łatwo wymieniać informacje i współpracować.

**Jak współdziała z innymi systemami?**
- Projekty stworzone w Figmie są przekazywane do deweloperów (np. programistów korzystających z React Native), którzy implementują zaprojektowane interfejsy.
- Deweloperzy mogą używać Figma API do eksportowania zasobów graficznych, takich jak obrazy czy ikony, do aplikacji.

---

### **Przepływ informacji między systemami**
1. **Projektowanie (Figma):**
   - Projektanci tworzą interfejs użytkownika aplikacji i dostarczają gotowe zasoby oraz specyfikacje do zespołu deweloperskiego.
2. **Tworzenie aplikacji mobilnej (React Native):**
   - Programiści implementują projekt interfejsu w kodzie React Native, opierając się na projektach z Figmy.
   - React Native pobiera dane z backendu (Firebase), np. listę użytkowników czy dane produktów.
3. **Backend i dane (Firebase):**
   - Firebase przechowuje dane aplikacji, obsługuje autentykację użytkowników oraz wysyła powiadomienia push.
   - W razie potrzeby Firebase hostuje stronę WWW będącą uzupełnieniem aplikacji.

---

### **Które narzędzie odpowiada za utworzenie strony WWW?**
- **React Native:** Nie tworzy stron WWW – służy do aplikacji mobilnych.
- **Firebase:** Może hostować stronę WWW, ale nie tworzy jej wizualnej warstwy.
- **Figma:** Projektuje wizualną stronę WWW, ale sama jej nie tworzy.
  
Podsumowując: **warstwa wizualna strony WWW** projektowana jest w Figmie, a **hosting** i ewentualne backendowe funkcje zapewnia Firebase. Kod strony WWW jest tworzony przy użyciu innych narzędzi, np. React (nie React Native).