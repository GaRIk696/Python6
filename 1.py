def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

def test():
    assert average_num([1, 2, 3, 4, 5]) == 3.0
    assert average_num([1, 2, 3]) == 2
    assert average_num([10, 20, 30, 40]) == 25
    assert average_num([1.5, 2.5, 3.5]) == 2.5
    assert average_num([0.1, 0.2, 0.3]) == 0.2
    assert average_num([1, 2.5, 3]) == 2.17
    assert average_num(['1', '2', '3']) == 2
    assert average_num([1, 2.5, "3"]) == 2.17
    assert average_num(['a', 'b', 'c']) == "Bad request"
    assert average_num([1, 2, 'xyz']) == "Bad request"

    print("Все тесты пройдены успешно!")

test()