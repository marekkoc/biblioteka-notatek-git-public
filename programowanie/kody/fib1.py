#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:15:48 2024
Modified: 2024.10.13

Algorytm fibonacciego na podstawie książki:
    2019#Kopec_Classic-computer-science-problems

@author: marek
"""

def fib1(n:int)->int:
    if n<2: # base case
        return 1
    else:
        return fib1(n-1) + fib1(n-2) # recursive case


if __name__ == "__main__":
    print('dupa lampa')

    print(fib1(4))
