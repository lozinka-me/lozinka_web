import re

def password_strength(password):
    # Dužina lozinke
    length = len(password)

    # Cifre
    digits = len(re.findall(r"\d", password))

    # Slova
    letters = len(re.findall(r"[a-zA-Z]", password))

    # Veliko slovo
    uppercase = len(re.findall(r"[A-Z]", password))

    # Malo slovo
    lowercase = len(re.findall(r"[a-z]", password))

    # Simboli
    symbols = len(re.findall(r"\W", password))

    return {
        'length' : length,
        'letters': letters,
        'digits' : digits,
        'uppercase' : uppercase,
        'lowercase' : lowercase,
        'symbols' : symbols,
    }