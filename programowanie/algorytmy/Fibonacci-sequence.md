---
Data utworzenia: 2024-10-12
Data modyfikacji: 2024-10-12T23:24:00
Opis: Algorytm Fibonacciego
tags:
  - "#Fibonacci-algorytm"
Uwagi: 
To do: 
"Skrypt:":
---


Żródło: [Książka]() 
Tytuł : [2019#Kopec_Classic-comuter-science-problems-in-Python](), Rozdział 1


# Algorytm

W ciągu liczb Fibonacciego każda kolejna liczba (oprócz dwóch pierwszych) jest równa sumie dwóch liczb poprzednich:

$0, 1, 1, 2, 3, 5, 8, 13, 21, ...$

Zatem ogólne równianie które opisuje ciąg Fibonacciego jest następujące:

$$ fib(n) = fib(n-1) + fib(n-2) $$

Aby zaimplementować funkcję która oblicza dowolny element kodu Fibonacciego, możemy użyć **funkcji rekursywnej**. Funkcja **rekursywna** to taka funkcja, która wywołuje samą siebie.

```Python
def fib1(n: int) -> int:
	return fib(n-1) + fib(n-2)
```

W funkcji rekursywnej musimy zdefiniować **warunek bazowy**, taki warunek, który w odpowiednim miejscu przerwie wykonywanie się funkcji.