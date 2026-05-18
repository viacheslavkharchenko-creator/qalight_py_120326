"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
from functions_for_test import *
import pytest
"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def test_add():
    assert add(1,2)==3
    assert add(23,0)==23
    assert add(-1,-2)==-3

"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def test_is_even():
    assert is_even(30)
    assert is_even(15) is False
    assert is_even(-7) is False


"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def test_reverse_string():
    assert reverse_string("qqwwee") == "eewwqq"
    assert reverse_string("") == ""
    assert reverse_string("q") == "q"


"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def test_find_min():
    assert find_min([5,2,3,4,1,2,8])==1
    assert find_min([2])==2
    assert find_min([-100,-20,-34,-2,0])==-100


"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def test_contains_substring():
    assert contains_substring("QALight the best", "best") is True
    assert contains_substring("QALight the best", "Best") is False
    assert contains_substring("QALight the best", "") is True


"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
def test_divide():
    assert divide(6,2) == 3
    assert divide(10,-2) == -5
    with pytest.raises(ValueError):
        divide(123,0)

"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""
def test_is_palindrome():
    assert is_palindrome("qwerewq")
    assert is_palindrome("qwee") is False
    assert is_palindrome("")

"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
def test_sum_list():
    assert sum_list([1,2,3,4,5])==15
    assert sum_list([])==0
    assert sum_list([-1,-2,-3,3])==-3

"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
def test_to_upper():
    assert to_upper("asd") == "ASD"
    assert to_upper("ASD") == "ASD"
    assert to_upper("") == ""