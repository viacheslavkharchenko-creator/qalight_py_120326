"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


def sum_numbers_in_list(input_list):

    if not isinstance(input_list, list):
        raise ValueError("Вхідні дані повинні бути списком!")
    if len(input_list) == 0:
        raise ValueError("Список не може бути порожнім!")
    result = []
    for i in input_list:
        try:
            numbers = i.split(",")
            total_sum = 0
            for num in numbers:
                total_sum += int(num)
            result.append(total_sum)
        except AttributeError:
            result.append("Не можу це зробити! AttributeError")
        except ValueError:
            result.append("Не можу це зробити!")
    return result


if __name__ == "__main__":
    test_result = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(test_result)

    test_result = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(test_result)

    test_result = sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    print(test_result)

    test_result = sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    print(test_result)

    test_result = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    print(test_result)

    test_result = sum_numbers_in_list([])  # ValueError
    print(test_result)

    test_result = sum_numbers_in_list("21")  # ValueError
    print(test_result)

