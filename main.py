def simple_text_editor():
    filename = input("Введіть назву нового файлу (з .txt): ")
    print("Введіть текст (для завершення введення залиште рядок порожнім):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print("\nФайл збережено. Вміст файлу:")
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())

def analyze_file():
    filename = input("Введіть назву файлу для аналізу: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)
        print("\nАналіз файлу:")
        print(f"Кількість рядків: {len(lines)}")
        print(f"Кількість слів: {len(words)}")
        print(f"Кількість символів: {characters}")
    except FileNotFoundError:
        print("Файл не знайдено!")

def find_and_replace():
    filename = input("Введіть назву файлу для редагування: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        find_text = input("Введіть слово або фразу для пошуку: ")
        replace_text = input("Введіть слово або фразу для заміни: ")
        new_content = content.replace(find_text, replace_text)
        new_filename = input("Введіть назву нового файлу для збереження результату: ")
        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print("Заміна виконана. Новий файл збережено.")
    except FileNotFoundError:
        print("Файл не знайдено!")

def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Створити текстовий файл")
        print("2. Аналіз вмісту файлу")
        print("3. Пошук і заміна у файлі")
        print("4. Вийти")
        choice = input("Оберіть дію (1-4): ")
        if choice == "1":
            simple_text_editor()
        elif choice == "2":
            analyze_file()
        elif choice == "3":
            find_and_replace()
        elif choice == "4":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
