# Тестирование. Библиотека PyTest


# Task 1.
# Ознакомьтесь с программой Task Manager, которая предназначена для управления задачами.
# Проведите тестирование для алгоритма, используемого в системе управления задачами.

import datetime
import pytest

from app.task_manager import Task, TaskList

# 1. Тест инициализации задачи test_task_initialization:
# Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры sample_task.
# Убедиться, что приоритет равен 1, дедлайн не установлен и задача не помечена как завершенная.


@pytest.fixture(params=["Sample Task 1", "Sample Task 2"])
def sample_task(request):
    return Task(request.param)


@pytest.fixture
def task_list():
    return TaskList()


def test_task_initialization(sample_task):
    assert sample_task.description.startswith("Sample Task")
    assert sample_task.priority == 1
    assert sample_task.deadline is None
    assert sample_task.is_completed == False


# 2. Тест отметки задачи как выполненной test_mark_completed:
# Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры sample_task.
# Вызвать метод mark_completed() для того, чтобы отметить задачу как выполненную.
# Убедиться, что статус выполнения изменился на "Выполнено".


def test_mark_completed(sample_task):
    sample_task.mark_completed()
    assert sample_task.is_completed == True


# 3. Тест установки дедлайна для задачи test_set_deadline:
# Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры sample_task.
# Установить deadline для задачи, используя модуль datetime.
# Установить дедлайн для задачи с использованием метода set_deadline() и передать в него созданный объект дедлайна deadline.
# Проверить, что дедлайн задачи sample_task теперь соответствует установленному дедлайну deadline.


def test_set_deadline(sample_task):
    deadline = datetime.datetime(2025, 9, 15)
    sample_task.set_deadline(deadline)
    assert sample_task.deadline == deadline


# 4. Тест строкового представления задачи test_task_string_representation:
# Создать экземпляр задачи с описанием, полученным из параметризованной фикстуры sample_task.
# Убедиться, что строковое представление задачи str(sample_task) соответствует ожидаемому формату, который создается на основе атрибутов задачи:
# "Description: [описание]
#  Priority: 1
#  Status: Not Completed
#  No Deadline"


def test_task_string_representation(sample_task):
    str_representation = (
        f"Description: {sample_task.description}\n"
        f"Priority: 1\n"
        f"Status: Not Completed\n"
        f"No Deadline\n"
    )
    assert str(sample_task) == str_representation


# 5. Тест инициализации списка задач test_tasklist_initialization:
# Создать пустой список задач TaskList.
# Убедиться, что список задач пуст.


def test_tasklist_initialization(task_list):
    assert task_list.tasks == []


# 6. Тест добавления задачи в список test_add_task:
# С помощью метода add_task() добавить задачу sample_task с заданным описанием "Sample Task" в список задач task_list.
# Убедиться, что список содержит одну задачу.
# Убедиться, что sample_task находится в списке задач.


def test_add_task(task_list, sample_task):
    task_list.add_task(sample_task)
    assert len(task_list.tasks) == 1
    assert sample_task in task_list.tasks


# 7. Тест удаления задач из списка test_remove_task:
# Добавить задачу с описанием, полученным из параметризованной фикстуры sample_task, в список задач task_list.
# Вызвать метод remove_task() для удаления задачи sample_task из списка.
# Убедиться, что после удаления задачи, количество задач в списке task_list уменьшилось на 1.
# Также убедиться, что удаленная задача sample_task больше не присутствует в списке задач task_list.


def test_remove_task(task_list, sample_task):
    task_list.add_task(sample_task)
    task_list.remove_task(sample_task)
    assert len(task_list.tasks) == 0
    assert sample_task not in task_list.tasks


# 8. Тест сортировки задач по приоритету test_sort_by_priority:
# Добавить в список задач task_list две задачи task1 и task2 с разными приоритетами.
# Вызвать метод sort_by_priority() для сортировки задач в списке task_list.
# Убедиться, что задачи в списке расположены в порядке убывания приоритета. Чем больше значение, тем выше приоритет задачи.


def test_sort_by_priority(task_list):
    task1 = Task("task 1", 3)
    task2 = Task("task 2", 1)

    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.sort_by_priority()

    assert task_list.tasks[0].priority > task_list.tasks[1].priority
    assert task_list.tasks == [task1, task2]


# 9. Тест фильтрации задач по статусу выполнения test_filter_by_status:
# Добавить в список задач task_list две задачи task1 и task2. Одну из задач пометить как выполненная.
# Выполнить фильтрацию задач по статусу выполнения "Выполнено".
# Убедиться, что в результирующем списке содержится только выполненная задача.


def test_filter_by_status(task_list):
    task1 = Task(
        "task 1",
    )
    task2 = Task(
        "task 2",
    )

    task_list.add_task(task1)
    task_list.add_task(task2)
    task2.mark_completed()

    completed_tasks = task_list.filter_by_status(completed=True)

    assert completed_tasks == [task2]
    assert len(completed_tasks) == 1


# Task 2
# Задача 2.
# Ознакомьтесь с программой Watering System, которая предназначена для управления системой полива почвы.
# Проведите тестирование для алгоритма, используемого в системе полива.

import pytest
from app.watering_system import WateringSystem


# 1. Тест на начальный уровень влажности участка test_initial_soil_moisture:
# Создать экземпляр системы автоматического полива с заданным участком Garden и начальным уровнем влажности 30% с помощью фикстуры watering_system.
# Проверить, что начальный уровень влажности участка Garden равен 30%.


@pytest.fixture
def watering_system():
    system = WateringSystem()
    system.add_area("Garden", 30)
    # system.water_spray_supply("Garden", 10)

    system.add_area("Flowerbed", 25)
    system.water_spray_supply("Flowerbed", 8)
    return system


def test_initial_soil_moisture(watering_system):
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


# 2. Тест на добавление воды в систему test_add_water:
# Создать экземпляр системы автоматического полива с начальным уровнем воды 2000 мл с помощью фикстуры watering_system.
# Вызвать метод add_water с параметром 500 для добавления 500 мл воды.
# Проверить, что уровень воды в системе стал равен 2500 мл.


def test_add_water(watering_system):
    watering_system.add_water(500)
    assert watering_system.water_level == 2500


# 3. Тест на добавление уже существующего участка test_add_existing_area:
# Создать экземпляр системы автоматического полива с заданным участком Garden и начальным уровнем влажности 30% с помощью фикстуры watering_system.
# Вызвать метод add_area с параметром Garden и новым начальным уровнем влажности 50.
# Проверить, что метод add_area не изменил начальный уровень влажности участка Garden (остался 30%).


def test_add_existing_area(watering_system):
    watering_system.add_area("Garden", 50)
    assert watering_system.areas["Garden"]["soil_moisture"] == 30


# 4. Тест на добавление нового участка test_add_new_area:
# Создать экземпляр системы автоматического полива с пустым списком участков с помощью фикстуры watering_system.
# Вызвать метод add_area с параметром Lawn и начальным уровнем влажности 40.
# Проверить, что участок Lawn добавлен в систему.


def test_add_new_area(watering_system):
    result = watering_system.add_area("Lawn", 40)
    assert result is None
    assert "Lawn" in watering_system.areas


# 5. Тест для проверки подачи воды test_water_spray_supply:
# Создать экземпляр системы автоматического полива с заданным участком Garden и начальным уровнем влажности 30% с помощью фикстуры watering_system.
# Вызвать метод test_water_spray_supply с параметрами Garden и скоростью подачи воды 15.
# Проверить, что скорость подачи воды для участка Garden стала равной 15.


def test_water_spray_supply(watering_system):
    watering_system.water_spray_supply("Garden", 15)
    assert watering_system.areas["Garden"]["spray_water"] == 15


# 6. Тест для проверки уровня влажности после полива test_water_area:
# Создать экземпляр системы автоматического полива с заданными участками с помощью фикстуры watering_system.
# Параметры теста: area (участок для полива), duration (продолжительность полива в минутах) и expected_moisture (ожидаемый уровень влажности после полива).
# Вызвать метод water_area с заданными параметрами.
# Проверить, что уровень влажности на участке после полива соответствует ожидаемому.


@pytest.mark.parametrize(
    "area, duration, expected_moisture", [("Garden", 30, 100), ("Flowerbed", 25, 100)]
)
def test_water_area(watering_system, area, duration, expected_moisture):
    watering_system.water_area(area, duration)
    assert watering_system.areas[area]["soil_moisture"] == expected_moisture


# 7. Тест на полив при нехватке воды test_water_area_not_enough_water:
# Создать экземпляр системы автоматического полива с начальным уровнем воды 0 мл с помощью фикстуры watering_system.
# Вызвать метод water_area с параметрами Garden (участок для полива) и duration (продолжительность полива в минутах) 30.
# Проверить, что метод water_area возвращает None, так как не хватает воды для полива.


def test_water_area_not_enough_water(watering_system):
    watering_system.water_level = 0
    result = watering_system.water_area("Garden", 30)
    assert result is None


# 8. Тест на полив при максимальной влажности test_max_soil_moisture:
# Создать экземпляр системы автоматического полива с заданным участком Garden и максимальным уровнем влажности 100% с помощью фикстуры watering_system.
# Вызвать метод water_area с параметрами Garden и duration 30.
# Проверить, что метод water_area не выполнил полива, так как уровень влажности уже максимальный.


def test_max_soil_moisture(watering_system):
    watering_system.areas["Garden"]["soil_moisture"] = 100
    result = watering_system.water_area("Garden", 30)
    assert result is None


# 9. Тест для проверки влажности почвы после длительного полива test_soil_moisture_after_long_watering:
# Создать экземпляр системы автоматического полива с заданным участком Garden и начальным уровнем влажности 30% с помощью фикстуры watering_system.
# Вызвать метод water_area с параметрами Garden и duration 60 (продолжительность полива в минутах).
# Проверить, что после длительного полива уровень влажности на участке Garden стал максимальным (100%).


def test_soil_moisture_after_long_watering(watering_system):
    watering_system.water_area("Garden", 60)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100


# 10. Тест на проверку влажности почвы после полива test_soil_moisture_after_watering:
# Создать экземпляр системы автоматического полива с заданным участком Garden и начальным уровнем влажности 30% с помощью фикстуры watering_system.
# Вызвать метод water_area с параметрами Garden и duration 30 (продолжительность полива в минутах).
# Проверить, что после полива уровень влажности на участке Garden стал максимальным (100%).


def test_soil_moisture_after_watering(watering_system):
    watering_system.water_area("Garden", 30)
    assert watering_system.areas["Garden"]["soil_moisture"] == 100


# Примечание: используйте параметризованную фикстуру watering_system, которая создает экземпляр класса WateringSystem и
# настраивает его с определенными участками для полива и расписанием. А именно:
# 1) Добавляет участок Garden с начальным уровнем влажности 30%, и устанавливает скорость подачи воды 10.
# 2) Добавляет участок Flowerbed с начальным уровнем влажности 25%, и устанавливает скорость подачи воды 8.
# А также используйте фикстуру, которая определяет разные сценари полива и ожидаемые результаты. Это позволит создавать
# новые списки задач для каждого теста. Таким образом, мы обеспечиваем изоляцию между тестами и удостоверяемся, что
# каждый тест не зависит от состояния других тестов. Это важно для корректного тестирования функциональности.
