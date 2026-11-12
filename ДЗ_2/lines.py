def show_header(title):
    print("\n" + "=" * 54)
    print(f"  {title}")
    print("=" * 54)


def show_result(result):
    print(f"\n  Результат: {result}")


def normalize_text(text):
    allowed_punctuation = ".,!?:;-"
    cleaned_chars = []

    for char in text:
        if char.isalnum() or char.isspace() or char in allowed_punctuation:
            cleaned_chars.append(char)
        else:
            cleaned_chars.append(" ")

    cleaned = " ".join("".join(cleaned_chars).split())

    for symbol in ".,!?:;":
        cleaned = cleaned.replace(" " + symbol, symbol)

    result_chars = []
    for char in cleaned:
        if char in ".,!?:;" and result_chars and result_chars[-1] == char:
            continue
        result_chars.append(char)

    return "".join(result_chars).strip().capitalize()


def levelchoice(level):

    if level == 1:
        show_header("УРОВЕНЬ 1 · РЕГИСТР БУКВ")
        test = "пРиВет МИР"
        print("Методы: upper(), lower(), capitalize()")
        print(f"\nПример строки: {test!r}")
        print(f"  1. upper()      → {test.upper()}")
        print(f"  2. lower()      → {test.lower()}")
        print(f"  3. capitalize() → {test.capitalize()}")

        raw = input("\nВведите строку и номер метода через запятую\n"
                    "Например: Привет мир, 1\n> ")
        parts = raw.rsplit(",", 1)

        if len(parts) != 2:
            print("Ошибка: введите строку, запятую и номер метода.")
            return

        text = parts[0].strip()
        method = parts[1].strip()
        methods = {
            "1": str.upper,
            "2": str.lower,
            "3": str.capitalize,
        }

        if method not in methods:
            print("Ошибка: выберите метод 1, 2 или 3.")
            return

        show_result(methods[method](text))

    elif level == 2:
        show_header("УРОВЕНЬ 2 · ПОИСК И ЗАМЕНА")
        test = "Очень круто"
        print("Методы: find(), replace(), count()")
        print(f"\nПример строки: {test!r}")
        print(f"  1. find('круто')              → {test.find('круто')}")
        print(f"  2. replace('круто', 'п')      → {test.replace('круто', 'п')}")
        print(f"  3. count('о')                 → {test.count('о')}")

        print("\nФормат ввода:")
        print("  найти; строка; подстрока")
        print("  заменить; строка; старая подстрока; новая подстрока")
        print("  посчитать; строка; подстрока")
        parts = [part.strip() for part in input("\n> ").split(";")]

        if not parts:
            print("Ошибка: ничего не введено.")
            return

        action = parts[0].lower()

        if action == "найти" and len(parts) == 3:
            show_result(parts[1].find(parts[2]))
        elif action == "заменить" and len(parts) == 4:
            show_result(parts[1].replace(parts[2], parts[3]))
        elif action == "посчитать" and len(parts) == 3:
            show_result(parts[1].count(parts[2]))
        else:
            print("Ошибка: проверьте команду и количество аргументов.")

    elif level == 3:
        show_header("УРОВЕНЬ 3 · РАЗДЕЛЕНИЕ И ОБЪЕДИНЕНИЕ")
        test = "Я изучаю Python"
        words = ["Я", "изучаю", "Python"]
        print("Методы: split(), join()")
        print(f"\n  split() → {test.split()}")
        print(f"  '-'.join({words}) → {'-'.join(words)}")

        method = input("\nВыберите метод: 1 — split, 2 — join\n> ").strip()

        if method == "1":
            text = input("Введите строку: ")
            separator = input("Разделитель (Enter — пробелы): ")
            result = text.split(separator) if separator else text.split()
            show_result(result)
        elif method == "2":
            raw_words = input("Введите элементы через ';'\nНапример: Я; изучаю; Python\n> ")
            words = [word.strip() for word in raw_words.split(";")]
            separator = input("Разделитель для объединения (Enter — без него): ")
            show_result(separator.join(words))
        else:
            print("Ошибка: выберите 1 или 2.")

    elif level == 4:
        show_header("УРОВЕНЬ 4 · ПРОВЕРКА И ФОРМАТИРОВАНИЕ")
        print("Методы: isdigit(), isalpha(), strip(), format()")
        print("\n  '12345'.isdigit() →", "12345".isdigit())
        print("  'Привет'.isalpha() →", "Привет".isalpha())
        print("  '  текст  '.strip() →", repr("  текст  ".strip()))
        print("  'Привет, {}!'.format('мир') →", "Привет, {}!".format("мир"))

        method = input("\nВыберите метод: 1–4\n> ").strip()

        if method == "1":
            text = input("Введите строку: ")
            show_result(text.isdigit())
        elif method == "2":
            text = input("Введите строку: ")
            show_result(text.isalpha())
        elif method == "3":
            text = input("Введите строку: ")
            chars = input("Символы для удаления с краёв (Enter — пробелы): ")
            show_result(text.strip(chars) if chars else text.strip())
        elif method == "4":
            template = input("Введите шаблон с полями {}: ")
            values = input("Введите значения через ';'\n> ").split(";")
            values = [value.strip() for value in values]
            try:
                show_result(template.format(*values))
            except (IndexError, KeyError, ValueError) as error:
                print(f"Ошибка форматирования: {error}")
        else:
            print("Ошибка: выберите число от 1 до 4.")

    elif level == 5:
        show_header("УРОВЕНЬ 5 · ОЧИСТКА ТЕКСТА")
        print("Удаляем лишние символы, лишние пробелы и повторы пунктуации.")
        test = "  ***пРИВЕТ   ,,,   мИР!!!###  "
        print(f"\nДо:    {test!r}")
        print(f"После: {normalize_text(test)!r}")

        text = input("\nВведите текст для обработки\n> ")
        show_result(normalize_text(text))

    else:
        print("Ошибка: такого уровня нет. Выберите число от 1 до 5.")


def main():
    """Точка входа в программу."""
    show_header("ТРЕНАЖЁР МЕТОДОВ СТРОК PYTHON")
    print("Выберите уровень:")
    print("  1 — Регистр букв")
    print("  2 — Поиск и замена")
    print("  3 — split() и join()")
    print("  4 — Проверка и форматирование")
    print("  5 — Очистка текста")

    try:
        level = int(input("\nНомер уровня (1–5)\n> ").strip())
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return

    levelchoice(level)


if __name__ == "__main__":
    main()