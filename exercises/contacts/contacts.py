#Телефонный справочник
contacts = {}

# Читаем контакты из файла
try:
    with open("contacts.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                name, phone = line.split(":", 1)
                contacts[name.strip()] = phone.strip()

except FileNotFoundError:
    print("Файл не найден. Создадим его при сохранении.")

# Меню программы
while True:
    print("\n--- Телефонный справочник ---")
    print("1 - Добавить контакт")
    print("2 - Найти контакт")
    print("3 - Удалить контакт")
    print("4 - Показать все контакты")
    print("5 - Сохранить и выйти")

    choice = input("Выбери действие: ").strip()

    if choice == "1":
        name = input("Введите имя: ").strip()
        phone = input("Введите номер: ").strip()

        contacts[name] = phone
        print("Контакт добавлен!")

    elif choice == "2":
        name = input("Введите имя для поиска: ").strip()

        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Не найден")

    elif choice == "3":
        name = input("Введите имя для удаления: ").strip()

        try:
            contacts.pop(name)
            print("Контакт удалён!")
        except KeyError:
            print("Контакт не найден")

    elif choice == "4":
        if contacts:
            for k, v in contacts.items():
                print(k, ":", v)
        else:
            print("Справочник пуст")

    elif choice == "5":
        try:
            with open("contacts.txt", "w", encoding="utf-8") as file:
                for k, v in contacts.items():
                    file.write(f"{k}:{v}\n")

            print("Контакты сохранены. До свидания!")
            break

        except OSError:
            print("Ошибка при сохранении файла")

    else:
        print("Неверный выбор. Введи число от 1 до 5.")
