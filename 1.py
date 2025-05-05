def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


assert average_num([10, 20, 30]) == 20.0
assert average_num([1.5, 2.5, 3.5]) == 2.5
assert average_num([1, 2.5, 3, 4.5]) == 2.75
assert average_num(['10', '20', '30']) == 20.0
assert average_num([5, '10', 15.0]) == 10.0
assert average_num([7]) == 7.0
assert average_num([-5, 0, 5]) == 0.0
assert average_num(['a', 'b', 'c']) == "Bad request"
assert average_num([10, '20', 'x']) == "Bad request"
assert average_num([1000000, 2000000, 3000000]) == 2000000.0


print("Пройдено успешно!")