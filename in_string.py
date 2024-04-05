def check_vowels():
    # Código a implementar utilizando input.
    entrada = input(">").lower()

    vocales = ["a", "e", "i", "o", "u"]

    for v in vocales:
        print(f"Contiene {v}: {v in entrada}")


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
