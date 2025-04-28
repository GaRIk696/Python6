# Тестирование корректности работы со строками

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def test():
    assert is_palindrome(" ") == True

    assert is_palindrome("казак") == True
    assert is_palindrome("Peep") == True
    assert is_palindrome("Do geese see God") == True
    assert is_palindrome("Pull up if I pull up") == True
    assert is_palindrome("Лидер бодро, гордо бредил") == True
    assert is_palindrome("Не палиндром") == False

    assert is_palindrome("") == True
    assert is_palindrome("a") == True

    assert is_palindrome("  ") == True

    assert is_palindrome("Race fast, safe car!") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("123321") == True
    assert is_palindrome("A1B2B1A") == True
    assert is_palindrome("A1B2C3") == False

    assert is_palindrome("Level") == True
    assert is_palindrome("LevEL") == True
    assert is_palindrome("Python") == False

    assert is_palindrome("!!!") == True
    assert is_palindrome(".,!") == True
    assert is_palindrome("..a..") == True

    print("Все тесты пройдены успешно!")

test()