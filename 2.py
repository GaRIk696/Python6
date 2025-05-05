def is_palin(s: str) -> bool:
    if not isinstance(s, str):
        raise ValueError("Входные данные должны быть строкой")
    cleaned = ''.join(filter(str.isalnum, s.lower()))
    return cleaned == cleaned[::-1]

def test():
    assert is_palin("") == True
    assert is_palin("э") == True
    assert is_palin("11") == True
    assert is_palin("Лёша на полке клопа нашёл") == True
    assert is_palin("А роза упала на лапу Азора") == True
    assert is_palin("Я иду с мечем судия") == True
    assert is_palin("Madam, I'm Adam") == True

    assert is_palin("мама мыла раму") == False
    assert is_palin("Python") == False
    assert is_palin("3245768090-09876") == False
    assert is_palin("Was it a car or a cat I saw?") == True
    assert is_palin("No 'x' in Nixon") == True
    assert is_palin("A1B2B1A") == True
    assert is_palin("Level") == True

    print("Пройдено успешно!")


test()