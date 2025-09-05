# def inc(x):
#     return x + 1
#
#
# def test_inc():
#     assert inc(3) == 4


# import pytest
#
#
# def f():
#     raise SystemExit(1)
#
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()


# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "check")


# import pytest
#
#
# @pytest.fixture
# def value():
#     return 7
#
#
# @pytest.fixture()
# def my_set():
#     return {1, 2, 3, 7}
#
#
# def test_f(value, my_set):
#     assert value in my_set
#     # аргументы прописываем в fixture в функции с названием переменной, так как мы не
#     # запускаем именно файл и аргументы никак по-другому в тесте не ввести


# А вот так делать нежелательно (но это пример как оно работает)
# import pytest
#
#
# @pytest.fixture
# def L1():
#     return []
#
#
# @pytest.fixture
# def append_1(L1):
#     L1.append(1)
#
#
# @pytest.fixture
# def append_2(L1, append_1):
#     L1.append(2)
#
#
# @pytest.fixture
# def append_3(L1, append_2):
#     L1.append(3)
#
#
# def test_list(
#     L1, append_3
# ):  # без append_3 ост-е fixture тоже не вызовутся и будет L1=[]
#     print(L1)
#     assert L1 == [1, 2, 3]


# pytest.mark.parametrize

# import pytest
#
#
# @pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected  # AssertionError: assert 54 == 42
#     #  +  where 54 = eval('6*9')


# pytest.mark.parametrize для класса
# import pytest
#
#
# @pytest.mark.parametrize("n, expected", [(1, 2), (3, 4)])
# class TestClass:
#     def test_simple_case(self, n, expected):
#         assert n + 1 == expected
#
#     def test_weird_simple_case(self, n, expected):
#         assert (n * 1) + 1 == expected


# Случай который прога обрабатывать не умеет но и не должна
# мы хотим expected to fail

# import pytest
#
#
# @pytest.mark.parametrize(
#     "test_input, expected",
#     [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
# )
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected # 2 passed, 1 xfailed in 0.39s


# все возможные пары по комбинаторике если parametrize подряд

# import pytest
#
#
# @pytest.mark.parametrize("x", [0, 1, 100])
# @pytest.mark.parametrize("y", [2, 3])  # всего 6 вариантов
# def test_foo(x, y):
#     pass

# import pytest
#
#
# def multiply(x, y):
#     s = 0
#     for _ in range(x):
#         s += y
#     return s  # табл умнож
#
#
# @pytest.mark.parametrize("x", list(range(0, 10)))  # (-10, 10) - не пройдет часть тестов
# @pytest.mark.parametrize("y", list(range(0, 10)))
# def test_multiply(x, y):
#     assert multiply(x, y) == x * y  #  100 passed in 0.36s


# from faker import Faker
#
#
# # fake = Faker("ru_RU")
# # for i in range(100):
# #     print(fake.text())
#
# from faker.providers import internet
# from faker.providers import color
#
# fake = Faker("ru_RU")
# # fake.add_provider(internet)
# #
# # for i in range(100):
# #     print(fake.ipv4_private())
#
# fake.add_provider(color)
#
# for i in range(100):
#     print(fake.color())


# ПИШЕМ СОБСТВЕННЫЙ ФЕЙК
# from faker import Faker
# from faker.providers import DynamicProvider
#
# medical_professions_provider = DynamicProvider(
#     provider_name="medical_profession",
#     elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
# )
#
# fake = Faker()
# fake.add_provider(medical_professions_provider)
#
# print(fake.medical_profession())


# MONKEYPATCHING
# from pathlib import Path
#
#
# def getssh():
#     return Path.home() / ".ssh"
#
#
# def test_getssh(monkeypatch):
#     def mockreturn():
#         return Path("/abc")
#
#     monkeypatch.setattr(Path, "home", mockreturn)
#
#     x = getssh()
#     assert x == Path("/abc/.ssh")


# норм пример MONKEYPATCHING

import requests


def get_json(url):
    r = requests.get(url)
    return r.json()


class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
