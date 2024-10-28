---
Utworzono: 2024-10-13T10:18:00
Zmodyfikowano: 2024-10-28T10:18:00
tags:
---

# Type annotation - type hint

Notatka na podstawie odpowiedzi chatGPT.

W Pythonie **"type hint"** (wskazówka typów) lub **"type annotation"** (anotacja typów) to sposób na informowanie o typach danych używanych w kodzie, co ułatwia jego czytelność, sprawdzanie poprawności oraz narzędziom statycznym wykrywanie potencjalnych błędów.

### Jak to działa?
Type hinting pozwala na wskazanie typów danych dla zmiennych, argumentów funkcji oraz wartości zwracanych przez funkcje, ale nie jest przez Python bezpośrednio egzekwowane (nie wprowadza typowania statycznego). Wskazówki typów działają jako informacja pomocnicza dla programisty oraz narzędzi, takich jak ==**mypy**==, **PyCharm**, czy **VS Code**, do przeprowadzania sprawdzeń typów.

### Przykłady użycia

1. **Anotacja zmiennych**:
   ```python
   age: int = 25
   name: str = "Alice"
   scores: list[int] = [95, 87, 92]
   ```

2. **Type hints w funkcjach**:
   - **Dla argumentów i wartości zwracanej**:
     ```python
     def greet(name: str) -> str:
         return f"Hello, {name}"
     ```
   - **Funkcja z listą jako argument**:
     ```python
     def calculate_average(scores: list[float]) -> float:
         return sum(scores) / len(scores)
     ```

3. **Opcjonalne typy**: Jeśli funkcja może przyjąć wartość `None`, stosujemy **Optional** (dostępne z modułu `typing`):
   ```python
   from typing import Optional

   def get_user_age(user_id: int) -> Optional[int]:
       # Funkcja może zwrócić wiek użytkownika lub None
       ...
   ```

4. **Typy złożone i zagnieżdżone**: Typy dla słowników, tupli, zestawów, itp., można określić przy użyciu `typing.Dict`, `typing.Tuple`, itp.:
   ```python
   from typing import Dict, Tuple

   def get_user_info(user_id: int) -> Dict[str, Tuple[str, int]]:
       # Zwraca słownik, gdzie klucz to str, a wartość to tupla z nazwą i wiekiem
       ...
   ```

### Zalety "type hint"
- **Czytelność**: Kod jest łatwiejszy do zrozumienia.
- **Sprawdzanie błędów**: Narzędzia mogą analizować kod i wykrywać błędy typów.
- **Intuicyjność dla IDE**: Edytory kodu mogą podpowiadać odpowiednie typy danych i autouzupełnianie.

Type hinty to przydatne narzędzie, które zwiększa jakość kodu i wspomaga jego utrzymanie, szczególnie w większych projektach.


## Kilka słów dlaczego stosować "podpowiedzi typów"

Fragment pochodzi z książki: #book-2019-kopec-classic-computer-science-problems-in-python 
ze strony 4:

Every code listing in this book makes use of Python type hints, also known as type
annotations. These annotations are a relatively new feature for the Python language,
and they may look intimidating to Python programmers who have never seen them
before. They are used for three reasons:

1. They provide clarity about the types of variables, function parameters, and function returns
2. They self-document the code in a sense, as a result of reason 1. Instead of having to search through a comment or docstring to find the return type of a function, you can just look at its signature.
3. They allow the code to be type-checked for correctness. One popular Python
type checker is mypy.

They provide clarity about the types of variables, function parameters, and function returns.
They self-document the code in a sense, as a result of reason 1. Instead of having to search through a comment or docstring to find the return type of a function, you can just look at its signature.
They allow the code to be type-checked for correctness. One popular Python type checker  is ==mypy==

# mypy

Odpowiedź z chatGPT

**`mypy`** to pakiet do statycznego sprawdzania typów w Pythonie. Pozwala analizować kod, aby upewnić się, że typy używane w całym programie są zgodne z oczekiwaniami, co pomaga zapobiegać błędom wynikającym z niepoprawnych typów danych. `mypy` współpracuje z type hintami (anotacjami typów) w Pythonie, które programista umieszcza w kodzie dla zmiennych, argumentów funkcji oraz wartości zwracanych.

### Jak działa `mypy`?
1. **Analiza statyczna**: `mypy` działa w czasie statycznym, co oznacza, że sprawdza kod bez jego uruchamiania. Analizuje zgodność typów w oparciu o anotacje typów.
2. **Kompatybilność z PEP 484**: `mypy` opiera się na standardzie **PEP 484**, który wprowadza type hinty do Pythona, i obsługuje także zaawansowane typy, takie jak typy złożone, typy opcjonalne, unie, generatory itp.
3. **Integracja z narzędziami**: `mypy` można zintegrować z edytorami kodu, np. VS Code lub PyCharm, aby sprawdzał typy w locie i pokazywał potencjalne błędy.

### Przykład użycia `mypy`
Poniższy kod zawiera błędne przypisanie typu. `mypy` zasygnalizuje niezgodność między deklarowanym typem `int` a przypisaną wartością `str`:

```python
def add(a: int, b: int) -> int:
    return a + b

result: int = add(5, "10")  # Błąd: drugi argument jest typu `str`, a nie `int`.
```

Jeśli uruchomimy `mypy` na powyższym kodzie:
```bash
mypy script.py
```

To wynik pokaże błąd typu, ponieważ `"10"` jest typu `str`, a nie `int`.

### Dlaczego warto używać `mypy`?
- **Większa niezawodność kodu**: Zapewnia zgodność typów, co zmniejsza liczbę błędów.
- **Lepsza czytelność**: Kod z anotacjami typów jest bardziej przejrzysty i łatwiejszy do zrozumienia.
- **Pomoc w refaktoryzacji**: `mypy` pomaga zidentyfikować potencjalne problemy typowe przy zmianach w kodzie.

`mypy` jest szczególnie przydatny w większych projektach lub tam, gdzie Python współpracuje z różnorodnymi typami danych i złożonymi strukturami, zapewniając lepszą kontrolę nad spójnością typów.