
import random

random.seed(726)

SIZE = 8

walls = [
    (1, 1), (1, 2), (1, 4),
    (2, 4), (3, 1), (3, 2),
    (4, 5), (5, 5), (6, 2), (6, 3)
]

rooms = {
    (2, 2): "сундук",
    (4, 4): "монстр",
    (5, 2): "ловушка",
    (6, 6): "ключ",
    (7, 7): "портал"
}


# Генераторы коллекций
def generators():
    numbers = [x for x in range(10)]

    even = [x for x in numbers if x % 2 == 0]

    squares = {x: x ** 2 for x in range(5)}

    expression = (x * 2 for x in range(5))

    print("\nГенератор списков:", even)
    print("Генератор словаря:", squares)
    print("Генератор выражений:", list(expression))


# Класс игрока
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.inventory = []

    def move(self, dx, dy):
        nx = self.x + dx
        ny = self.y + dy

        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if (nx, ny) not in walls:
                self.x = nx
                self.y = ny
                return True

        print("Там стена!")
        return False

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print("Предмет удалён")
        else:
            print("Предмет не найден")


# Создание игрока
player = Player(0, 0)

visited = set()


# Генератор видимых клеток
def visible_cells():
    for x in range(max(0, player.x - 1),
                   min(SIZE, player.x + 2)):
        for y in range(max(0, player.y - 1),
                       min(SIZE, player.y + 2)):
            yield (x, y)


# Отображение лабиринта
def show_map():
    print("\nЛАБИРИНТ")

    for y in range(SIZE):
        for x in range(SIZE):

            pos = (x, y)

            if pos == (player.x, player.y):
                print("P", end=" ")
            elif pos not in visited:
                print("*", end=" ")
            elif pos in walls:
                print("#", end=" ")
            elif pos in rooms:
                print("?", end=" ")
            else:
                print(".", end=" ")

        print()


# Проверка комнат
def check_room():
    pos = (player.x, player.y)

    if pos not in rooms:
        return False

    room = rooms[pos]

    if room == "сундук":
        print("Ты нашёл сундук!")
        player.inventory.append("монета")
        player.inventory.extend(["зелье", "меч"])
        del rooms[pos]

    elif room == "монстр":
        print("Ты встретил монстра!")
        player.health -= 20
        print("Здоровье -20")
        del rooms[pos]

    elif room == "ловушка":
        print("Ты попал в ловушку!")
        player.health -= 30
        del rooms[pos]

    elif room == "ключ":
        print("Ты нашёл ключ!")
        player.inventory.append("ключ")
        del rooms[pos]

    elif room == "портал":
        if "ключ" in player.inventory:
            print("Портал открыт! ПОБЕДА!")
            return True
        else:
            print("Для портала нужен ключ!")

    return False


# Инвентарь
def inventory_menu():
    while True:
        print("\n--- ИНВЕНТАРЬ ---")
        print(player.inventory)

        print("1 - Добавить предмет")
        print("2 - Выбросить предмет")
        print("3 - Выбросить по номеру")
        print("4 - Сортировать")
        print("5 - Перевернуть список")
        print("6 - Найти предмет")
        print("7 - Изменить предмет")
        print("8 - Копировать инвентарь")
        print("9 - Показать генераторы")
        print("0 - Назад")

        choice = input("Выбор: ")

        if choice == "1":
            item = input("Название предмета: ")
            player.inventory.append(item)

        elif choice == "2":
            item = input("Что выбросить? ")
            player.remove_item(item)

        elif choice == "3":
            if player.inventory:
                index = int(input("Номер предмета: "))

                if 0 <= index < len(player.inventory):
                    item = player.inventory.pop(index)
                    print("Выброшено:", item)
                else:
                    print("Неверный номер")
            else:
                print("Инвентарь пуст")

        elif choice == "4":
            player.inventory.sort()
            print("Отсортировано")

        elif choice == "5":
            player.inventory.reverse()
            print("Список перевёрнут")

        elif choice == "6":
            item = input("Что ищем? ")

            if item in player.inventory:
                print("Индекс:", player.inventory.index(item))
            else:
                print("Не найдено")

        elif choice == "7":
            if player.inventory:
                index = int(input("Номер предмета: "))

                if 0 <= index < len(player.inventory):
                    new_item = input("Новое название: ")
                    player.inventory[index] = new_item
                else:
                    print("Неверный номер")
            else:
                print("Инвентарь пуст")

        elif choice == "8":
            copied = player.inventory[:]

            print("Оригинал:", player.inventory)
            print("Копия:", copied)

            if copied:
                copied[0] = "изменённый предмет"

            print("Изменённая копия:", copied)
            print("Оригинал остался:", player.inventory)

        elif choice == "9":
            generators()

        elif choice == "0":
            break


# Основная игра
def game():
    print("=== ЛАБИРИНТ ===")
    print("W - вверх")
    print("S - вниз")
    print("A - влево")
    print("D - вправо")
    print("I - инвентарь")
    print("Q - выход")

    while player.health > 0:

        # Открываем клетки вокруг игрока
        for cell in visible_cells():
            visited.add(cell)

        show_map()

        print("\nЗдоровье:", player.health)
        print("Координаты:", player.x, player.y)

        command = input("Твой ход: ").lower()

        if command == "w":
            player.move(0, -1)

        elif command == "s":
            player.move(0, 1)

        elif command == "a":
            player.move(-1, 0)

        elif command == "d":
            player.move(1, 0)

        elif command == "i":
            inventory_menu()

        elif command == "q":
            print("Выход из игры")
            break

        else:
            print("Неизвестная команда")

        if check_room():
            break

    if player.health <= 0:
        print("Ты проиграл!")


game()
