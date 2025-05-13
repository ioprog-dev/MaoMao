def spliter(string: str, c: int) -> list[str]:
    # Проверка типов
    if not isinstance(string, str):
        raise TypeError("The first argument must be a string.")
    if not isinstance(c, int):
        raise TypeError("The second argument must be an integer.")

    # Проверка, что длина строки кратна c
    if len(string) % c != 0:
        raise ValueError("The length of the string is not a multiple of the specified chunk size.")

    # Разделение строки на части
    return [string[i:i + c] for i in range(0, len(string), c)]



